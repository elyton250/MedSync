from flask import Blueprint, flash, jsonify, render_template, session, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from app.models.patient import Patient
from app.models.doctor import Doctor
from app.models.nurse import Nurse
from app.models.biller import Biller
from app.models.pharmacist import Pharmacist
from app.hash_pass import encrypt_password, check_password
from app.user_wrapper import UserWrapper
from app import login_manager
import requests
from app import db

# Initialize Blueprint
pages = Blueprint('pages', __name__)
api = Blueprint('api', __name__)

@pages.route('/', strict_slashes=False)
def landing_page():
    """ Landing page """
    return render_template('index.html')

# ***************** AUTHENTICATION ROUTES ******************

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
    elif role == 'pharmacist':
        user = Pharmacist.get_one(user_id)
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

        if role == 'doctor':
            user = Doctor.get_one(_id)
        elif role == 'nurse':
            user = Nurse.get_one(_id)
        elif role == 'biller':
            user = Biller.get_one(_id)
        elif role == 'pharmacist':
            user = Pharmacist.get_one(_id)

        if user and check_password(user['hash_password'], password):
            user_wrapper = UserWrapper(user, role)
            login_user(user_wrapper)
            session['role'] = role
            if role == 'doctor':
                return redirect(url_for('pages.dashboard_doctor'))
            elif role == 'nurse':
                return redirect(url_for('pages.dashboard_nurse'))
            elif role == 'biller':
                return redirect(url_for('pages.dashboard_biller'))
            elif role == 'pharmacist':
                return redirect(url_for('pages.dashboard_pharmacist'))
        return redirect(url_for('pages.login'))
    return redirect(url_for('pages.login'))

role_to_collection = {
    'doctor': Doctor,
    'nurse': Nurse,
    'pharmacist': Pharmacist,
    'biller': Biller
}

@pages.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup():
    if request.method == 'POST':
        role = request.form.get('role')
        if not role or role not in role_to_collection:
            flash('Invalid or missing role!', 'danger')
            return redirect(url_for('pages.signup'))

        data = {
            'id_number': request.form.get('number'),
            'first_name': request.form.get('firstName'),
            'last_name': request.form.get('lastName'),
            'contact_number': request.form.get('contactNumber'),
            'password': request.form.get('pswd')
        }

        if role == 'doctor':
            data['specialty'] = request.form.get('specialty')
            response = requests.post(
                'https://medsync-production.up.railway.app/signup/doctor', json=data)
        elif role == 'nurse':
            response = requests.post(
                'http://localhost:5000/signup/nurse', json=data)
        elif role == 'pharmacist':
            response = requests.post(
                'http://localhost:5000/signup/pharmacist', json=data)
        elif role == 'biller':
            response = requests.post(
                'http://localhost:5000/signup/biller', json=data)

        if response.status_code == 200:
            user_collection = role_to_collection[role]
            user = user_collection.get_by_id_number(data['id_number'])
            flash(f'Successfully created account! Use your code {user.get("_id")} to Login', 'success')
            return redirect(url_for('pages.login'))
        else:
            flash('Unable to create account!', 'danger')
            return redirect(url_for('pages.signup'))

    return render_template('auth.html')

@pages.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('role', None)
    return redirect(url_for('pages.landing_page'))

# ***************** DASHBOARD ROUTES ******************

@pages.route('/dashboard_doctor', strict_slashes=False)
@login_required
def dashboard_doctor():
    """ Doctor dashboard """
    return render_template('doctor/dashboard-doctor.html')

@pages.route('/dashboard_nurse', strict_slashes=False)
@login_required
def dashboard_nurse():
    """ Nurse dashboard """
    return render_template('nurse/dashboard-nurse.html')

@pages.route('/dashboard_biller', strict_slashes=False)
@login_required
def dashboard_biller():
    """ Biller dashboard """
    return render_template('biller/dashboard-biller.html')

@pages.route('/dashboard_pharmacist', strict_slashes=False)
@login_required
def dashboard_pharmacist():
    """ Pharmacist dashboard """
    return render_template('pharmacist/dashboard-pharmacist.html')

# ***************** PATIENT ROUTES ******************

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
@login_required
def create_plan(patient_id):
    """ get all patients"""
    patient = Patient.get_one_by_id(patient_id)
    return render_template('doctor/create-plan.html', patient=patient)

@pages.route('/patient_history/<patient_id>', strict_slashes=False)
@login_required
def patient_history(patient_id):
    """ get all patients"""
    patient = Patient.get_one_by_id(patient_id)
    histories = Patient.get_medical_histories(patient_id)
    treatments = [history.get('treatment') for history in histories]
    return render_template('doctor/medical-history.html', patient=patient, histories=histories, treatments=treatments)
