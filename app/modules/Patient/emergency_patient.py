# app/modules/patient/emergency_patient.py

from app.modules.Patient.base import PatientBase
from datetime import datetime


class EmergencyPatient(PatientBase):
    """
    Acil Hasta Sınıfı
    - Hayati riski olan hastaları temsil eder
    - Öncelik seviyesi en yüksektir
    """

    def __init__(
        self,
        patient_id: int,
        name: str,
        age: int,
        gender: str,
        emergency_level: int,
        arrival_time: datetime | None = None,
        status: str = "acil"
    ):
        super().__init__(patient_id, name, age, gender, status)

        if emergency_level not in (1, 2, 3):
            raise ValueError("Acil seviye 1, 2 veya 3 olmalıdır")

        self._emergency_level = emergency_level
        self._arrival_time = arrival_time or datetime.now()

    # property
    @property
    def emergency_level(self):
        return self._emergency_level

    @property
    def arrival_time(self):
        return self._arrival_time

    # abstract method override
    def get_priority(self) -> int:
        """
        Acil hastalarda öncelik seviyesi:
        Seviye 1 → 100
        Seviye 2 → 80
        Seviye 3 → 60
        """
        priority_map = {
            1: 100,
            2: 80,
            3: 60
        }
        return priority_map[self._emergency_level]

    # abstract method override
    def describe(self) -> str:
        return (
            f"[ACİL HASTA] "
            f"ID: {self.patient_id}, "
            f"Ad: {self.name}, "
            f"Yaş: {self.age}, "
            f"Cinsiyet: {self.gender}, "
            f"Acil Seviye: {self._emergency_level}, "
            f"Geliş Zamanı: {self._arrival_time.strftime('%Y-%m-%d %H:%M')}"
        )

    # emergency-specific behavior
    def stabilize(self):
        """
        Hasta stabilize edildiğinde çağrılır
        """
        self.update_status("stabil")

    def escalate(self):
        """
        Hastanın durumu kötüleşirse acil seviyesi yükseltilir
        """
        if self._emergency_level > 1:
            self._emergency_level -= 1

    def __str__(self):
        return self.describe()