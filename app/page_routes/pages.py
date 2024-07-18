from app.models.patient import Patient
from flask import Blueprint, jsonify, render_template


pages = Blueprint('pages', __name__)


@pages.route('/pages')
def landing_page():
    """ Texting API. """
    return jsonify({"Response": "OK to Pages"})


@pages.route('/dashboard', strict_slashes=False)
def dashboard_doctor():
    """ get all patients"""
    return render_template('doctor/dashboard-doctor.html')


@pages.route('/all_patients', strict_slashes=False)
def all_patients():
    """ get all patients"""
    patients = Patient.get_all()
    print(patients)
    return render_template('doctor/all-patients.html', patients=patients)


@pages.route('/patient_view/<patient_id>', strict_slashes=False)
def patient_view(patient_id):
    """ get all patients"""
    patient = Patient.get_one_by_id(patient_id)
    return render_template('doctor/patient-view.html', patient=patient)