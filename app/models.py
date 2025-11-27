import reflex as rx
from datetime import datetime
from typing import Optional
from sqlmodel import Field, Relationship, Column, JSON, SQLModel


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    password: str
    name: str = ""
    phone: str = ""
    ambulance_id: str = ""
    vehicle_number: str = ""
    is_setup_complete: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    reports: list["PatientReport"] = Relationship(back_populates="user")


class PatientReport(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="reports")
    location: str = ""
    accident_type: str = "Road"
    accident_date: str = ""
    accident_time: str = ""
    patient_count: int = 1
    is_patient_speaking: bool = True
    patient_name: str = ""
    patient_age: str = ""
    patient_gender: str = "Male"
    patient_contact: str = ""
    patient_allergies: str = ""
    patient_history: str = ""
    est_patient_age: str = ""
    est_patient_gender: str = "Male"
    consciousness_level: str = "Alert"
    injuries: dict[str, str | int | bool] = Field(default={}, sa_column=Column(JSON))
    assessment: dict[str, str | int | bool] = Field(default={}, sa_column=Column(JSON))
    treatment: dict[str, str | int | bool] = Field(default={}, sa_column=Column(JSON))
    photos: list[str] = Field(default=[], sa_column=Column(JSON))
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)