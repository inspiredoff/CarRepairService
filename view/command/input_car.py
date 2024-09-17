from view.command.command import Command
from view.console_ui import ConsoleUI


class InputCar(Command):
    def __init__(self, console_ui: ConsoleUI):
        super().__init__(console_ui)
        self.description = "input car"

    async def execute(self):
        await self.console_ui.input_car()
