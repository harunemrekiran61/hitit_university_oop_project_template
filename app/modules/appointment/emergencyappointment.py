# app/modules/appointment/emergencyappointment.py

from datetime import datetime, timedelta
from .base import AppointmentBase


class EmergencyAppointment(AppointmentBase):

    EMERGENCY_BASE_FEE = 750
    AMBULANCE_FEE = 400

    def __init__(
        self,
        appointment_id: int,
        patient_id: int,
        doctor_name: str,
        date_time: datetime,
        emergency_level: int,
        ambulance_used: bool = False,
        triage_notes: str = ""
    ):
        super().__init__(appointment_id, patient_id, doctor_name, date_time)
        self.emergency_level = emergency_level      # 1–5 arası aciliyet seviyesi
        self.ambulance_used = ambulance_used
        self.triage_notes = triage_notes
        self.priority = self._calculate_priority()

    def calculate_fee(self) -> int:
        fee = self.EMERGENCY_BASE_FEE

        if self.emergency_level >= 4:
            fee += 300

        if self.ambulance_used:
            fee += self.AMBULANCE_FEE

        return fee

    def get_details(self) -> str:
        return (
            f"ACİL RANDEVU | Dr. {self.doctor_name} | "
            f"Seviye: {self.emergency_level} | "
            f"Ambulans: {'Evet' if self.ambulance_used else 'Hayır'}"
        )
    
    # Normal aciliyet seviyesi
    @classmethod
    def default_emergency_level(cls) -> int:
        return 3

    # Aciliyet seviyesini arttır
    def escalate_emergency(self):
        if self.emergency_level < 5:
            self.emergency_level += 1
            self.priority = self._calculate_priority()

    # Aciliyet seviyesi geçerli mi
    @staticmethod
    def is_valid_emergency_level(level: int) -> bool:
        return isinstance(level, int) and 1 <= level <= 5

    # Aciliyete göre öncelik hesapla (private)
    def _calculate_priority(self) -> int:
        return self.emergency_level * 10
    
    # Ambulans gerekli mi
    @staticmethod
    def is_ambulance_required(level: int) -> bool:
        return level >= 4
    
    # Randevu erteleme
    def delay_appointment(self, minutes: int):
        if minutes > 0:
            self.date_time += timedelta(minutes=minutes)


