from view.command.command import Command
from view.console_ui import ConsoleUI


class GetAllClient(Command):
    def __init__(self, console_ui: ConsoleUI):
        super().__init__(console_ui)
        self.description = "input all Client"

    async def execute(self):
        await self.console_ui.get_all_client()
