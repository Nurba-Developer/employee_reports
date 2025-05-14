from abc import ABC, abstractmethod

class Report(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def generate(self):
        pass
