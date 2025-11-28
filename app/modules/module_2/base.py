# app/modules/module_2/base.py
from abc import ABC, abstractmethod

class BaseClass2(ABC):
    def __init__(self, parameter: str):
        self.base2Attribute = parameter

    @abstractmethod
    def method2(self) -> None:
        # model tanimiii
        pass