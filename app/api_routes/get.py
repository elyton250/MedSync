from app.models.patient import Patient
from flask import Blueprint, jsonify


api = Blueprint('api', __name__)

@api.route('/')
def hello_world():
    """ Texting API. """
    return jsonify({"Response": "OK"})

@api.route('/patients', strict_slashes=False)
def get_patients():
    """ get all patients"""
    from app.models.patient import Patient
    return Patient.get_all()

@api.route('/patients/<id_number>', strict_slashes=False)
def get_patient(id_number):
    """ get patient by National identity card number"""
    from app.models.patient import Patient
    return Patient.get_one(id_number)

""" I commented this because patients can have same names"""
# @api.route('/patients/<string:first_name>/<string:last_name>')
# def get_patient_by_name(first_name, last_name):
#     from app.models.patient import Patient
#     return Patient.get_by_name(first_name, last_name)

@api.route('/patients/<int:id_number>/medical_histories', strict_slashes=False)
def get_medical_histories_by_patient(id_number):
    """ get medical histories by patient's NID number"""
    from app.models.patient import Patient
    return Patient.get_medical_histories(id_number)

# @api.route('/patients/<int:id_number>/delete', methods=['DELETE'], strict_slashes=False)
# def delete_patient(id_number):
#     """ delete patient by National identity card number"""
#     from app.models.patient import Patient
#     if Patient.get_one(id_number):
#         Patient.delete(id_number)
#     return jsonify({"message": "patient successfully deleted"}),200

@api.route('/doctors')
def get_doctors():
    from app.models.doctor import Doctor
    return Doctor.get_all()

@api.route('/doctors/<int:id>')
def get_doctor(id):
    from app.models.doctor import Doctor
    return Doctor.get_one(id)

@api.route('/doctors/<string:first_name>/<string:last_name>')
def get_doctor_by_name(first_name, last_name):
    from app.models.doctor import Doctor
    return Doctor.get_by_name(first_name, last_name)

@api.route('/doctors/<int:id>/patients')
def get_patients_by_doctor(id):
    from app.models.doctor import Doctor
    return Doctor.get_patient(id)

@api.route('/doctors/<int:id>/delete')
def delete_doctor(id):
    from app.models.doctor import Doctor
    return Doctor.delete(id)

@api.route('/doctors/<int:id>/update')
def update_doctor(id):
    from app.models.doctor import Doctor
    return Doctor.update(id)

@api.route('/doctors/<int:id>/create')
def create_doctor(id):
    from app.models.doctor import Doctor
    return Doctor.create(id)