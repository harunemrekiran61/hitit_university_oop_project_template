# app/modules/module_1/implementations.py
from app.modules.module_1.base import BaseClass1

class Base1SubClass1(BaseClass1):
    def method1(self):
        print(f"Sinif Attribute: {self.base1Attribute}")

class Base1SubClass2(BaseClass1):
    def method1(self):
        print(f"Sinif Attribute: {self.base1Attribute}")