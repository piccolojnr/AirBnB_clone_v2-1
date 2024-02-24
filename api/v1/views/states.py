#!/usr/bin/python3
"""API endpoint for /api/v1/states"""
from flask import jsonify, abort, make_response, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route("/states", methods=["GET"], strict_slashes=False)
def states():
    """retrieves all states objs"""
    states_list = storage.all(State)
    return jsonify([obj.to_dict() for obj in states_list.values()])


@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
def state(state_id):
    """retrieves state with id"""
    s_state = storage.get(State, state_id)
    if not s_state:
        abort(404)
    return jsonify(s_state.to_dict())


@app_views.route("/states/<state_id>", methods=["DELETE"], strict_slashes=False)
def delete_state(state_id):
    """delete a state obj"""
    s_state = storage.get(State, state_id)
    if not s_state:
        abort(404)

    storage.delete(s_state)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route("/states", methods=["POST"], strict_slashes=False)
def create_state():
    """creates a state obj"""
    new_state = request.get_json()
    if not new_state:
        abort(400, "Not a JSON")
    if "name" not in new_state:
        abort(400, "Missing name")
    state = State(**new_state)
    storage.new(state)
    storage.save()
    return make_response(jsonify(state.to_dict()), 201)


@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
def update_state(state_id):
    """update a state obj"""
    s_state = storage.get(State, state_id)
    if not s_state:
        abort(404)
    new_state = request.get_json()
    if not new_state:
        abort(400, "Not a JSON")

    for k, v in new_state.items():
        if k != "id" and k != "created_at" and k != "updated_at":
            setattr(s_state, k, v)

    storage.save()
    return make_response(jsonify(s_state.to_dict()), 200)
