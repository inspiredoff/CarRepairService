from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base, as_declarative

from model.src.storage.database import Base


@as_declarative()
class AbstractBase:
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    number: Mapped[str] = mapped_column(unique=True)


class ClientsTable(AbstractBase):
    __tablename__ = "Client"

    first_name: Mapped[str]
    last_name: Mapped[str]
    family_name: Mapped[str]
    car_id: Mapped[int] = mapped_column(ForeignKey("Car.id"))


class CarsTable(AbstractBase):
    __tablename__ = "Cars"

    brand: Mapped[str]
    model: Mapped[str]
    year: Mapped[int]
    client_id: Mapped[int] = mapped_column(ForeignKey("Client.client_id"))


class RepairsTable(AbstractBase):
    __tablename__ = "Repair"

    date: Mapped[int]
    cost: Mapped[int]
    client_id: Mapped[int] = mapped_column(ForeignKey("Client.client_id"))
    car_id: Mapped[int] = mapped_column(ForeignKey("Car.id"))
