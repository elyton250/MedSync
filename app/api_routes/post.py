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

@post_routes.route('/patients/<patient_id>/medical_histories', methods=['POST'])
def add_medical_history(patient_id):
    """ add medical history"""
    patient = Patient.get_one_by_id(patient_id)
    if not patient:
        return jsonify({"message": "patient not found"}), 404

    data = {
        "patient_id": request.form.get("patient_id"),
        "visit_date": request.form.get("visit_date"),
        "diagnosis": request.form.get("diagnosis"),
        "treatment_type": request.form.get("treatment_type"),
        "treatment_description": request.form.get("treatment_description"),
        "note": request.form.get("note"),
        "treatment_duration": request.form.get("treatment_duration")
    }
    
    Patient.add_medical_history(patient_id, data)
    
    return jsonify({"message": "medical history successfully added"}), 200
