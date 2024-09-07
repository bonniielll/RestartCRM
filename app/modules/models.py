from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from app.database import Base, str_uniq, int_pk, created_at, updated_at
from typing import List
from sqlalchemy import ForeignKey


class Clients(Base):
    id: Mapped[int_pk]
    account: Mapped[str] = mapped_column(server_default=text('Нет'))
    phone_number: Mapped[str_uniq]
    names: Mapped[str]
    comment: Mapped[str]
    count_interactions: Mapped[int] = mapped_column(server_default=text('0'))
    amount_revenue: Mapped[int] = mapped_column(server_default=text('0'))
    amount_payday: Mapped[int] = mapped_column(server_default=text('0'))


class NewTrading(Base):
    id: Mapped[int_pk]
    account: Mapped[str] = mapped_column(server_default=text('Нет'))
    client_number: Mapped[str]
    akb: Mapped[str]
    scrap_akb: Mapped[str]
    scrap_price: Mapped[int]
    action_sum: Mapped[int]
    sum: Mapped[int]
    method: Mapped[str]
    comment: Mapped[str] = mapped_column(server_default=text('Нет'))
    payment_invoice: Mapped[str] = mapped_column(server_default=text('Нет'))
    invoice_data: Mapped[str] = mapped_column(server_default=text('Нет'))


class ComissionTrading(Base):
    id: Mapped[int_pk]
    account: Mapped[str] = mapped_column(server_default=text('Нет'))
    akb_name: Mapped[str]
    guarantee: Mapped[str]
    price: Mapped[int]
    action_sum: Mapped[int] = mapped_column(server_default=text('0'))
    sum: Mapped[int]
    method_pay: Mapped[str]
    client: Mapped[str] = mapped_column(server_default=text('Нет'))


class ScrapTrading(Base):
    id: Mapped[int_pk]
    account: Mapped[str] = mapped_column(server_default=text('Нет'))
    client: Mapped[str] = mapped_column(server_default=text('Нет'))
    ah_akb: Mapped[str]
    sum: Mapped[int]
    method_pay: Mapped[str]
    comment: Mapped[str] = mapped_column(server_default=text('Нет'))
    mandarin_data: Mapped[str] = mapped_column(server_default=text('Нет'))
    passport_photo: Mapped[str] = mapped_column(server_default=text('Нет'))


class Expertise(Base):
    id: Mapped[int_pk]
    account: Mapped[str] = mapped_column(server_default=text('Нет'))
    akb_name: Mapped[str]
    client: Mapped[str]
    when_broken: Mapped[str] = mapped_column(server_default=text('После продажи клиенту'))
    akb_docs: Mapped[str]
    akb_place: Mapped[str]
    comment_on_start: Mapped[str]
    akb_on_switch: Mapped[str] = mapped_column(server_default=text('Нет'))
    manager: Mapped[str]
    market: Mapped[str]
    tracker_url: Mapped[str] = mapped_column(server_default=text('Нет'))
        

class Service(Base):
    id: Mapped[int_pk]
    account: Mapped[str] = mapped_column(server_default=text('Нет'))
    akb_name: Mapped[str]
    service_pay_sum: Mapped[int] = mapped_column(server_default=text('0'))
    comment_before: Mapped[str]
    akb_on_switch: Mapped[str] = mapped_column(server_default=text('Нет'))
    deposit_for_switch_sum: Mapped[int] = mapped_column(server_default=text('0'))
    comment_after: Mapped[str] = mapped_column(server_default=text('Нет'))
    pay_method: Mapped[str]


class ScrapRecording(Base):
    id: Mapped[int_pk]
    account: Mapped[str] = mapped_column(server_default=text('Нет'))
    move: Mapped[str]
    akb: Mapped[str]
    price: Mapped[int]
    sum: Mapped[int]
    method_pay: Mapped[str]
    comment: Mapped[str]


