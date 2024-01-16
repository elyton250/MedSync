#!/usr/bin/python3
"""this the part that retreives alll the info from the database"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from medsync.datacreation import Patient, Address, Vaccination, Medication, create_database


if __name__ == "__main__":
    """
    these will be used when deployed on mysqlserver
    username = "admin1"
    password = "  "
    host = "127.0.0.1"
    port = "3306"
    """
    db = "Medsync"

    url = f"sqlite:///{db}.db"

    engine = create_engine(url)
    
    Session = sessionmaker(bind=engine)
    session1 = Session()

    information = (
        session1.query(Patient, Medication, Vaccination)
        .join(Medication, Patient.id == Medication.patient_id)
        .join(Vaccination, Patient.id == Vaccination.patient_id)
        .all()
    )
    if information:
        print("We found this\n------------------\n")
    for patient, medication, vaccination in information:
        print(f"Patient ID: {patient.id} | Patient name: {patient.f_name} {patient.l_name} | Medication: {medication.medication_name} | Dosage: {medication.dosage} | Vaccination: {vaccination.vaccine_name}")
    print("Thank you for using Medsync")

    session1.close()
