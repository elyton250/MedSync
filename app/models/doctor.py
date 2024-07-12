from app import db
from app.id_gen import generate_id
from app.models.patient import Patient
from app.models.department import Department
from app.hash_pass import encrypt_password

class Doctor:
    def __init__(
        self,
        id_number,
        first_name,
        last_name,
        specialty,
        contact_number,
        password,
        department = None
    ):
        self._id = generate_id(first_name,last_name,id_number)
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name
        self.specialty = specialty
        self.hash_password = encrypt_password(password)
        self.contact_number = contact_number
        self.department = Department.get_by_name(department) or specialty

    def save(self):
        db.doctors.insert_one(self.__dict__)

    @staticmethod
    def get_all():
        return list(db.doctors.find())

    @staticmethod
    def get_one(id):
        # print(f"getting doctor with id {id}")
        doctor = db.doctors.find_one({"_id": id})
        # print(f"found doctor {doctor}")
        return doctor
    
    @staticmethod
    def get_by_id_number(id_number):
        return db.doctors.find_one({"id_number": id_number})

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

    @staticmethod
    def create(data):
        """ create doctor"""
        doctor = Doctor(**data)
        doctor.save()
        return doctor
        
        
