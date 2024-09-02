from app.dao.base import BaseDao
from app.modules.models import Clients, NewTrading, ComissionTrading, ScrapTrading, Expertise


class ClientsDAO(BaseDao):
    model = Clients

class NewTradingDAO(BaseDao):
    model = NewTrading

class ComissionDAO(BaseDao):
    model = ComissionTrading

class ScrapDAO(BaseDao):
    model = ScrapTrading

class ExpertiseDAO(BaseDao):
    model = Expertise