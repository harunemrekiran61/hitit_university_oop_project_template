# app/modules/module_2/base.py
from abc import ABC, abstractmethod
from datetime import datetime

class AppointmentBase(ABC):
    def __init__(self, appointment_id: int, patient_id: int, doctor_name: str, date_time: datetime, status: str = "scheduled"):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_name = doctor_name
        self.date_time = date_time
        self.status = status

    # Ücret hesaplamasi
    @abstractmethod
    def calculate_fee(self):
        pass

    # Detaylar
    @abstractmethod
    def get_details(self):
        pass

    # Modül adı
    @classmethod
    def get_module_name(cls):
        return "Randevu Modülü"

    # Tarih formatı
    @staticmethod
    def validate_datetime(dt):
        return isinstance(dt, datetime)
