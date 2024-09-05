from pydantic import BaseModel, EmailStr, Field, validator
import re


class SClientAdding(BaseModel):
    phone_number: str = Field(..., min_length=5, max_length=50, description="Номер телефона в международном формате, начинающийся с '+'")
    names: str = Field(..., min_length=2, max_length=50, description="ФИО клиента")
    comment: str = Field(..., min_length=1, max_length=50, description="Комментарий")


class SNewAdding(BaseModel):
    client_number: str = Field(..., min_length=5, max_length=50, description='Номер клиента')
    akb: str = Field(..., min_length=5, max_length=50, description='Название нового АКБ')
    scrap_akb: str = Field(..., min_length=5, max_length=50, description='Старый АКБ')
    scrap_price: str = Field(..., min_length=5, max_length=50, description='Сумма за старый АКБ')
    action_sum: str = Field(..., min_length=5, max_length=50, description='Сумма скидка')
    sum: str = Field(..., min_length=5, max_length=50, description='Сумма продажи')
    method: str = Field(..., min_length=5, max_length=50, description='Способ оплаты')
    comment: str = Field(..., min_length=5, max_length=50, description='Комментарий')
    payment_invoice: str = Field(..., min_length=3, max_length=50, description='Оплата по счету')
    invoice_data: str = Field(..., min_length=0, max_length=50, description='Оплата по счету')


class SComissionAdding(BaseModel):
    akb_name: str = Field(..., min_length=5, max_length=50, description='Название акб (и код)')
    guarantee: str = Field(..., min_length=5, max_length=50, description='Гарантия (мес)')
    price: str = Field(..., min_length=5, max_length=50, description='Цена акб')
    action_sum: str = Field(..., min_length=5, max_length=50, description='Сумма скидки')
    sum: str = Field(..., min_length=5, max_length=50, description='Сумма оплаты')
    method_pay: str = Field(..., min_length=5, max_length=50, description='Способ оплаты')
    client: str = Field(..., min_length=5, max_length=50, description='Номер клиента')


class SScrapAdding(BaseModel):
    client: str = Field(..., min_length=5, max_length=50, description='Номер клиента')
    ah_akb: str = Field(..., min_length=5, max_length=50, description='Объём АКБ')
    sum: str = Field(..., min_length=5, max_length=50, description='Сумма выплаты')
    method_pay: str = Field(..., min_length=5, max_length=50, description='Метод выплаты')
    comment: str = Field(..., min_length=5, max_length=50, description='Комментарий')
    mandarin_data: str = Field(..., min_length=5, max_length=50, description='Данные для мандарина')
    passport_photo: str = Field(..., min_length=5, max_length=50, description='Ссылка на фото паспорта')


class SExperiseAdding(BaseModel):
    akb_name: str = Field(..., min_length=5, max_length=50, description='Название акб и код')
    client: str = Field(..., min_length=5, max_length=50, description='Номер клиента')
    when_broken: str = Field(..., min_length=2, max_length=50, description='Когда обнаружили брак')
    akb_docs: str = Field(..., min_length=0, max_length=50, description='Где документы')
    akb_place: str = Field(..., min_length=2, max_length=50, description='Где акб')
    comment_on_start: str = Field(..., min_length=5, max_length=50, description='Комментарии на момент принятия')
    akb_on_switch: str = Field(..., min_length=0, max_length=50, description='Подменный акб (Если есть то название)')
    manager: str = Field(..., min_length=2, max_length=50, description='Имя менеджера, который принял АКБ')
    market: str = Field(..., min_length=2, max_length=50, description='Магазин, в котором акб приняли')
    tracker_url: str = Field(..., min_length=0, max_length=50, description='Ссылка на трекер')


class SServiceAdding(BaseModel):
    akb_name: str = Field(..., min_length=5, max_length=50, description='Название акб')
    service_pay_sum: str = Field(..., min_length=5, max_length=50, description='Сумма за услуги')
    comment_before: str = Field(..., min_length=5, max_length=50, description='Комментарий на момент приема АКБ')
    akb_on_switch: str = Field(..., min_length=0, max_length=50, description='Акб на подмену (название и код)')
    deposit_for_switch_sum: str = Field(..., min_length=0, max_length=50, description='Залог за подменный АКБ')
    comment_after: str = Field(..., min_length=0, max_length=50, description='Коментарий после передачи АКБ клиенту')
    pay_method: str = Field(..., min_length=5, max_length=50, description='Способ оплаты')