from flask import Blueprint, request, jsonify
from app.api_routes.get import api

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/signup/doctor', methods=['POST'], strict_slashes=False)
def signup_doc():
    """ add doctor"""
    from app.models.doctor import Doctor
    data = request.get_json()
    if Doctor.get_by_id_number(data.get('id_number')):
        return jsonify({"message": "doctor already exists"}), 400
    registerd_doctor = Doctor.create(data)
    return jsonify({"message": "doctor successfully added"}), 200