# app/modules/patient/service.py
from .repository import PatientRepository
from .base import PatientBase

class PatientService:
    """
    Hasta işlemlerine ait iş kurallarını yöneten servis katmanı
    """

    def __init__(self, repository: PatientRepository):
        self._repository = repository

    def register_patient(self, patient: PatientBase):
        """
        Yeni hasta kaydı oluşturur
        """
        if self._repository.get_by_id(patient.patient_id):
            raise ValueError("Bu ID ile kayıtlı hasta zaten var")
        self._repository.add(patient)

    def discharge_patient(self, patient_id: int):
        """
        Hastayı taburcu eder
        """
        patient = self._repository.get_by_id(patient_id)
        if not patient:
            raise ValueError("Hasta bulunamadı")

        patient.update_status("taburcu")

    def update_patient_status(self, patient_id: int, new_status: str):
        """
        Hastanın durumunu günceller
        """
        patient = self._repository.get_by_id(patient_id)
        if not patient:
            raise ValueError("Hasta bulunamadı")

        patient.update_status(new_status)

    def get_patient(self, patient_id: int) -> PatientBase:
        """
        ID'ye göre hasta getirir
        """
        patient = self._repository.get_by_id(patient_id)
        if not patient:
            raise ValueError("Hasta bulunamadı")
        return patient

    def list_patients(self):
        """
        Tüm hastaları listeler
        """
        return self._repository.list_all()

    def list_patients_by_status(self, status: str):
        """
        Duruma göre hasta listeler
        """
        return self._repository.filter_by_status(status)

    def list_patients_by_type(self, patient_type: str):
        """
        Hasta tipine göre listeleme
        (Inpatient, Outpatient, EmergencyPatient)
        """
        return self._repository.filter_by_type(patient_type)

    def total_patient_count(self) -> int:
        """
        Toplam hasta sayısını döndürür
        """
        return self._repository.count()