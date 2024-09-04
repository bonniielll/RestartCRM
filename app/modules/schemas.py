from pydantic import BaseModel, EmailStr, Field, validator
import re


class SClientAdding(BaseModel):
    phone_number: str = Field(..., min_length=5, max_length=50, description="Номер телефона в международном формате, начинающийся с '+'")
    names: str = Field(..., min_length=2, max_length=50, description="ФИО клиента")
    comment: str = Field(..., min_length=0, max_length=50, description="Комментарий")


class SNewAdding(BaseModel):
    client_number: str = Field(..., min_length=5, max_length=50, description='Номер клиента')
    akb: str = Field(..., min_length=5, max_length=50, description='Название нового АКБ')
