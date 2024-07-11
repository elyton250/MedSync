from app.models.patient import Patient
from flask import Blueprint, jsonify


api = Blueprint('api', __name__)

@api.route('/')
def hello_world():
    """ Texting API. """
    return jsonify({"Response": "OK"})

@api.route('/patients')
def get_patients():
    """ get all patients"""
    from app.models.patient import Patient
    return Patient.get_all()

@api.route('/patients/<id_number>')
def get_patient(id_number):
    """ get patient by National identity card number"""
    from app.models.patient import Patient
    return Patient.get_one(id_number)

# @api.route('/patients/<string:first_name>/<string:last_name>')
# def get_patient_by_name(first_name, last_name):
#     from app.models.patient import Patient
#     return Patient.get_by_name(first_name, last_name)

@api.route('/patients/<int:id>/medical_histories')
def get_medical_histories_by_patient(id):
    from app.models.patient import Patient
    return Patient.get_medical_histories(id)

@api.route('/patients/<int:id>/delete')
def delete_patient(id):
    from app.models.patient import Patient
    return Patient.delete(id)

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