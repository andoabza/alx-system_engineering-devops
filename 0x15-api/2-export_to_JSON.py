#!/usr/bin/python3
"""
module that defines API interactions for State __objects
"""
from models import storage
from models.city import City
from api.v1.views import app_views
from flask import jsonify, abort, request


@app_views.route('/states/<state_id>/cities', strict_slashes=False, methods=["GET"])
def id_for_city(state_id):
    """
    defines the states/<state_id>/cities route
    Returns: state id or 404 Error if object not linked to State object
    """
    citi = storage.all("City").values()
    a_state = storage.get("State", state_id)
    if a_state:
        return jsonify(cities.to_dict() for cities in citi)
    return abort(404)


@app_views.route('/cities/<city_id>', strict_slashes=False, methods=['GET'])
def get_city(city_id):
    """
    defines the cities route
    Returns: list of all State objects
    """
    city = storage.get("City", city_id).values()
    if city:
        return jsonify(city.to_dict())



@app_views.route('/states/<state_id>', strict_slashes=False,
                 methods=['DELETE'])
def delete_state_id(state_id):
    """
    defines DELETE for state objects by id
    Returns: if successful 200 and an empty dictionary
             404 if state_id is not linked to any State obj
    """
    state = storage.get("State", state_id)
    if state:
        storage.delete(state)
        storage.save()
        return jsonify({}), 200
    return abort(404)


@app_views.route('/cities/', strict_slashes=False, methods=['POST'])
def create_state():
    """
    define how to create a new state objects
    Returns: 201 on successful creation
             400 "Not a JSON" if HTTP body request is not valid
             404 if state_id is not linked to any State object
    """
    try:
        city = request.get_json()

        if city.get("name") is None:
            return abort(400, 'Missing name')
    except:
        return abort(400, 'Not a JSON')

    new_city = City(**city)
    storage.new(new_city)
    storage.save()
    return jsonify(new_city.to_dict()), 201


@app_views.route('/cities/<city_id>', strict_slashes=False, methods=['PUT'])
def state_update(city_id):
    """
    defines how an Update to a city is made
    Returns: 200 and the state object if successful
             400 "Not a JSON" if HTTP body request is not valid
             404 if state_id is not linked to any State object
    """
    city_data = request.get_json()

    if not city_data:
        return abort(400, 'Not a JSON')

    city = storage.get("City", state_id)

    if not city:
        return abort(404)

    for key, value in city_data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(city, key, value)
    storage.save()

    return jsonify(city.to_dict()), 200


# """ a code that save content a json to afile"""
# import requests
# from sys import argv

# usr_id = argv[1]
# #with open('file.json', 'w', encoding='utf-8') as f:
# #   f.write(test)

# todo = requests.get("https://jsonplaceholder.typicode.com/todos/")
# todos = todo.json()[{usr_id}]
# print(todos.json())