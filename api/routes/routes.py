from flask import Blueprint
from api.routes.exampleRoute import example_route_bp

bp = Blueprint('api', __name__, url_prefix='/api')

bp.register_blueprint(example_route_bp, url_prefix='/example_resource')