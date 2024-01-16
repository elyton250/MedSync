#!/usr/bin/python3
from sqlalchemy import Integer, Column, String, MetaData, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
from .patient_info import Patient
from datetime import datetime

mymetadata = MetaData()

Base = declarative_base(metadata=mymetadata)

class Vaccination(Base):
    __tablename__ = 'vaccination'
    vaccine_id = Column(Integer, primary_key=True)
    vaccine_name = Column(String(255))
    vaccinated_pathogen = Column(String(255))
    time_taken = Column(DateTime, default=datetime.utcnow)

    patient_id = Column(Integer, ForeignKey(Patient.id))
Base.metadata.create_all(engine)
