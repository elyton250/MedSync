from app import db
from app.id_gen import generate_id

class MedicalHistory:
    def __init__(
        self,
        patient_id,
        visit_date,
        diagnosis,
        treatment,
        notes=None,
    ):
        self.id = generate_id()
        self.patient_id = patient_id
        self.visit_date = visit_date
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.notes = notes if notes is not None else ""

    def save(self):
        db.medical_histories.insert_one(self.__dict__)

    @staticmethod
    def get_all():
        return list(db.medical_histories.find())

    @staticmethod
    def get_one(id):
        return db.medical_histories.find_one({"id": id})

    @staticmethod
    def get_by_patient_id(patient_id):
        return list(db.medical_histories.find({"patient_id": patient_id}))

    @staticmethod
    def delete(id):
        db.medical_histories.delete_one({"id": id})
