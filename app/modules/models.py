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

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"


class NewTrading(Base):
    id: Mapped[int_pk]
    account: Mapped[str]
    client_number: Mapped[str] = mapped_column(server_default=text('0'))
    akb: Mapped[str]
    akb_price: Mapped[int]
    scrap_akb: Mapped[str]
    scrap_price: Mapped[int] = mapped_column(server_default=text('0'))
    action_sum: Mapped[int] = mapped_column(server_default=text('0'))
    sum: Mapped[int]
    method: Mapped[str]
    comment: Mapped[str]
    payment_invoice: Mapped[str]
    invoice_data: Mapped[str]


class ComissionTrading(Base):
    id: Mapped[int_pk]
    account: Mapped[str]
    akb_name: Mapped[str]
    guarantee: Mapped[str]
    price: Mapped[int]
    action_sum: Mapped[int] = mapped_column(server_default=text('0'))
    sum: Mapped[int]
    method_pay: Mapped[str]
    client: Mapped[str]


class ScrapTrading(Base):
    id: Mapped[int_pk]
    account: Mapped[str]
    client: Mapped[str]
    ah_akb: Mapped[str]
    sum: Mapped[int]
    method_pay: Mapped[str]
    comment: Mapped[str]
    mandarin_data: Mapped[str]
    passport_photo: Mapped[str]


class Expertise(Base):
    id: Mapped[int_pk]
    account: Mapped[str]
    akb_name: Mapped[str]
    client: Mapped[str]
    when_broken: Mapped[str]
    akb_docs: Mapped[str]
    akb_place: Mapped[str]
    comment_on_start: Mapped[str]
    akb_on_switch: Mapped[str]
    manager: Mapped[str]
    market: Mapped[str]
    tracker_url: Mapped[str]
        

class Service(Base):
    id: Mapped[int_pk]
    account: Mapped[str]
    akb_name: Mapped[str]
    service_pay_sum: Mapped[int] = mapped_column(server_default=text('0'))
    comment_before: Mapped[str]
    akb_on_switch: Mapped[str]
    deposit_for_switch_sum: Mapped[int] = mapped_column(server_default=text('0'))
    comment_after: Mapped[str]
    pay_method: Mapped[str]


class ScrapRecording(Base):
    id: Mapped[int_pk]
    account: Mapped[str]
    move: Mapped[str]
    akb: Mapped[str]
    price: Mapped[int]
    sum: Mapped[int]
    method_pay: Mapped[str]
    comment: Mapped[str]
    where_move: Mapped[str]

