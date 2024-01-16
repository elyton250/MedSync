#!/usr/bin/python3
"""this module creates the table if it doesnot exist"""
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patient_information'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    f_name = Column(String(255))
    l_name = Column(String(255))
    country_origin = Column(String(255))
    national_id = Column(String(255))
    birthdate = Column(Date)
    gender = Column(String(45))
    blood_group = Column(String(2))
    phone_number = Column(String(25))
    email = Column(String(255))
    allergies = Column(String(255))

class Address(Base):
    __tablename__ = 'address'
    address_id = Column(Integer, primary_key=True, nullable=False, unique=True)
    patient_id = Column(Integer, ForeignKey(Patient.id))
    country_residence = Column(String(255))
    province = Column(String(255))
    district = Column(String(255))
    sector = Column(String(255))
    cell = Column(String(255))
    village = Column(String(255))

class Medication(Base):
    __tablename__ = 'medication'
    patient_id = Column(Integer, ForeignKey(Patient.id))
    medication_id = Column(Integer, primary_key=True, autoincrement=True)
    medication_name = Column(String(255))
    dosage = Column(String(255))
    frequency = Column(String(255))
    route = Column(String(45))

class Vaccination(Base):
    __tablename__ = 'vaccination'
    patient_id = Column(Integer, ForeignKey(Patient.id))
    vaccine_id = Column(Integer, primary_key=True)
    vaccine_name = Column(String(255))
    vaccinated_pathogen = Column(String(255))

def create_database():
    """this function creates tables if they are not there"""
    engine = create_engine("sqlite:///Medsync.db")
    Base.metadata.create_all(engine, checkfirst=True)
