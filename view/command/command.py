from abc import ABC
from abc import abstractmethod

from view.console_ui import ConsoleUI


class Command(ABC):
    description: str
    console_ui: ConsoleUI

    def __init__(self, console_ui: ConsoleUI):
        self.console_ui = console_ui

    def get_description(self):
        return self.description

    @abstractmethod
    def execute():
        pass
