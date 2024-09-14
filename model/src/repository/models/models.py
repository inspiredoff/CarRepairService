from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base, as_declarative

from model.src.repository.database import Base


@as_declarative()
class AbstractBase:
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)


class AbcCar(AbstractBase):
    make: Mapped[str]
    model: Mapped[str]
    year: Mapped[int]
    sts_number: Mapped[int]
    client_id: Mapped[int] = mapped_column(ForeignKey("Client.client_id"))


class Client(AbstractBase):
    __tablename__ = "Client"

    first_name: Mapped[str]
    last_name: Mapped[str]
    family_name: Mapped[str]
    car_id: Mapped[int] = mapped_column(ForeignKey("Car.id"))


class adresess(AbstractBase):
    __tablename__ = "adresess"

    phone_number: Mapped[int]
    client_id: Mapped[int] = mapped_column(ForeignKey("Client.client_id"))


class Car(AbcCar):
    __tablename__ = "Cars"


class HistoryCarRepair(AbstractBase):
    __tablename__ = "HistoryCarRepair"

    date: Mapped[int]
    cost: Mapped[int]
    client_id: Mapped[int] = mapped_column(ForeignKey("Client.client_id"))
    car_id: Mapped[int] = mapped_column(ForeignKey("Car.id"))


class SupportCar(AbstractBase):
    __tablename__ = "SupportCar"

    make: Mapped[str]
    model: Mapped[str]
    year: Mapped[int]
