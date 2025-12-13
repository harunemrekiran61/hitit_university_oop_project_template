from app.modules.Patient.implementations import (
    Base1SubClass1, Base1SubClass2
)

from app.modules.module_2.implementations import (
    Base2SubClass1, Base2SubClass2
)

def run_demo():
    print("=== PROJECT MENU ===")

    # Ogrenci 1 (Modul 1)
    base_1 = [
        Base1SubClass1("parametre1"),
        Base1SubClass2("parametre2")
    ]
    for n in base_1:
        n.method1()

    # Ogrenci 2 (Modul 2)
    base_2 = [
        Base2SubClass1("parametre3"),
        Base2SubClass2("parametre4")
    ]
    for n in base_2:
        n.method2()

if __name__ == "__main__":
    run_demo()