from app import db
from app.id_gen import generate_id
from medical_history import MedicalHistory

        
class Patient():
    def __init__(
        self,
        id_number,
        first_name,
        last_name,
        date_of_birth,
        gender,
        address,
        contact_number,
        medical_history = MedicalHistory.get_all(),
        ):
        self.id = generate_id()
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.address = address
        self.contact_number = contact_number
        self.medical_history = medical_history
        
    
    def save(self):
        db.patients.insert_one(self.__dict__)   
        
    @staticmethod
    def get_all():
        return list(db.patients.find())
    
    @staticmethod
    def get_one(id):
        return db.patients.find_one({"id": id})#
    
    @staticmethod
    def get_by_name(first_name, last_name):
        return db.patients.find_one(
            {"first_name":first_name},
            {"last_name":last_name}
            )
    
    @staticmethod
    def delete(id):
        db.patients.delete_one({"id": id})