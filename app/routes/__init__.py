from flask import Blueprint

# Create a Blueprint for API routes
api_bp = Blueprint('api', __name__)

# Import route files to register them
from .auth_routes import *  # Import all routes from auth_routes.py
from .shared_routes import *  # Import all routes from user_routes.py
from .main_routes import main_routes  # Import the main_routes Blueprint
from .admin_routes import * # Import all routes from admin_routes
from .tutor_routes import * # Import all routes from tutor_routes
from .student_routes import * # Import all routes from student_routes