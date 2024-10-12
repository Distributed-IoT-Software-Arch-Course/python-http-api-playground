from flask import Flask
from flask_restful import Resource, Api, reqparse
from resources.device_resource import DeviceResource
from resources.devices_resource import DevicesResource
from resources.locations_resource import LocationsResource
from resources.location_resource import LocationResource
from persistence.data_manager import DataManager
from model.location_model import LocationModel
from model.device_model import DeviceModel

# Create Flask App
app = Flask(__name__)

# Create RESTful API
api = Api(app)

# Define API Endpoint Prefix
ENDPOINT_PREFIX = "/api/iot/inventory"

print("Starting HTTP RESTful API Server ...")

# Create Data Manager to handle the data of locations and devices
data_manager = DataManager()

# Add Locations Resource to handle the list of locations
api.add_resource(LocationsResource, ENDPOINT_PREFIX + '/location',
                 resource_class_kwargs={'data_manager': data_manager},
                 endpoint="locations",
                 methods=['GET', 'POST'])

# Add Location Resource to handle a specific location by its id
api.add_resource(LocationResource, ENDPOINT_PREFIX + '/location/<string:location_id>',
                 resource_class_kwargs={'data_manager': data_manager},
                 endpoint='location',
                 methods=['GET', 'PUT', 'DELETE'])

# Add Devices Resource to handle the list of devices for a specific location
api.add_resource(DevicesResource, ENDPOINT_PREFIX + '/location/<string:location_id>/device',
                 resource_class_kwargs={'data_manager': data_manager},
                 endpoint="devices",
                 methods=['GET', 'POST'])

# Add Device Resource to handle a specific device by its id and the associated location id
api.add_resource(DeviceResource, ENDPOINT_PREFIX + '/location/<string:location_id>/device/<string:device_id>',
                resource_class_kwargs={'data_manager': data_manager},
                 endpoint='device',
                 methods=['GET', 'PUT', 'DELETE'])

# Start the Flask App
if __name__ == '__main__':

    # Create Demo Data for the API in order to have some data to work with

    # Demo Location
    demo_location = LocationModel("l0001",
                                  "TestBuilding",
                                  48.312321,
                                  10.433423211)

    # Add New Location
    data_manager.add_location(demo_location)

    # Demo Device for the previous location
    demo_device = DeviceModel("d0001",
                              "demo-device",
                              demo_location.uuid,
                              DeviceModel.DEVICE_TYPE_DEFAULT,
                              "ACME Inc",
                              "0.0.1beta",
                              48.312321,
                              10.433423211)

    # Add New Device
    data_manager.add_device(demo_location.uuid, demo_device)

    # Run the Flask App
    app.run(host='0.0.0.0', port=7070)  # run our Flask app