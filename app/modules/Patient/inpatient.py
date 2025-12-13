from .base import PatientBase

class Inpatient(PatientBase):
    """
    Yatan hasta sınıfı 
    """

    # maksimum kapasite
    _max_capacity = 10
    _current_inpatients = 0

    def __init__(self, patient_id: int, name: str, age: int, gender: str, room_number: int = None, status="aktif"):
        
        # kapasite kontrolü
        if Inpatient._current_inpatients >= Inpatient._max_capacity:
            raise ValueError("Yatan hasta kapasitesi dolu! Yeni hasta kabul edilemiyor.")

        super().__init__(patient_id, name, age, gender, status)

        self._room_number = room_number  
        Inpatient._current_inpatients += 1 

    # property
    @property
    def room_number(self):
        return self._room_number

    @room_number.setter
    def room_number(self, value):
        if value is not None and value <= 0:
            raise ValueError("Oda numarası pozitif bir sayı olmalıdır.")
        self._room_number = value

    # abstract method override
    def get_priority(self) -> int:
        """Inpatient için orta öncelik"""
        return 2

    def describe(self) -> str:
        return (
            f"Inpatient Hasta → İsim: {self.name}, Yaş: {self.age}, "
            f"Cinsiyet: {self.gender}, Oda: {self.room_number}, Durum: {self.status}"
        )

    # class methods
    @classmethod
    def get_capacity_info(cls):
        return f"Aktif yatan hasta sayısı: {cls._current_inpatients}/{cls._max_capacity}"

    @classmethod
    def discharge_patient(cls):
        """Bir hasta taburcu edildiğinde toplam aktif hasta sayısını 1 azaltır"""
        if cls._current_inpatients > 0:
            cls._current_inpatients -= 1

    # static method
    @staticmethod
    def patient_type() -> str:
        return "Inpatient"