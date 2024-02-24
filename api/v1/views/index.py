#!/usr/bin/python3
"""API endpoint for /api/v1/"""
from flask import jsonify
from api.v1.views import app_views


# Create a route /status that returns JSON
@app_views.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "OK"})
