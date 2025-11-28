# app/modules/module_1/base.py
from abc import ABC, abstractmethod

class BaseClass1(ABC):
    def __init__(self, parameter: str):
        self.base1Attribute = parameter

    @abstractmethod
    def method1(self) -> None:
        # metot tanimi 2344445
        pass