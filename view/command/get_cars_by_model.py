from view.command.command import Command
from view.console_ui import ConsoleUI


class GetCarsByModel(Command):
    def __init__(self, console_ui: ConsoleUI):
        super().__init__(console_ui)
        self.description = "print Cars by model"

    async def execute(self):
        await self.console_ui.get_cars_by_model()
