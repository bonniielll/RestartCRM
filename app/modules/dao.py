from app.dao.base import BaseDao
from app.modules.models import Clients, DailyCash, NewTrading, ComissionTrading, ScrapTrading, Expertise, ScrapRecording


class ClientsDAO(BaseDao):
    model = Clients


class NewTradingDAO(BaseDao):
    model = NewTrading


class ComissionTradingDAO(BaseDao):
    model = ComissionTrading


class ScrapDAO(BaseDao):
    model = ScrapTrading


class ExpertiseDAO(BaseDao):
    model = Expertise


class ServiceDAO(BaseDao):
    model = ScrapRecording


class DailyDAO(BaseDao):
    model = DailyCash
