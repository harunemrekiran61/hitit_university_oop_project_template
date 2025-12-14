from .base import PatientBase

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
        appointment_date: str = None,
        status: str = "aktif"
    ):
        super().__init__(patient_id, name, age, gender, status)
        self._appointment_date = appointment_date

    # property
    @property
    def appointment_date(self):
        return self._appointment_date

    @appointment_date.setter
    def appointment_date(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("Randevu tarihi string formatında olmalıdır.")
        self._appointment_date = value

    # abstract method override
    def get_priority(self) -> int:
        """Outpatient için düşük öncelik"""
        return 3

    def describe(self) -> str:
        return (
            f"Outpatient Hasta → İsim: {self.name}, Yaş: {self.age}, "
            f"Cinsiyet: {self.gender}, Randevu Tarihi: {self.appointment_date}, "
            f"Durum: {self.status}"
        )

    # static method
    @staticmethod
    def patient_type() -> str:
        return "Outpatient"