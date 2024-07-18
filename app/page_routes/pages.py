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

