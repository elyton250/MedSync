from flask import Blueprint, request, jsonify
from app.models.patient import Patient

post_routes = Blueprint('post_routes', __name__)

@post_routes.route('/add_patient', methods=['POST'])
def add_patient():
    """ add patient"""
    data = request.get_json()
    if Patient.get_one(data.get('id_number')):
        return jsonify({"message": "patient already exists"}), 400
    Patient.create(data).__dict__
    
    return jsonify({"message": "patient successfully added"}), 200

@post_routes.route('/patients/<int:id_number>/medical_histories', methods=['POST'])
def add_medical_history(id_number):
    """ add medical history by patient's NID number"""
    data = request.get_json()
    Patient.add_medical_history(id_number, data)
    return jsonify({"message": "medical history successfully added"}), 200

@post_routes.route('/add_doctor', methods=['POST'], strict_slashes=False)
def add_doctor():
    """ add doctor"""
    from app.models.doctor import Doctor
    data = request.get_json()
    if Doctor.get_one(data.get('id')):
        return jsonify({"message": "doctor already exists"}), 400
    registerd_doctor = Doctor.create(data)
    return jsonify({"message": "doctor successfully added"}), 200
