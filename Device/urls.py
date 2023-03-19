from django.urls import path
from . import views


urlpatterns = [
    path('load-data/', views.load_data, name='load_data'),
    path('get/<int:device_fk_id>', views.get, name='get'),
    path('get-location/<int:device_fk_id>', views.get_device_location, name='get_device_location'),
    path('get-all-locations/<int:device_fk_id>', views.get_device_location_points, name='get_device_location_points'),
]