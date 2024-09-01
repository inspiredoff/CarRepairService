from model.src.models.entity import Entity
from model.src.storage.storage import Database


class car_storage(Database):
    async def get_entity_by_id(self, id: int) -> Entity:
        pass

    async def get_entity_by_name(self, name: str) -> Entity:
        pass

    async def get_entity_by_number(self, number: str) -> Entity:
        pass

    async def get_all_entities(self) -> list[Entity]:
        pass


    async def add_entity(self, entity: Entity):
        pass