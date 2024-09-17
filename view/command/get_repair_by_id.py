from view.command.command import Command
from view.console_ui import ConsoleUI


class GetRepairById(Command):
    def __init__(self, console_ui: ConsoleUI):
        super().__init__(console_ui)
        self.description = "print repair by id"

    async def execute(self):
        await self.console_ui.get_repair_by_id()
