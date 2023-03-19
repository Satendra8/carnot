This project contains four endpoints that are used for loading, and retrieving, data related to device location. The following is a brief description of each endpoint.

# Endpoint 1: load-data
Method: GET
URL: http://127.0.0.1:8003/load-data/
Description:

This endpoint is used for loading data into from csv file to redis.

# # Endpoint 2: get
Method: GET
URL: http://127.0.0.1:8003/get/20984
Description:

This API takes device ID and returns device’s latest information in response.


# # #Endpoint 3: get-device-location
Method: GET
URL: http://127.0.0.1:8003/get-location/20984
Description:

This API takes device ID and returns start location & end location for that device.
Location should be (lat, lon) tuple.

# # # #Endpoint 4: get_device_location_points
Method: GET
URL: http://127.0.0.1:8003/get-all-locations/25029?start_time=2021-10-23T13:33:29Z&end_time=2021-10-23T13:40:58Z

Description:

This API takes in device ID, start time & end time and returns all the location
points as list of latitude, longitude & time stamp.

* * The Entire data stored in redis cache is in redis_data.csv file

