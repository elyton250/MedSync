from flask import Blueprint, jsonify

delete_routes = Blueprint('delete_routes', __name__)

@delete_routes.route('/patients/<int:id_number>/delete', methods=['DELETE'], strict_slashes=False)
def delete_patient(id_number):
    """ delete patient by National identity card number"""
    from app.models.patient import Patient
    if Patient.get_one(id_number):
        Patient.delete(id_number)
    # elif not Patient.get_one(id_number):
    #     return jsonify({"message": "patient not found"}), 404
    return jsonify({"message": "patient successfully deleted"}),200