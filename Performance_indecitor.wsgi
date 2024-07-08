import sys
import os
from app import app

# Set the path to your application directory
sys.path.insert(0, 'app')

# Define the WSGI application callable
application = app