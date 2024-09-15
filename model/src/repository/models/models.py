from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base, as_declarative

from model.src.repository.database import Base


@as_declarative()
class AbstractBase:
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)


class Client(AbstractBase):
    __tablename__ = "Client"

    first_name: Mapped[str]
    last_name: Mapped[str]
    family_name: Mapped[str]
    phone_number: Mapped[int] = mapped_column(ForeignKey("Addressees.phone_number"))
    car_id: Mapped[int] = mapped_column(ForeignKey("Car.id"))


class Addressees(AbstractBase):
    __tablename__ = "Addressees"

    phone_number: Mapped[int]


class Car(AbstractBase):
    __tablename__ = "Cars"
    make: Mapped[str]
    model: Mapped[str]
    year: Mapped[int]
    sts_number: Mapped[int]
    client_id: Mapped[int] = mapped_column(ForeignKey("Client.client_id"))


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
