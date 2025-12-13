# app/modules/patient/base.py
from abc import ABC, abstractmethod

class PatientBase(ABC):
    """
    Soyut Hasta Sınıfı
    """
    
    # class attribute
    _hospital_name = "Hitit University Hospital"  

    def __init__(self, patient_id: int, name: str, age: int, gender: str, status: str = "aktif"):
        self._patient_id = patient_id
        self._name = name
        self._age = age
        self._gender = gender
        self._status = status

   # property
    @property
    def patient_id(self):
        return self._patient_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("İsim alanı boş bırakılamaz")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not self.validate_age(value):
            raise ValueError("Geçersiz yaş değeri")
        self._age = value

    @property
    def gender(self):
        return self._gender

    @property
    def status(self):
        return self._status

    def update_status(self, new_status: str):
        """Nesne metodu"""
        self._status = new_status

    # abstract class
    @abstractmethod
    def get_priority(self) -> int:
        pass

    @abstractmethod
    def describe(self) -> str:
        pass

    # class method
    @classmethod
    def get_hospital_name(cls):
        return cls._hospital_name

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            patient_id=data["patient_id"],
            name=data["name"],
            age=data["age"],
            gender=data["gender"],
            status=data.get("status", "active"),
        )

    # static method
    @staticmethod
    def validate_age(age: int) -> bool:
        return isinstance(age, int) and age >= 0

    @staticmethod
    def normalize_name(name: str) -> str:
        return name.strip().title()