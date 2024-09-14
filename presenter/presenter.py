from model.src.services import Services
from view.view import View


class Presenter:

    def __init__(self, view: View):
        self.view = view
        self.services = Services()

    #Client
    async def get_all_client(self):
        await self.services.get_all_client()

    async def get_client_by_id(self, id: int):
        await self.services.get_client_by_id(id)

    async def get_client_by_first_name(self, first_name: str):
        await self.services.get_client_by_first_name(first_name)

    async def get_client_by_family_name(self, family_name: str):
        await self.services.get_client_by_family_name(family_name)

    async def get_client_by_last_name(self, last_name: str):
        await self.services.get_client_by_last_name(last_name)

    #Car
    async def get_all_car(self):
        await self.services.get_all_car()

    async def get_car_by_id(self, id: int):
        await self.services.get_car_by_id(id)

    async def get_car_by_brand(self, brand: str):
        await self.services.get_car_by_brand(brand)

    async def get_car_by_model(self, model: str):
        await self.services.get_car_by_model(model)

    #Repair
    async def get_all_repair(self):
        pass

    async def get_repair_by_id(self, id: int):
        pass

    async def get_repair_by_car_id(self, id: int):
        pass

    async def get_repair_by_client_id(self, id: int):
        pass

    async def get_repair_by_date(self, date: str):
        pass

    async def get_repair_by_status(self, status: str):
        pass