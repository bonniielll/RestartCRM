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
    scrap_akb: Mapped[str]
    scrap_price: Mapped[str]
    action_sum: Mapped[str]
    sum: Mapped[str]
    method: Mapped[str]
    comment: Mapped[str]
    payment_invoice: Mapped[str]
    invoice_data: Mapped[str]


class ComissionTrading(Base):
    id: Mapped[int_pk]
    akb_name: Mapped[str]
    guarantee: Mapped[str]
    price: Mapped[str]
    action_sum: Mapped[str]
    sum: Mapped[str]
    method_pay: Mapped[str]
    client: Mapped[str]


class ScrapTrading(Base):
    id: Mapped[int_pk]
    client: Mapped[str]
    ah_akb: Mapped[str]
    sum: Mapped[str]
    method_pay: Mapped[str]
    comment: Mapped[str]
    mandarin_data: Mapped[str]
    passport_photo: Mapped[str]


class Expertise(Base):
    id: Mapped[int_pk]
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
    akb_name: Mapped[str]
    service_pay_sum: Mapped[str]
    comment_before: Mapped[str]
    akb_on_switch: Mapped[str]
    deposit_for_switch_sum: Mapped[str]
    comment_after: Mapped[str]
    pay_method: Mapped[str]
