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


# @api.route('/patients/<id>', strict_slashes=False)
# def get_patient_by_id(id):
#     """ get patient by id"""
#     if not id:
#         return jsonify({"message": "id is required"}), 400
#     if isinstance(id, str):
#         return jsonify({"message": "id must be an integer"}), 400
#     from app.models.patient import Patient
#     return Patient.get_one_by_id(id)

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

# ********************** END PATIENTS *****************************

@api.route('/doctors')
def get_doctors():
    """ get all doctors in doctors collection"""
    from app.models.doctor import Doctor
    return Doctor.get_all()

@api.route('/doctors/<id>', methods=['GET'], strict_slashes=False)
def get_doctor(id):
    """ Get a doctor by user id"""
    from app.models.doctor import Doctor
    # print(isinstance(id, str))
    if not id:
        return jsonify({"message": "id is required"}), 400
    if Doctor.get_one(id) is None:
        return jsonify({"message": "doctor not found"}), 404
    return Doctor.get_one(id)

""" I commented this because doctors can have same names"""
# @api.route('/doctors/<string:first_name>/<string:last_name>')
# def get_doctor_by_name(first_name, last_name):
#     from app.models.doctor import Doctor
#     return Doctor.get_by_name(first_name, last_name)

# @api.route('/doctors/<int:id>/patients')
# def get_patients_by_doctor(id):
#     from app.models.doctor import Doctor
#     return Doctor.get_patient(id)

# @api.route('/doctors/<int:id>/update')
# def update_doctor(id):
#     from app.models.doctor import Doctor
#     return Doctor.update(id)

# @api.route('/doctors/<int:id>/create')
# def create_doctor(id):
#     from app.models.doctor import Doctor
#     return Doctor.create(id)

# ********************** END DOCTORS *****************************

@api.route('/billers')
def get_billers():
    """ get all billers in billers collection"""
    from app.models.biller import Biller
    return Biller.get_all()

@api.route('/billers/<id>', methods=['GET'], strict_slashes=False)
def get_biller(id):
    """ Get a biller by user id"""
    from app.models.biller import Biller
    # print(isinstance(id, str))
    if not id:
        return jsonify({"message": "id is required"}), 400
    if Biller.get_one(id) is None:
        return jsonify({"message": "biller not found"}), 404
    return Biller.get_one(id)


# ********************** END BILLERS *****************************


@api.route('/nurses')
def get_nurses():
    """ get all nurses in nurses collection"""
    from app.models.nurse import Nurse
    return Nurse.get_all()


@api.route('/nurses/<id>', methods=['GET'], strict_slashes=False)
def get_nurse(id):
    """ Get a nurse by user id"""
    from app.models.nurse import Nurse
    # print(isinstance(id, str))
    if not id:
        return jsonify({"message": "id is required"}), 400
    if Nurse.get_one(id) is None:
        return jsonify({"message": "nurse not found"}), 404
    return Nurse.get_one(id)


# ********************** END NURSES *****************************
