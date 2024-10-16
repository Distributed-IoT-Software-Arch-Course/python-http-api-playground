from json import JSONDecodeError
from flask import request, Response
from flask_restful import Resource
from dto.location_entity_response import LocationEntityResponse
from dto.location_update_request import LocationUpdateRequest
from model.location_model import LocationModel


class LocationResource(Resource):
    """ Location Resource for handling HTTP requests related to a single Location """


    def __init__(self, **kwargs):
        """ Constructor injecting the DataManager instance """
        self.data_manager = kwargs['data_manager']

    def get(self, location_id):
        """ HTTP GET Method to retrieve a single Location Resource """

        # Check if the location exists in the dictionary
        if location_id in self.data_manager.location_dictionary:

            # Retrieve the Location Model from the DataManager
            location = self.data_manager.location_dictionary[location_id]

            # Iterate over the dictionary to build a serializable device id list
            device_id_list = []
            for device in location.device_dictionary.values():
                device_id_list.append(device.uuid)

            # Create a LocationEntityResponse object to serialize the data
            location_entity_response = LocationEntityResponse(location.uuid,
                                                              location.name,
                                                              location.latitude,
                                                              location.longitude,
                                                              device_id_list)

            # Return the serialized data and 200 OK code
            return location_entity_response.__dict__, 200
        else:
            return {'error': "Location Not Found !"}, 404

    def delete(self, location_id):
        """ HTTP DELETE Method to remove a single Location Resource """
        try:
            # Check if the location exists in the dictionary
            if location_id in self.data_manager.location_dictionary:
                # Remove the location from the dictionary
                self.data_manager.remove_location(location_id)

                # Return 204 No Content
                return Response(status=204)
            else:
                return {'error': "Location UUID not found"}, 404
        except Exception as e:
            return {'error': "Generic Internal Server Error ! Reason: " + str(e)}, 500

    def put(self, location_id):
        """ HTTP PUT Method to update a single Location Resource """

        try:
            # Check if the location exists in the dictionary
            if location_id in self.data_manager.location_dictionary:

                # The boolean flag force the parsing of POST data as JSON irrespective of the mimetype
                json_data = request.get_json(force=True)
                location_update_request = LocationUpdateRequest(**json_data)

                # Check if the location exists in the dictionary
                if location_update_request.uuid not in self.data_manager.location_dictionary:
                    # return data and 200 OK code
                    return {'error': "Location UUID not found exists"}, 404
                else:
                    # Create a new Location Model with the updated data
                    updated_location_model = LocationModel(location_update_request.uuid,
                                                           location_update_request.name,
                                                           location_update_request.latitude,
                                                           location_update_request.longitude)

                    # Update the location in the dictionary
                    self.data_manager.update_location(updated_location_model)

                    # Return 204 No Content
                    return Response(status=204)
            else:
                return {'error': "Location UUID not found"}, 404
        except JSONDecodeError:
            return {'error': "Invalid JSON ! Check the request"}, 400
        except Exception as e:
            return {'error': "Generic Internal Server Error ! Reason: " + str(e)}, 500
