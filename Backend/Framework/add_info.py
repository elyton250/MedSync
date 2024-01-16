#!/usr/bin/python3
"""this the part that retreives information and add it to the database"""
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
    create_database()

    db = "Medsync"

    url = f"sqlite:///{db}.db"

    engine = create_engine(url)

    Session = sessionmaker(bind=engine)
    session = Session()

    patient_data = {
        'f_name': input("Enter first name: "),
        'l_name': input("Enter last name: "),
        'country_origin': input("Enter country of origin: "),
        'national_id': input("Enter national ID: "),
        'gender': input("Enter gender: "),
        'phone_number': input("Enter phone number: "),
        'email': input("Enter email: "),
        'allergies': input("Enter allergies: ")
    }

    address_data = {
        'country_residence': input("Enter country of residence: "),
        'province': input("Enter province: "),
        'district': input("Enter district: "),
        'sector': input("Enter sector: "),
        'cell': input("Enter cell: "),
        'village': input("Enter village: ")
    }

    medication_data = {
        #'medication_id': input("Enter medication ID: "),
        'medication_name': input("Enter medication name: "),
        'dosage': (input("Enter dosage: ")),
        'frequency': (input("Enter frequency: ")),
        'route': input("Enter route: ")
    }

    vaccination_data = {
        #'vaccine_id': int(input("Enter vaccine ID: ")),
        'vaccine_name': input("Enter vaccine name: "),
        'vaccinated_pathogen': input("Enter vaccinated pathogen: ")
    }

    #print(f"I am adding this {patient_data}")

    patient = Patient(**patient_data)
    address = Address(**address_data)
    medication = Medication(**medication_data)
    vaccination = Vaccination(**vaccination_data)

    #for data in patient:
       # print(f"patient added \n ----------\n{data}")

    session.add_all([patient, address, medication, vaccination])
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()
