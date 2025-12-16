# app/modules/patient/service.py

from app.modules.Patient.repository import PatientRepository
from app.modules.Patient.base import PatientBase


class PatientService:
    def __init__(self, repository: PatientRepository):
        self._repository = repository

    def register_patient(self, patient: PatientBase):
        if self._repository.get_by_id(patient.patient_id):
            raise ValueError("Bu ID ile kayıtlı hasta zaten var")
        self._repository.add(patient)

    def discharge_patient(self, patient_id: int):
        patient = self._repository.get_by_id(patient_id)
        if not patient:
            raise ValueError("Hasta bulunamadı")
        patient.update_status("taburcu")

    def update_patient_status(self, patient_id: int, new_status: str):
        patient = self._repository.get_by_id(patient_id)
        if not patient:
            raise ValueError("Hasta bulunamadı")
        patient.update_status(new_status)

    def list_patients(self):
        return self._repository.list_all()