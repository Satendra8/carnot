from django.shortcuts import render
from Device.models import get_client
import json
from datetime import datetime
from django.http import HttpResponse
import pandas as pd
from datetime import datetime
import os

# Create your views here.

def load_data(request):
    # Read the Excel file
    file_path = os.path.join(os.path.dirname(__file__), 'RawDataBackendDeveloper.csv')
    print(file_path)
    df = pd.read_csv(file_path)

    # Sort by the sts column
    df = df.sort_values('sts')

    rclient = get_client()

    for index, row in df.iterrows():
        print("row",index)

        device_fk_id = row['device_fk_id']
        time_stamp = row['time_stamp']

        data = {
        "device_fk_id": device_fk_id,
        "latitude": row['latitude'],
        "longitude": row['longitude'],
        "time_stamp": time_stamp,
        "sts": row['sts'],
        "speed": row['speed']
        }

        timestamp_obj = datetime.strptime(time_stamp, '%Y-%m-%dT%H:%M:%SZ')
        unix_timestamp = int(timestamp_obj.timestamp())
        rclient.hset(device_fk_id, unix_timestamp, json.dumps(data))
        rclient.zadd(f"{device_fk_id}_timestamps", {unix_timestamp: unix_timestamp})
    return HttpResponse({"Data Successfully inserted"})



def get(request, device_fk_id):
    r_client = get_client()
    timestamps = r_client.zrange(f"{device_fk_id}_timestamps", -1, -1)
    data = r_client.hmget(device_fk_id, timestamps)
    data = {"results": [json.loads(d) for d in data if d is not None]}
    return HttpResponse(json.dumps(data))



def get_device_location(request, device_fk_id):
    r_client = get_client()
    # Get timestamps for device
    timestamps = r_client.zrange(f"{device_fk_id}_timestamps", 0, -1)
    
    # Get data for timestamps
    data = r_client.hmget(device_fk_id, timestamps)
    data = [json.loads(d) for d in data if d is not None]
    
    # Get start and end locations
    start_location = (data[0]['latitude'], data[0]['longitude'])
    end_location = (data[-1]['latitude'], data[-1]['longitude'])
    result = {"results": [start_location, end_location]}
    return HttpResponse(json.dumps(result))


def get_device_location_points(request, device_fk_id):
    start_time = request.GET['start_time']
    end_time = request.GET['end_time']
    timestamp_obj = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%SZ')
    start_unix_timestamp = int(timestamp_obj.timestamp())

    timestamp_obj = datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%SZ')
    end_unix_timestamp = int(timestamp_obj.timestamp())

    r_client = get_client()
    # Get timestamps within the specified time range
    timestamps = r_client.zrangebyscore(f"{device_fk_id}_timestamps", start_unix_timestamp, end_unix_timestamp)
    # Get data for timestamps
    data = r_client.hmget(device_fk_id, timestamps)
    data = [json.loads(d) for d in data if d is not None]
    # Extract latitude, longitude, and timestamp from data
    location_points = [(d['latitude'], d['longitude'], d['time_stamp']) for d in data]
    result = {"results": location_points}
    
    return HttpResponse(json.dumps(result))

