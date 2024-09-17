from view.command.command import Command
from view.console_ui import ConsoleUI


class GetAllCar(Command):
    def __init__(self, console_ui: ConsoleUI):
        super().__init__(console_ui)
        self.description = "print all car"

    async def execute(self):
        await self.console_ui.get_all_car()
