# app/modules/patient/emergency_patient.py

from .base import PatientBase
from datetime import datetime
from typing import Optional


class EmergencyPatient(PatientBase):
    """
    Acil Hasta Sınıfı
    """

    def __init__(
        self,
        patient_id: int,
        name: str,
        age: int,
        gender: str,
        emergency_level: int,
        arrival_time: Optional[datetime] = None,
        status: str = "acil"
    ):
        super().__init__(patient_id, name, age, gender, status)

        if emergency_level not in (1, 2, 3):
            raise ValueError("Acil seviye 1, 2 veya 3 olmalıdır")

        self._emergency_level = emergency_level
        self._arrival_time = arrival_time or datetime.now()

    # property
    @property
    def emergency_level(self) -> int:
        return self._emergency_level

    @property
    def arrival_time(self) -> datetime:
        return self._arrival_time

    # abstract method override
    def get_priority(self) -> int:
        """
        Acil hastalarda öncelik seviyesi:
        Seviye 1 → 100
        Seviye 2 → 80
        Seviye 3 → 60
        """
        return {
            1: 100,
            2: 80,
            3: 60
        }[self._emergency_level]

    def describe(self) -> str:
        return (
            f"[ACİL HASTA] "
            f"ID: {self.patient_id}, "
            f"Ad: {self.name}, "
            f"Yaş: {self.age}, "
            f"Cinsiyet: {self.gender}, "
            f"Acil Seviye: {self._emergency_level}, "
            f"Geliş Zamanı: {self._arrival_time.strftime('%Y-%m-%d %H:%M')}, "
            f"Durum: {self.status}"
        )

    # base davranışı override
    def update_status(self, new_status: str):
        """
        Acil hastalar için durum geçişleri kontrol altına alınır
        """
        valid_statuses = ["acil", "stabil", "taburcu"]

        if new_status not in valid_statuses:
            raise ValueError("Geçersiz acil hasta durumu")

        # Stabil olunca acil seviyesi otomatik düşürülür
        if new_status == "stabil" and self._emergency_level > 2:
            self._emergency_level = 2

        self._status = new_status

    # emergency-specific behavior
    def stabilize(self):
        """Hasta stabilize edildiğinde çağrılır"""
        self.update_status("stabil")

    def escalate(self):
        """Hastanın durumu kötüleşirse acil seviyesi yükseltilir"""
        if self._emergency_level > 1:
            self._emergency_level -= 1
            self._status = "acil"

    def __str__(self):
        return self.describe()