# app/modules/appointment/demo.py

from .repository import AppointmentRepository
from .onlineappointment import OnlineAppointment


def run_demo():
    print("\n APPOINTMENT MODULE DEMO \n")

    repo = AppointmentRepository()

    appointment = OnlineAppointment(
        appointment_id=1,
        patient_id=1,
        doctor_name="Dr. Ali",
        date_time="2025-12-21 14:00",
        status="aktif",
        platform="Zoom"
    )

    repo.add(appointment)

    for a in repo.list_all():
        print(a.describe())