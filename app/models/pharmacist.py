from app import db
from app.id_gen import generate_id
from app.models.patient import Patient
from app.hash_pass import encrypt_password

class Pharmacist:
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
        db.pharmacists.insert_one(self.__dict__)

    @staticmethod
    def get_all():
        return list(db.pharmacists.find())

    @staticmethod
    def get_one(id):
        # print(f"getting pharmacist with id {id}")
        pharmacist = db.pharmacists.find_one({"_id": id})
        # print(f"found pharmacist {pharmacist}")
        return pharmacist 
    
    @staticmethod
    def get_by_id_number(id_number):
        return db.pharmacists.find_one({"id_number": id_number})

    @staticmethod
    def get_by_name(first_name, last_name):
        return db.pharmacists.find_one({"first_name": first_name, "last_name": last_name})

    @staticmethod
    def delete(id):
        db.pharmacists.delete_one({"_id": id})
        
    @staticmethod
    def get_patient(id):
        patient = Patient.get_one(id)
        return patient

    @staticmethod
    def create(data):
        """ create pharmacist"""
        pharmacist = Pharmacist(**data)
        pharmacist.save()
        return pharmacist
        
        
