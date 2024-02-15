from abc import ABC, abstractmethod


class Observer(ABC):
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def update(self, *args):
        pass
