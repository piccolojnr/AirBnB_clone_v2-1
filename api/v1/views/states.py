#!/usr/bin/python3
"""API endpoint for /api/v1/states"""
from flask import jsonify, abort, make_response, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route("/states", methods=["GET"], strict_slashes=False)
def get_states():
    """get all states"""
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states])


@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
def get_state(state_id):
    """get state"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route("/states/<state_id>", methods=["DELETE"], strict_slashes=False)
def delete_state(state_id):
    """delete state"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route("/states", methods=["POST"], strict_slashes=False)
def create_state():
    """create state"""
    if not request.is_json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    if "name" not in data:
        abort(400, description="Missing name")
    new_state = State(**data)
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
def update_state(state_id):
    """update state"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not request.is_json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    # Ignore keys: id, created_at, and updated_at
    for key, value in data.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(state, key, value)
    storage.save()
    return jsonify(state.to_dict()), 200
