from abc import ABC, abstractmethod


class View(ABC):

    @abstractmethod
    def print_answer(self, text: str):
        pass

    @abstractmethod
    def start(self):
        pass
