from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import as_declarative



@as_declarative()
class AbstractBase:
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)


class ClientTable(AbstractBase):
    __tablename__ = "Client"

    first_name: Mapped[str]
    last_name: Mapped[str]
    family_name: Mapped[str]
    phone_number: Mapped[int] = mapped_column(ForeignKey("Addressees.phone_number"))
    car_id: Mapped[int] = mapped_column(ForeignKey("Car.id"))


class AddresseesTable(AbstractBase):
    __tablename__ = "Addressees"

    phone_number: Mapped[int]


class CarsTable(AbstractBase):
    __tablename__ = "Cars"
    make: Mapped[str]
    model: Mapped[str]
    year: Mapped[int]
    sts_number: Mapped[str]
    client_id: Mapped[int] = mapped_column(ForeignKey("Client.client_id"))


class HistoryCarRepairTable(AbstractBase):
    __tablename__ = "HistoryCarRepair"

    date: Mapped[str]
    cost: Mapped[int]
    state: Mapped[str]
    client_id: Mapped[int] = mapped_column(ForeignKey("Client.client_id"))
    car_id: Mapped[int] = mapped_column(ForeignKey("Car.id"))


class SupportCarTable(AbstractBase):
    __tablename__ = "SupportCar"

    make: Mapped[str]
    model: Mapped[str]
    year: Mapped[int]
