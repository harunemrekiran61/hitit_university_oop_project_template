# app/modules/patient/demo.py

from app.modules.Patient.repository import PatientRepository
from app.modules.Patient.service import PatientService
from app.modules.Patient.emergency_patient import EmergencyPatient


def run_demo():
    repo = PatientRepository()
    service = PatientService(repo)

    patient1 = EmergencyPatient(
        patient_id=1,
        name="Asel",
        age=22,
        gender="Kadın",
        emergency_level=1
    )

    service.register_patient(patient1)
    service.update_patient_status(1, "stabil")

    for patient in service.list_patients():
        print(patient.describe())


if __name__ == "__main__":
    run_demo()