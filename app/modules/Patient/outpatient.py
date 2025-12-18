# app/modules/patient/outpatient.py
from .base import PatientBase
from datetime import datetime


class Outpatient(PatientBase):
    """
    Ayaktan hasta sınıfı
    """

    def __init__(
        self,
        patient_id: int,
        name: str,
        age: int,
        gender: str,
        appointment_date: str | None = None,
        status: str = "aktif"
    ):
        super().__init__(patient_id, name, age, gender, status)
        self.appointment_date = appointment_date

    # property
    @property
    def appointment_date(self):
        return self._appointment_date

    @appointment_date.setter
    def appointment_date(self, value):
        if value is not None:
            try:
                datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                raise ValueError(
                    "Randevu tarihi 'YYYY-MM-DD' formatında olmalıdır."
                )
        self._appointment_date = value

    # abstract method override
    def get_priority(self) -> int:
        """Outpatient için düşük öncelik"""
        return 3

    def describe(self) -> str:
        return (
            f"Outpatient Hasta → "
            f"İsim: {self.name}, "
            f"Yaş: {self.age}, "
            f"Cinsiyet: {self.gender}, "
            f"Randevu Tarihi: {self.appointment_date}, "
            f"Durum: {self.status}"
        )

    # base davranışı override
    def update_status(self, new_status: str):
        """
        Ayaktan hasta iptal edilirse randevu otomatik silinir
        """
        if new_status == "iptal":
            self._appointment_date = None
        self._status = new_status

    # yardımcı davranış
    def has_appointment(self) -> bool:
        return self._appointment_date is not None

    # static method
    @staticmethod
    def patient_type() -> str:
        return "Outpatient"