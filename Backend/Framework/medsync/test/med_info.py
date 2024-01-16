#!/usr/bin/python3
from sqlalchemy import Integer, Column, String, MetaData, Date, ForeignKey
from sqlalchemy.orm import declarative_base
from .patient_info import Patient

mymetadata = MetaData()

Base = declarative_base(metadata=mymetadata)

class Medication(Base):
    __tablename__ = 'medication'
    medication_id = Column(String(20), primary_key=True)
    medication_name = Column(String(255))
    #TO DO: turn dose and frequency to ints
    dosage = Column(String(200))
    frequency = Column(String(200))
    route = Column(String(45))
    start_date = Column(Date)
    end_date = Column(Date)
    patient_id = Column(Integer, ForeignKey(Patient.id))
Base.metadata.create_all(engine)