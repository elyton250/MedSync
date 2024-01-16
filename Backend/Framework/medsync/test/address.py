#!/usr/bin/python3
from sqlalchemy import Integer, Column, String, ForeignKey, MetaData
from sqlalchemy.orm import declarative_base
from .patient_info import Patient

mymetadata = MetaData()

Base = declarative_base(metadata=mymetadata)

class Address(Base):
    __tablename__ = 'address'
    address_id = Column(Integer, primary_key=True, nullable=False, unique=True)
    patient_id = Column(Integer, ForeignKey(Patient.id))
    country_residence = Column(String(255))
    province = Column(String(255))
    district = Column(String(255))
    sector = Column(String(255))``
    cell = Column(String(255))
    village = Column(String(255))

Base.metadata.create_all(engine)
