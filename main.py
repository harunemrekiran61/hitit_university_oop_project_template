# main.py

import time
from datetime import datetime

from app.modules.Patient.demo import run_demo as run_patient_demo
from app.modules.appointment.demo import run_demo as run_appointment_demo


def clear_line():
    print("\r" + " " * 80 + "\r", end="")


def loading(text, duration=1.5):
    dots = ["", ".", "..", "..."]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(f"\r{text}{dots[i % 4]}", end="", flush=True)
        time.sleep(0.3)
        i += 1
    clear_line()


def divider(char="─", length=60):
    print(char * length)


def show_header():
    now = datetime.now().strftime("%d %B %Y  |  %H:%M:%S")
    divider()
    print("HITIT UNIVERSITY HOSPITAL".center(60))
    print("Hospital Information System".center(60))
    divider()
    print(f"System Time : {now}")
    divider()


def select_role():
    print("\nSelect User Role\n")
    print("  [1] Patient")
    print("  [2] Doctor / Medical Staff")
    print("  [3] Administrator")
    print("  [0] Exit")

    return input("\n> ").strip()


def patient_menu():
    print("\nPatient Panel")
    divider("-")
    print("  [1] Appointment System")
    print("  [0] Back")


def doctor_menu():
    print("\nDoctor / Staff Panel")
    divider("-")
    print("  [1] Patient Management")
    print("  [0] Back")


def admin_menu():
    print("\nAdministrator Panel")
    divider("-")
    print("  [1] Patient Management")
    print("  [2] Appointment Management")
    print("  [0] Back")


def main():
    while True:
        show_header()
        role = select_role()

        if role == "0":
            loading("Shutting down system")
            print("System closed. Stay healthy.")
            break

        while True:
            if role == "1":
                patient_menu()
                choice = input("\n> ").strip()
                if choice == "1":
                    loading("Opening Appointment Module")
                    run_appointment_demo()
                elif choice == "0":
                    break

            elif role == "2":
                doctor_menu()
                choice = input("\n> ").strip()
                if choice == "1":
                    loading("Opening Patient Management Module")
                    run_patient_demo()
                elif choice == "0":
                    break

            elif role == "3":
                admin_menu()
                choice = input("\n> ").strip()
                if choice == "1":
                    loading("Opening Patient Management Module")
                    run_patient_demo()
                elif choice == "2":
                    loading("Opening Appointment Management Module")
                    run_appointment_demo()
                elif choice == "0":
                    break

            else:
                print("\nInvalid selection.")
                time.sleep(1)

            input("\nPress ENTER to continue...")


if __name__ == "__main__":
    main()