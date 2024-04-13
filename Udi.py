from .utils import BanxicoAPI
from datetime import date

class Udi():
    def __init__(self, token):
        self.api= BanxicoAPI(token)
        self.idSeries = self.api.getIDSeries("UDI")

    def getIDSerie(self):
        return self.idSeries 

    def get_UDI_Today(self) -> float:
        today=date.today()
        return self.api.callAPI(self.idSeries["UDI"],str(today)+'/'+str(today))

    def get_UDI_date(self, date) -> float:
        return self.api.callAPI(self.idSeries["UDI"],str(date)+'/'+str(date))

    def get_UDI_date_range(self, init_Date, finish_Date) -> float:
        return self.api.callAPI(self.idSeries["UDI"],str(init_Date)+'/'+str(finish_Date))

    def get_UDI_last_value(self):
        return self.api.callAPI(self.idSeries["UDI"],"oportuno")
