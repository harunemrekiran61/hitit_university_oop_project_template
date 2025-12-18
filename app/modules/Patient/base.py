# app/modules/patient/base.py

from abc import ABC, abstractmethod
from datetime import datetime


class PatientBase(ABC):
    """
    Soyut Hasta Sınıfı
    Tüm hasta tipleri için ortak davranışları ve kuralları içerir.
    """

    # class attributes
    _hospital_name = "Hitit University Hospital"
    _valid_statuses = ["aktif", "acil", "stabil", "taburcu", "iptal"]

    def __init__(
        self,
        patient_id: int,
        name: str,
        age: int,
        gender: str,
        status: str = "aktif"
    ):
        self._patient_id = patient_id
        self.name = name                  
        self.age = age                   
        self._gender = gender
        self._status = None
        self._created_at = datetime.now()
        self._status_history: list[tuple[str, datetime]] = []

        self.update_status(status)

    # 

    @property
    def patient_id(self) -> int:
        return self._patient_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value or not value.strip():
            raise ValueError("İsim alanı boş bırakılamaz")
        self._name = self.normalize_name(value)

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int):
        if not self.validate_age(value):
            raise ValueError("Geçersiz yaş değeri")
        self._age = value

    @property
    def gender(self) -> str:
        return self._gender

    @property
    def status(self) -> str:
        return self._status

    @property
    def created_at(self) -> datetime:
        return self._created_at

    # 

    def update_status(self, new_status: str):
        """
        Hasta durumunu günceller ve geçmişe kaydeder
        """
        if new_status not in self._valid_statuses:
            raise ValueError(f"Geçersiz hasta durumu: {new_status}")

        self._status = new_status
        self._status_history.append((new_status, datetime.now()))

    def get_status_history(self):
        """
        Hasta durum geçmişini döndürür
        """
        return list(self._status_history)

    # 

    @abstractmethod
    def get_priority(self) -> int:
        """
        Hasta öncelik seviyesini döndürür
        """
        pass

    @abstractmethod
    def describe(self) -> str:
        """
        Hasta bilgisini açıklayan string döndürür
        """
        pass

    # 

    @classmethod
    def get_hospital_name(cls) -> str:
        return cls._hospital_name

    @classmethod
    def from_dict(cls, data: dict):
        """
        Dictionary üzerinden hasta oluşturur
        """
        return cls(
            patient_id=data["patient_id"],
            name=data["name"],
            age=data["age"],
            gender=data["gender"],
            status=data.get("status", "aktif"),
        )

    # 

    @staticmethod
    def validate_age(age: int) -> bool:
        return isinstance(age, int) and 0 <= age <= 120

    @staticmethod
    def normalize_name(name: str) -> str:
        return name.strip().title()

    # 

    def age_group(self) -> str:
        """
        Hastanın yaş grubunu döndürür
        """
        if self._age < 18:
            return "Çocuk"
        elif self._age < 65:
            return "Yetişkin"
        return "Yaşlı"

    def is_active(self) -> bool:
        return self._status in ("aktif", "acil", "stabil")

    # 

    def __eq__(self, other):
        if not isinstance(other, PatientBase):
            return False
        return self.patient_id == other.patient_id

    def __lt__(self, other):
        """
        Önceliğe göre karşılaştırma 
        """
        return self.get_priority() < other.get_priority()

    def __repr__(self):
        return (
            f"<{self.__class__.__name__} "
            f"id={self.patient_id}, "
            f"name={self.name}, "
            f"status={self.status}>"
        )