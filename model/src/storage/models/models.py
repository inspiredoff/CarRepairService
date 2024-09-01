from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from model.src.storage.database import Base


class Client(Base):
    __tablename__ = "Car"

    client_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    family_name: Mapped[str]
    number_telephone: Mapped[str]
    car_id: Mapped[int] = mapped_column(ForeignKey("Car.id"))



class Car(Base):
    __tablename__ = "Client"

    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str]
    model: Mapped[str]
    year: Mapped[int]
    number: Mapped[str]
    client_id: Mapped[int] = mapped_column(ForeignKey("Client.client_id"))

