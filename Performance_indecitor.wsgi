import sys
import os
from your_flask_app import app

# Set the path to your application directory
sys.path.insert(0, 'app.py')

# Define the WSGI application callable
application = app