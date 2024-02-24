#!/usr/bin/python3
"""API endpoint for /api/v1/"""
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.engine.db_storage import classes


# Create a route /status that returns JSON
@app_views.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "OK"})


@app_views.route("/stats", methods=["GET"])
def stats():
    new_dict = {}

    for _, value in classes.items():
        count = storage.count(value)
        new_dict[value.__tablename__] = count
    return jsonify(new_dict)
