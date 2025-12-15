# app/modules/patient/repository.py

from typing import List
from app.modules.Patient.base import PatientBase


class PatientRepository:
    def __init__(self):
        self._patients: List[PatientBase] = []

    def add(self, patient: PatientBase):
        self._patients.append(patient)

    def remove(self, patient_id: int):
        self._patients = [
            p for p in self._patients if p.patient_id != patient_id
        ]

    def get_by_id(self, patient_id: int) -> PatientBase | None:
        for patient in self._patients:
            if patient.patient_id == patient_id:
                return patient
        return None

    def list_all(self) -> List[PatientBase]:
        return self._patients

    def filter_by_status(self, status: str) -> List[PatientBase]:
        return [p for p in self._patients if p.status == status]