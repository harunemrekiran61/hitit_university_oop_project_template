# app/modules/patient/demo.py
from .repository import PatientRepository
from .service import PatientService
from .emergency_patient import EmergencyPatient
from .inpatient import Inpatient
from .outpatient import Outpatient

def run_demo():
    print("HASTA YÖNETİM SİSTEMİ \n")

    repo = PatientRepository()
    service = PatientService(repo)

    # Acil hasta
    emergency_patient = EmergencyPatient(
        patient_id=1,
        name="Asel",
        age=22,
        gender="Kadın",
        emergency_level=1
    )

    # Yatan hasta
    inpatient = Inpatient(
        patient_id=2,
        name="Koray",
        age=25,
        gender="Erkek",
        room_number=101
    )

    # Ayaktan hasta
    outpatient = Outpatient(
        patient_id=3,
        name="Zeynep",
        age=30,
        gender="Kadın",
        appointment_date="2025-12-20"
    )

    # Kayıt işlemleri
    service.register_patient(emergency_patient)
    service.register_patient(inpatient)
    service.register_patient(outpatient)

    # Durum güncellemeleri
    service.update_patient_status(1, "stabil")
    service.update_patient_status(2, "taburcu")

    print("Tüm Hastalar:\n")
    for patient in service.list_patients():
        print(patient.describe())

    print("\n Toplam Hasta Sayısı:", service.total_patient_count())


if __name__ == "__main__":
    run_demo()