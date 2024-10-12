# Python - IoT Inventory - Demo RESTful HTTP API

This project shows a demo implementation of a simple IoT device and location inventory through 
an HTTP RESTful API.

The structure of the playground is the following:

- [Libraries, Frameworks, and Dependencies](#libraries-frameworks-and-dependencies)
- [Modeled REST Resources](#modeled-rest-resources)
- [Project Structure](#project-structure)
- [Running the Project](#running-the-project)
- [Postman Collection](#postman-collection)

## Libraries, Frameworks, and Dependencies

The implementation is based on the following Python Frameworks 

- Flask: https://flask.palletsprojects.com/en/2.0.x/
- Flask RESTful: https://flask-restful.readthedocs.io/en/latest/index.html

APIs are exposed through a configurable port (7070) and accessible locally at: http://127.0.0.1:7070/api/iot/

The `requirements.txt` file contains the required dependencies to run the project.
If you are using a virtual environment, you can install the dependencies by running:

```bash
pip install -r requirements.txt
```
or in case of Python 3.7+:

```bash
pip3 install -r requirements.txt
```

Otherwise in PyCharms, you can install the dependencies by opening the `requirements.txt` 
file and clicking on the "Install requirements" popup and link or manually going to the package manager.

## Modeled REST Resources

- **/location**
  - _GET_: Returns the list of available locations
  - _POST_: Handles the creation of a new location

- **/location/<location_id>**
  - _GET_: Returns the target location with the specified `location_id`
  - _PUT_: Updates the target location with the specified `location_id`
  - _DELETE_: Deletes the target location with the specified `location_id`

- **/location/<location_id>/device**
  - _GET_: Returns the list of devices for the specified `location_id`
  - _POST_: Creates a new device for the specified `location_id`

- **/location/<location_id>/device/<device_id>**
  - _GET_: Returns the target device with the specified `device_id` associated with the specified `location_id`
  - _PUT_: Updates the target device with the specified `device_id` associated with the specified `location_id`
  - _DELETE_: Deletes the target device with the specified `device_id` associated with the specified `location_id`

A string like `<location_id>` or `<device_id>` is a placeholder for the actual location or device identifier.
In the current implementation device's data (e.g., temperature values or actuator status) are not handled and they are out of the scope of the demo inventory.

## Project Structure

The project is structured as follows:

- **Server Application**:    
  - _api_server.py_: The main entry point of the project. It contains the Flask application and the API resources.
- **Resources**: Contains the API resources for the locations and devices. Detailed in the following files:
  - _locations_resource.py_: Contains the LocationsResource class that handles the list of devices resource.
  - _location_resource.py_: Contains the LocationResource class that handles the device resources.
  - _devices_resource.py_: Contains the DevicesResource class that handles the list of devices resource.
  - _device_resource.py_: Contains the DeviceResource class that handles the device resources.
- **Models**: Contains the data models for the locations and devices. Detailed in the following files:
  - _location_model.py_: Contains the Location class that represents a location.
  - _device_model.py_: Contains the Device class that represents a device.
- **DTO**: Contains the Data Transfer Objects (DTOs) for the locations and devices. Detailed in the following files:
  - _device_creation_request.py_: Contains the DeviceCreationRequest class that represents the request to create a device.
  - _device_update_request.py_: Contains the DeviceUpdateRequest class that represents the request to update a device. 
  - _location_creation_request.py_: Contains the LocationCreationRequest class that represents the request to create a location. 
  - _location_entity_response.py_: Contains the LocationEntityResponse class that represents the response of a location entity. 
  - _location_update_request.py_: Contains the LocationUpdateRequest class that represents the request to update a location.
- **Persistence**: Contains the data access layer for the locations and devices. Detailed in the following file:
  - _data_manager.py_: Contains the DataManager class that handles the data access layer for the locations and devices.
- **Clients**: Contains the client to interact with the API. Detailed in the following file:
  - _create_and_get_location.py_: Implements the client to create a location and get the list of locations through the implemented API.
  - _create_location.py_: Implements the client to create a location through the implemented API.
  - _delete_location.py_: Implements the client to delete a location through the implemented API.
  - _get_location_list.py_: Implements the client to get the list of locations through the implemented API.
  - _get_single_location.py_: Implements the client to get a single location through the implemented API.
  - _update_location.py_: Implements the client to update a location through the implemented API.

## Running the Project

To run the project, you can execute the `api_server.py` file.
The server will start and expose the API resources through the configured port by default (7070).

## Postman Collection

In the `postman` folder, you can find a Postman collection that contains the requests to interact with the implemented API.
You can import the collection into Postman and run the requests to interact with the API.
  