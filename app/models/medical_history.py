from app import db
from app.id_gen import generate_id

class MedicalHistory:
    def __init__(
        self,
        patient_id,
        visit_date,
        diagnosis,
        treatment_type,
        treatment_description,
        treatment_duration,
        note=None,
    ):
        # self.id = generate_id()
        self.patient_id = patient_id
        self.visit_date = visit_date
        self.diagnosis = diagnosis
        self.treatment = [{treatment_type: treatment_description or ""}] if treatment_type else []
        self.treatment_duration = treatment_duration or ""
        self.note = note if note is not None else ""

    def save(self):
        db.medical_histories.insert_one(self.__dict__)
        
    
    def to_json(self):
        return {
            "patient_id": self.patient_id,
            "visit_date": self.visit_date,
            "diagnosis": self.diagnosis,
            "treatment": self.treatment,
            "treatment_duration": self.treatment_duration,
            "note": self.note            
        }
        

    @staticmethod
    def get_all():
        return list(db.medical_histories.find())

    @staticmethod
    def get_one_by_patient(patient_id):
        return db.medical_histories.find_one({"_id": patient_id})

    @staticmethod
    def get_by_patient_id(patient_id):
        return list(db.medical_histories.find({"_id": patient_id}))

    @staticmethod
    def delete(patient_id):
        db.medical_histories.delete_one({"_id": patient_id})
    
