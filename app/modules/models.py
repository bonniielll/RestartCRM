from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from app.database import Base, str_uniq, int_pk, created_at, updated_at
from typing import List
from sqlalchemy import ForeignKey


class Clients(Base):
    id: Mapped[int_pk]
    Client: Mapped[List["NewTrading", "ComissionTrading", "ScrapTrading", "Expertise"]] = relationship(back_populates='client')
    phone_number: Mapped[str_uniq]
    names: Mapped[str]
    count_interactions: Mapped[int] = mapped_column(server_default=text('0'))
    first_interaction: Mapped[created_at]
    last_interaction: Mapped[updated_at]
    amount_revenue: Mapped[int] = mapped_column(server_default=text('0'))
    amount_payday: Mapped[int] = mapped_column(server_default=text('0'))


class NewTrading(Base):
    id: Mapped[int_pk]


class ComissionTrading(Base):
    id: Mapped[int_pk]


class ScrapTrading(Base):
    id: Mapped[int_pk]


class Expertise(Base):
    id: Mapped[int_pk]
