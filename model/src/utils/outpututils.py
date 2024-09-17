from model.src.model.models import OriginEntity
from model.src.repository.models.models import AbstractBase


class OutputUtils:

    @staticmethod
    async def print_entity_ms(entity: OriginEntity):
        entity_dict = entity.__dict__
        print(entity_dict)



