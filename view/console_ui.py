from presenter.presenter import Presenter
from view.view import View


class ConsoleUI(View):

    def __init__(self):
        self.work = True
        self.presenter = Presenter(self)

    async def print_answer(self, text: str):
        pass

    async def start(self):
        pass

    async def stop(self):
        self.work = False

    async def get_all_client(self):
        await self.presenter.get_all_client()

    async def get_client_by_id(self):
        id = int(input("input client id"))
        await self.presenter.get_client_by_id(id)

    async def get_client_by_first_name(self):
        name = input("input client first name")
        await self.presenter.get_client_by_first_name(name)

    async def get_client_by_family_name(self):
        name = input("input family name")
        await self.presenter.get_client_by_family_name(name)

    async def get_client_by_last_name(self):
        name = input("input last_name")
        await self.presenter.get_client_by_last_name(name)

    # Car
    async def get_all_car(self):
        await self.presenter.get_all_car()

    async def get_car_by_id(self, id: int):
        id = int(input("input car id"))
        await self.presenter.get_car_by_id(id)

    async def get_car_by_make(self):
        make = input("input make name")
        await self.presenter.get_car_by_make(make)

    async def get_car_by_model(self, model: str):
        model = input("input model name")
        await self.presenter.get_car_by_model(model)

    # Repair
    async def get_all_repair(self):
        await self.presenter.get_all_repair()

    async def get_repair_by_id(self):
        id = int(input("input repair id"))
        await self.presenter.get_repair_by_id(id)

    async def get_repair_by_car_id(self):
        id = int(input("input car id"))
        await self.presenter.get_repair_by_car_id(id)

    async def get_repair_by_client_id(self):
        id = int(input("input client id"))
        await self.presenter.get_repair_by_client_id(id)


    async def get_repair_by_date(self):
        id = input("input date work repair")
        await self.presenter.get_repair_by_date(id)

    async def get_repair_by_status(self):
        state = input("input status repair car")
        await self.presenter.get_repair_by_status(state)


