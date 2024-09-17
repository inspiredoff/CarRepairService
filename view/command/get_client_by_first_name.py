from view.command.command import Command
from view.console_ui import ConsoleUI


class GetClientByFirstName(Command):
    def __init__(self, console_ui: ConsoleUI):
        super().__init__(console_ui)
        self.description = "choise client by first name"

    async def execute(self):
        await self.console_ui.get_client_by_first_name()
