from flask import Blueprint, request
from api.controller.exampleController import *

example_route_bp = Blueprint('example_controller', __name__)

@example_route_bp.route('/exampleGET', methods=['GET'])
def example_route():
    return example_controller()

@example_route_bp.route('/examplePOST', methods=['POST'])
def example_route_post():
    return example_controller_post(request)