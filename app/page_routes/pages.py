from flask import Blueprint, jsonify, render_template, session, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from app.models.patient import Patient
from app.models.doctor import Doctor
from app.models.nurse import Nurse
from app.models.biller import Biller
from app.hash_pass import encrypt_password, check_password
from app.user_wrapper import UserWrapper
from app import login_manager

# Initialize Blueprint
pages = Blueprint('pages', __name__)
api = Blueprint('api', __name__)

# # Initialize LoginManager
# login_manager = LoginManager()
# login_manager.init_app(medsync)

@pages.route('/pages')
def landing_page():
    """ Testing API. """
    return jsonify({"Response": "OK to Pages"})

@pages.route('/login', strict_slashes=False)
def login():
    """ Login page """
    return render_template('auth.html')

@login_manager.user_loader
def load_user(user_id):
    """ Load user by id

    Args:
        user_id: id of user
    """
    role = session.get('role')
    if role == 'doctor':
        user = Doctor.get_one(user_id)
    elif role == 'nurse':
        user = Nurse.get_one(user_id)
    elif role == 'biller':
        user = Biller.get_one(user_id)
    else:
        return None

    return UserWrapper(user, role)

@pages.route('/auth', methods=['POST', 'GET'], strict_slashes=False)
def auth():
    if request.method == 'POST':
        _id = request.form['User Id']
        password = request.form['pswd']
        role = request.form['role']
        user = None

        print(_id, password, role)
        print("-------------")
        if role == 'doctor':
            user = Doctor.get_one(_id)
        elif role == 'nurse':
            user = Nurse.get_one(_id)
        elif role == 'biller':
            user = Biller.get_one(_id)

        print(user)
        print("-------------")
        if user and check_password(user['hash_password'], password):
            user_wrapper = UserWrapper(user, role)
            login_user(user_wrapper)
            session['role'] = role
            print("Login Successful")
            return redirect(url_for('pages.dashboard_doctor'))
        return redirect(url_for('pages.login'))
    return redirect(url_for('pages.login'))

@pages.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('role', None)
    return redirect(url_for('pages.login'))

@pages.route('/dashboard', strict_slashes=False)
@login_required
def dashboard_doctor():
    """ Doctor dashboard """
    return render_template('doctor/dashboard-doctor.html')

@pages.route('/all_patients', strict_slashes=False)
@login_required
def all_patients():
    """ Get all patients """
    patients = Patient.get_all()
    return render_template('doctor/all-patients.html', patients=patients)

@pages.route('/patient_view/<patient_id>', strict_slashes=False)
@login_required
def patient_view(patient_id):
    """ View a single patient """
    patient = Patient.get_one_by_id(patient_id)
    return render_template('doctor/patient-view.html', patient=patient)

@pages.route('/create_plan/<patient_id>', strict_slashes=False)
def create_plan(patient_id):
    """ get all patients"""
    patient = Patient.get_one_by_id(patient_id)
    return render_template('doctor/create-plan.html', patient=patient)

@pages.route('/patient_history/<patient_id>', strict_slashes=False)
def patient_history(patient_id):
    """ get all patients"""
    patient = Patient.get_one_by_id(patient_id)
    histories = Patient.get_medical_histories(patient_id)
    print('histories', histories)
    treatments = []
    treatments = [history.get('treatment') for history in histories]
    return render_template('doctor/medical-history.html', patient=patient, histories=histories, treatments=treatments)
