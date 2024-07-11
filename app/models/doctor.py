from app import db
from app.id_gen import generate_id
from models.patient import Patient
from models.department import Department

class Doctor:
    def __init__(
        self,
        id_number,
        first_name,
        last_name,
        specialty,
        contact_number,
        department
    ):
        self._id = generate_id()
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name
        self.specialty = specialty
        self.contact_number = contact_number
        self.department = Department.get_by_name(department)

    def save(self):
        db.doctors.insert_one(self.__dict__)

    @staticmethod
    def get_all():
        return list(db.doctors.find())

    @staticmethod
    def get_one(id):
        return db.doctors.find_one({"id": id})

    @staticmethod
    def get_by_name(first_name, last_name):
        return db.doctors.find_one({"first_name": first_name, "last_name": last_name})

    @staticmethod
    def delete(id):
        db.doctors.delete_one({"id": id})
        
    @staticmethod
    def get_patient(id):
        patient = Patient.get_one(id)
        return patient
        
        
