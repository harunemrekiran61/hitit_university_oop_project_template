# app/modules/appointment/repository.py

from datetime import datetime, date
from typing import List, Optional
from .base import AppointmentBase


class AppointmentRepository:

    def __init__(self):
        self._appointments: List[AppointmentBase] = []

    #  Randevu kaydetme
    def save(self, appointment: AppointmentBase) -> None:

        if self.find_by_id(appointment.appointment_id):
            raise ValueError("Bu ID'ye sahip bir randevu zaten var.")

        self._appointments.append(appointment)

    # Randevu ID geçerli mi
    @staticmethod
    def is_valid_id(appointment_id: int) -> bool:

        return isinstance(appointment_id, int) and appointment_id > 0

    # ID'ye göre arama
    def find_by_id(self, appointment_id: int) -> Optional[AppointmentBase]:

        for appointment in self._appointments:
            if appointment.appointment_id == appointment_id:
                return appointment
        return None

    # Tarihe göre filtreleme
    def filter_by_date(self, target_date: date) -> List[AppointmentBase]:

        return [
            appointment
            for appointment in self._appointments
            if appointment.date_time.date() == target_date
        ]

    # Doktara göre filtreleme
    def filter_by_doctor(self, doctor_name: str) -> List[AppointmentBase]:

        return [
            appointment
            for appointment in self._appointments
            if appointment.doctor_name == doctor_name
        ]
    
    # Tarih Çakışması Kontrolü
    def has_time_conflict(self, new_appointment: AppointmentBase) -> bool:

        for appointment in self._appointments:
            if (
                appointment.doctor_name == new_appointment.doctor_name
                and appointment.date_time == new_appointment.date_time
                and appointment.status != "cancelled"
            ):
                return True
        return False

    # Randevu Silme
    def delete(self, appointment_id: int) -> bool:

        appointment = self.find_by_id(appointment_id)
        if appointment:
            self._appointments.remove(appointment)
            return True
        return False
    
    # Tüm randevu verilerini silme
    def clear(self) -> None:

        self._appointments.clear()

    # Tüm randevuları gösterme
    def list_all(self) -> List[AppointmentBase]:

        return list(self._appointments)

    # Toplam randevu sayısını gösterme
    def count(self) -> int:

        return len(self._appointments)
    
    # Randevu güncelleme
    def update(self, appointment: AppointmentBase) -> None:

        existing = self.find_by_id(appointment.appointment_id)
        if not existing:
            raise ValueError("Güncellenecek randevu bulunamadı.")

        index = self._appointments.index(existing)
        self._appointments[index] = appointment

