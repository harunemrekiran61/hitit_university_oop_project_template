# app/modules/patient/repository.py
from typing import List
from .base import PatientBase

class PatientRepository:
    """
    Hasta verilerinin in-memory olarak yönetildiği repository sınıfı
    """

    def __init__(self):
        self._patients: List[PatientBase] = []

    def add(self, patient: PatientBase):
        """
        Yeni hasta ekler.
        Aynı ID ile hasta varsa eklemeye izin vermez.
        """
        if self.get_by_id(patient.patient_id):
            raise ValueError(f"Aynı ID'ye sahip hasta zaten mevcut: {patient.patient_id}")
        self._patients.append(patient)

    def remove(self, patient_id: int):
        """
        ID'ye göre hasta siler.
        Hasta yoksa hata fırlatır.
        """
        patient = self.get_by_id(patient_id)
        if not patient:
            raise ValueError(f"Silinecek hasta bulunamadı: {patient_id}")
        self._patients.remove(patient)

    def get_by_id(self, patient_id: int) -> PatientBase | None:
        """
        ID'ye göre hasta döndürür.
        """
        return next(
            (p for p in self._patients if p.patient_id == patient_id),
            None
        )

    def list_all(self) -> List[PatientBase]:
        """
        Tüm hastaları listeler (kopya liste döner).
        """
        return list(self._patients)

    def filter_by_status(self, status: str) -> List[PatientBase]:
        """
        Duruma göre hasta filtreler.
        """
        return [p for p in self._patients if p.status == status]

    def filter_by_type(self, patient_type: str) -> List[PatientBase]:
        """
        Hasta tipine göre filtreleme (Inpatient, Outpatient, EmergencyPatient)
        """
        return [
            p for p in self._patients
            if p.__class__.__name__.lower() == patient_type.lower()
        ]

    def count(self) -> int:
        """
        Toplam hasta sayısını döndürür.
        """
        return len(self._patients)