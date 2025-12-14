# app/modules/appointment/routineappointment.py

from datetime import datetime
from .base import AppointmentBase


class RoutineAppointment(AppointmentBase):

    def __init__(
        self,
        appointment_id: int,
        patient_id: int,
        doctor_name: str,
        date_time: datetime,
        room_number: int,
        duration_minutes: int = 30
    ):
        super().__init__(appointment_id, patient_id, doctor_name, date_time)
        self.room_number = room_number
        self.duration_minutes = duration_minutes

    def calculate_fee(self) -> int:
        base_fee = 300
        extra_fee = 50 if self.duration_minutes > 30 else 0.   # Süre artarsa ücret artar
        return base_fee + extra_fee

    def get_details(self) -> str:
        return (
            f"Rutin Randevu | Dr. {self.doctor_name} | "
            f"Oda: {self.room_number} | Süre: {self.duration_minutes} dk"
        )

    # Randevular için normal süre
    @classmethod
    def default_duration(cls):
        return 30
    
    # Randevu süresini uzat
    def extend_duration(self, extra_minutes: int):
        if extra_minutes > 0:
            self.duration_minutes += extra_minutes

    # Oda numarası geçerlimi diye kontrol
    @staticmethod
    def is_room_valid(room_number: int) -> bool:
        return isinstance(room_number, int) and room_number > 0























