# app/modules/patient/implementations.py
from .base import PatientBase

class PrintablePatient(PatientBase):
    """
    PatientBase için örnek implementasyon
    (abstract class test/demo amaçlı)
    """

    def get_priority(self) -> int:
        return 99

    def describe(self) -> str:
        return (
            f"[TEST PATIENT] "
            f"ID: {self.patient_id}, "
            f"Ad: {self.name}, "
            f"Yaş: {self.age}, "
            f"Durum: {self.status}"
        )