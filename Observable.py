from abc import ABC, abstractmethod


class Observable(ABC):

    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify(self):
        for i in range(len(self.observers)):
            self.observers[i].update()
