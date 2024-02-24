#!/usr/bin/python3
"""API blueprint definition for endpoint /api/v1"""
from flask import Blueprint

# Create a Blueprint instance with url_prefix
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# Import routes (index.py is not checked for PEP8)
import api.v1.views.index
