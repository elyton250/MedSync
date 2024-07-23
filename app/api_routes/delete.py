from flask import Blueprint, jsonify

delete_routes = Blueprint('delete_routes', __name__)

@delete_routes.route('/patients/<id_number>/delete', methods=['DELETE'], strict_slashes=False)
def delete_patient(id_number):
    """ delete patient by National identity card number"""
    from app.models.patient import Patient
    patient_to_delete = Patient.get_one(id_number)
    if patient_to_delete is not None:
        Patient.delete(id_number)
        return jsonify({"message": "patient successfully deleted"}),200
    else:
        return jsonify({"message": "patient not found"}),404

@delete_routes.route('/doctors/<id>/delete', methods=['DELETE'], strict_slashes=False)
def delete_doctor(id):
    from app.models.doctor import Doctor
    if not id:
        return jsonify({"message": "id is required"}), 400
    if Doctor.get_one(id) is None:
        return jsonify({"message": "doctor not found"}), 404
    Doctor.delete(id)
    return jsonify({"message": "doctor successfully deleted"}), 200
    
@delete_routes.route('/billers/<id>/delete', methods=['DELETE'], strict_slashes=False)
def delete_biller(id):
    from app.models.biller import Biller
    if not id:
        return jsonify({"message": "id is required"}), 400
    if Biller.get_one(id) is None:
        return jsonify({"message": "biller not found"}), 404
    Biller.delete(id)
    return jsonify({"message": "biller successfully deleted"}), 200

@delete_routes.route('/nurses/<id>/delete', methods=['DELETE'], strict_slashes=False)
def delete_nurse(id):
    from app.models.nurse import Nurse
    if not id:
        return jsonify({"message": "id is required"}), 400
    if Nurse.get_one(id) is None:
        return jsonify({"message": "nurse not found"}), 404
    Nurse.delete(id)
    return jsonify({"message": "nurse successfully deleted"}), 200

@delete_routes.route('/pharmacists/<id>/delete', methods=['DELETE'], strict_slashes=False)
def delete_pharmacist(id):
    from app.models.pharmacist import Pharmacist
    if not id:
        return jsonify({"message": "id is required"}), 400
    if Pharmacist.get_one(id) is None:
        return jsonify({"message": "pharmacist not found"}), 404
    Pharmacist.delete(id)
    return jsonify({"message": "pharmacist successfully deleted"}), 200