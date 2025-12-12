# app/modules/module_2/implementations.py
from .base import AppointmentBase

class RoutineAppointment(AppointmentBase):
    def __init__(self, appointment_id, patient_id, doctor_name, date_time, room_number):
        super().__init__(appointment_id, patient_id, doctor_name, date_time)
        self.room_number = room_number

    def calculate_fee(self):
        return 300

    def get_details(self):
        return f"Dr. {self.doctor_name} ile {self.room_number} numaralı odada rutin randevu"
