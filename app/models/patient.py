from app import db
from app.id_gen import generate_id
from app.models.medical_history import MedicalHistory
from bson.objectid import ObjectId

class Patient:
    def __init__(
        self,
        id_number,
        first_name,
        last_name,
        date_of_birth,
        gender,
        address,
        contact_number,
        medical_history=None
    ):
        self._id = generate_id(first_name, last_name, id_number)
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.address = address
        self.contact_number = contact_number
        self.medical_history = medical_history if medical_history is not None else []
    
    def to_json(self):
        return {
            "id": self._id,
            "id_number": self.id_number,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "address": self.address,
            "contact_number": self.contact_number,
            "medical_history": self.medical_history
        }

    def save(self):
        """ save patient"""
        db.patients.insert_one(self.__dict__)

    @staticmethod
    def get_all():
        """ get all patients"""
        return list(db.patients.find())

    @staticmethod
    def get_one(id_number):
        """
        get patient by National identity card number"""
        return db.patients.find_one({"id_number": id_number})

    # @staticmethod
    # def get_by_name(first_name, last_name):
    #     return db.patients.find_one({"first_name": first_name, "last_name": last_name})

    @staticmethod
    def get_medical_histories(id):
        return list(db.medical_histories.find({"patient_id": id}))

    @staticmethod
    def delete(id):
        db.patients.delete_one({"id": id})

    @staticmethod
    def update(id, data):
        db.patients.update_one({"id": id}, {"$set": data})
    
    @staticmethod
    def create(data):
        patient = Patient(**data)
        patient.save()
        return patient