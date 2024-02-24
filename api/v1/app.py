#!/usr/bin/python3
"""api main file
"""
from flask import Flask
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)

# Import routes from app_views
app.register_blueprint(app_views, url_prefix="/api/v1")


# Teardown app context to close storage
@app.teardown_appcontext
def teardown_appcontext(error):
    storage.close()


if __name__ == "__main__":
    # Run the Flask server
    host = os.environ.get("HBNB_API_HOST", "0.0.0.0")
    port = int(os.environ.get("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
