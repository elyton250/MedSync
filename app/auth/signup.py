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

@auth_routes.route('/signup/biller', methods=['POST'], strict_slashes=False)
def signup_biller():
    """ add biller"""
    from app.models.biller import Biller
    data = request.get_json()
    if Biller.get_by_id_number(data.get('id_number')):
        return jsonify({"message": "biller already exists"}), 400
    registerd_biller = Biller.create(data)
    return jsonify({"message": "biller successfully added"}), 200

@auth_routes.route('/signup/nurse', methods=['POST'], strict_slashes=False)
def signup_nurse():
    """ add nurse"""
    from app.models.nurse import Nurse
    data = request.get_json()
    if Nurse.get_by_id_number(data.get('id_number')):
        return jsonify({"message": "nurse already exists"}), 400
    registerd_nurse = Nurse.create(data)
    return jsonify({"message": "nurse successfully added"}), 200