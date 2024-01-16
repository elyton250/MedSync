#!/usr/bin/python3
from sqlalchemy import Integer, Column, String, Date, MetaData
from sqlalchemy.orm import declarative_base

mymetadata = MetaData()

Base = declarative_base(metadata=mymetadata)

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
Base.metadata.create_all(engine)