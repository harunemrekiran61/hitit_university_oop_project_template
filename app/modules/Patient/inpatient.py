# app/modules/patient/inpatient.py
from .base import PatientBase


class Inpatient(PatientBase):
    """
    Yatan hasta sınıfı
    """

    _max_capacity = 10
    _current_inpatients = 0

    def __init__(
        self,
        patient_id: int,
        name: str,
        age: int,
        gender: str,
        room_number: int,
        status: str = "aktif"
    ):
        # kapasite kontrolü
        if Inpatient._current_inpatients >= Inpatient._max_capacity:
            raise ValueError("Yatan hasta kapasitesi dolu! Yeni hasta kabul edilemiyor.")

        super().__init__(patient_id, name, age, gender, status)

        self.room_number = room_number
        self._is_discharged = False  # aynı hasta iki kere düşürülmesin

        Inpatient._current_inpatients += 1

    # property
    @property
    def room_number(self):
        return self._room_number

    @room_number.setter
    def room_number(self, value):
        if value is None or value <= 0:
            raise ValueError("Oda numarası pozitif bir sayı olmalıdır.")
        self._room_number = value

    # abstract method override
    def get_priority(self) -> int:
        """Inpatient için orta öncelik"""
        return 2

    def describe(self) -> str:
        return (
            f"Inpatient Hasta → "
            f"İsim: {self.name}, "
            f"Yaş: {self.age}, "
            f"Cinsiyet: {self.gender}, "
            f"Oda: {self.room_number}, "
            f"Durum: {self.status}"
        )

    # class methods
    @classmethod
    def get_capacity_info(cls):
        return f"Aktif yatan hasta sayısı: {cls._current_inpatients}/{cls._max_capacity}"

    @classmethod
    def _decrease_capacity(cls):
        if cls._current_inpatients > 0:
            cls._current_inpatients -= 1

    # base davranışı override
    def update_status(self, new_status: str):
        """
        Hasta taburcu edilirse kapasite otomatik güncellenir
        """
        if new_status == "taburcu" and not self._is_discharged:
            Inpatient._decrease_capacity()
            self._is_discharged = True

        self._status = new_status

    # static method
    @staticmethod
    def patient_type() -> str:
        return "Inpatient"