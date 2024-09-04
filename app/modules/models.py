from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from app.database import Base, str_uniq, int_pk, created_at, updated_at
from typing import List
from sqlalchemy import ForeignKey


class Clients(Base):
    id: Mapped[int_pk]
    phone_number: Mapped[str_uniq]
    names: Mapped[str]
    comment: Mapped[str]
    count_interactions: Mapped[int] = mapped_column(server_default=text('0'))
    amount_revenue: Mapped[int] = mapped_column(server_default=text('0'))
    amount_payday: Mapped[int] = mapped_column(server_default=text('0'))


class NewTrading(Base):
    id: Mapped[int_pk]
    client_number: Mapped[str]
    akb: Mapped[str]
    method: Mapped[str]
    scrap_akb: Mapped[str]
    sum: Mapped[str]



class ComissionTrading(Base):
    id: Mapped[int_pk]


class ScrapTrading(Base):
    id: Mapped[int_pk]


class Expertise(Base):
    id: Mapped[int_pk]


class Service(Base):
    id: Mapped[int_pk]
