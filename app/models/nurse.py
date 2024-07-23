from app import db
from app.id_gen import generate_id
from app.models.patient import Patient
from app.hash_pass import encrypt_password

class Nurse:
    def __init__(
        self,
        id_number,
        first_name,
        last_name,
        contact_number,
        password,
    ):
        self._id = generate_id(first_name,last_name,id_number)
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name
        self.hash_password = encrypt_password(password)
        self.contact_number = contact_number

    def save(self):
        db.nurses.insert_one(self.__dict__)

    @staticmethod
    def get_all():
        return list(db.nurses.find())

    @staticmethod
    def get_one(id):
        # print(f"getting nurse with id {id}")
        nurse = db.nurses.find_one({"_id": id})
        # print(f"found nurse {nurse}")
        return nurse
    
    @staticmethod
    def get_by_id_number(id_number):
        return db.nurses.find_one({"id_number": id_number})

    @staticmethod
    def get_by_name(first_name, last_name):
        return db.nurses.find_one({"first_name": first_name, "last_name": last_name})

    @staticmethod
    def delete(id):
        db.nurses.delete_one({"_id": id})
        
    @staticmethod
    def get_patient(id):
        patient = Patient.get_one(id)
        return patient

    @staticmethod
    def create(data):
        """ create doctor"""
        nurse = Nurse(**data)
        nurse.save()
        return nurse
        
        
