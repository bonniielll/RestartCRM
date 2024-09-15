from pydantic import BaseModel, EmailStr, Field, validator
import re


class SClientAdding(BaseModel):
    phone_number: str = Field(..., description="Номер телефона в международном формате, начинающийся с '+'")
    names: str = Field(..., min_length=2, max_length=50, description="ФИО клиента")
    comment: str = Field(..., min_length=1, max_length=50, description="Комментарий")


class SNewAdding(BaseModel):
    account: str = Field(..., min_length=0, max_length=30, description='Аккаунт')
    client_number: str = Field(..., description='Номер клиента')
    akb: str = Field(..., min_length=2, max_length=50, description='Название нового АКБ')
    akb_price: int = Field(..., description='Цена за новый АКБ')
    scrap_akb: str = Field(..., min_length=0, max_length=50, description='Старый АКБ')
    scrap_price: int = Field(..., description='Сумма за старый АКБ')
    action_sum: int = Field(..., description='Сумма скидки')
    sum: int = Field(..., description='Сумма продажи')
    method: str = Field(..., min_length=0, max_length=50, description='Способ оплаты')
    comment: str = Field(..., description='Комментарий')
    payment_invoice: str = Field(..., description='Оплата по счету')
    invoice_data: str = Field(..., description='Оплата по счету')


class SComissionAdding(BaseModel):
    account: str = Field(..., min_length=0, max_length=30, description='Аккаунт')
    akb_name: str = Field(..., min_length=0, max_length=50, description='Название акб (и код)')
    guarantee: int = Field(..., description='Гарантия (мес)')
    price: float = Field(..., description='Цена акб')
    scrap_akb: str = Field(..., description='Старый акб')
    scrap_price: float = Field(..., description='Сумма за старый акб')
    action_sum: float = Field(..., description='Сумма скидки')
    sum: float = Field(..., description='Сумма оплаты')
    method_pay: str = Field(..., description='Способ оплаты')
    client: str = Field(..., description='Номер клиента')
    comment: str = Field(..., description='Комментарий к продаже')


class SScrapAdding(BaseModel):
    account: str = Field(..., description='Магазин')
    client: str = Field(..., description='Номер клиента')
    ah_akb: str = Field(..., description='Объём АКБ')
    count: float = Field(..., description='Количество/Вес')
    price: float = Field(..., description='Цена за кг/шт')
    sum: float = Field(..., description='Сумма выплаты')
    method_pay: str = Field(..., description='Метод выплаты')
    comment: str = Field(..., description='Комментарий')
    mandarin_data: str = Field(..., description='Данные для мандарина')
    passport_photo: str = Field(..., description='Ссылка на фото паспорта')


class SExperiseAdding(BaseModel):
    account: str = Field(..., description='Магазин')
    akb_name: str = Field(..., description='Название акб и код')
    client: str = Field(..., description='Номер клиента')
    client_names: str = Field(..., description='ФИО клиента')
    when_broken: str = Field(..., min_length=2, max_length=50, description='Когда обнаружили брак')
    akb_docs: str = Field(..., min_length=0, max_length=50, description='Где документы')
    akb_place: str = Field(..., min_length=2, max_length=50, description='Где акб')
    comment_on_start: str = Field(..., description='Комментарии на момент принятия')
    akb_on_switch: str = Field(..., min_length=0, max_length=50, description='Подменный акб (Если есть то название)')
    manager: str = Field(..., min_length=2, max_length=50, description='Имя менеджера, который принял АКБ')
    tracker_url: str = Field(..., description='Ссылка на трекер')


class SServiceAdding(BaseModel):
    akb_name: str = Field(..., min_length=5, max_length=50, description='Название акб')
    service_pay_sum: str = Field(..., min_length=5, max_length=50, description='Сумма за услуги')
    comment_before: str = Field(..., min_length=5, max_length=50, description='Комментарий на момент приема АКБ')
    akb_on_switch: str = Field(..., min_length=0, max_length=50, description='Акб на подмену (название и код)')
    deposit_for_switch_sum: str = Field(..., min_length=0, max_length=50, description='Залог за подменный АКБ')
    comment_after: str = Field(..., min_length=0, max_length=50, description='Коментарий после передачи АКБ клиенту')
    pay_method: str = Field(..., min_length=5, max_length=50, description='Способ оплаты')


class SDailyAdding(BaseModel):
    magazine: str = Field(..., description='Магазин')
    manager: str = Field(..., description='Менеджер')
    cash: float = Field(..., description='Остаток в кассе')
    daytime: str = Field(..., description='Утро/Вечер')