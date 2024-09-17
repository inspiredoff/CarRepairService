from model.services import Services
from view.view import View


class Presenter:

    def __init__(self, view: View):
        self.__view = view
        self.__services = Services()

    # Client
    async def get_all_client(self):
        await self.__services.get_all_client()

    async def get_client_by_id(self, id: int):
        await self.__services.get_client_by_id(id)

    async def get_client_by_first_name(self, first_name: str):
        await self.__services.get_client_by_first_name(first_name)

    async def get_client_by_family_name(self, family_name: str):
        await self.__services.get_client_by_family_name(family_name)

    async def get_client_by_last_name(self, last_name: str):
        await self.__services.get_client_by_last_name(last_name)

    async def add_client(self, first_name: str, family_name: str, last_name: str, phone_number: int) -> None:
        await self.__services.add_client(first_name, family_name, last_name, phone_number)

    # Car
    async def get_all_car(self):
        await self.__services.get_all_car()

    async def get_car_by_id(self, id: int):
        await self.__services.get_car_by_id(id)

    async def get_car_by_make(self, make: str):
        await self.__services.get_car_by_make(make)

    async def get_car_by_model(self, model: str):
        await self.__services.get_car_by_model(model)

    async def add_car(self, make: str, model: str, year: int, number: str) -> None:
        await self.__services.add_car(make, model, year, number)

    # Repair
    async def get_all_repair(self):
        await self.__services.get_all_repair()

    async def get_repair_by_id(self, id: int):
        await self.__services.get_repair_by_id(id)

    async def get_repair_by_client_id(self, client_id: int):
        await self.__services.get_repair_by_client_id(client_id)

    async def get_repair_by_car_id(self, car_id: int):
        await self.__services.get_repair_by_car_id(car_id)

    async def get_repair_by_date(self, date: str):
        await self.__services.get_repair_by_date(date)

    async def get_repair_by_status(self, state: str):
        await self.__services.get_repair_by_status(state)

    # SupportCar
    async def get_make_by_id(self, make_id: int):
        await self.__services.get_make_by_id(make_id)

    async def get_model_by_id(self, model_id: int):
        await self.__services.get_model_by_id(model_id)

    async def get_model_by_make_name(self, make_name: str):
        await self.__services.get_model_by_make_name(make_name)

    async def get_model_by_make_id(self, make_id: int):
        await self.__services.get_model_by_make_id(make_id)

    async def get_make_by_name(self, make_name: str):
        await self.__services.get_make_by_name(make_name)

    async def get_all_model(self):
        await self.__services.get_all_models()

    async def get_all_make(self):
        await self.__services.get_all_make()
