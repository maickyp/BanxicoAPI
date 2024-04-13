from .utils import BanxicoAPI
from datetime import date

class Cetes():
    def __init__(self, token):
        self.api= BanxicoAPI(token)
        self.idSeries=self.api.getIDSeries("CETES")

    def getIDSerie(self):
        return self.idSeries 
    
    def get_CETES28_Today(self) -> float:
        today=date.today()
        return self.api.callAPI(self.idSeries["CETES28_RENDIMIENTO"],str(today)+'/'+str(today))

    def get_CETES28_date(self, date) -> float:
        return self.api.callAPI(self.idSeries["CETES28_RENDIMIENTO"],str(date)+'/'+str(date))

    def get_CETES28_date_range(self, init_Date, finish_Date) -> float:
        return self.api.callAPI(self.idSeries["CETES28_RENDIMIENTO"],str(init_Date)+'/'+str(finish_Date))

    def get_CETES28_last_value(self):
        return self.api.callAPI(self.idSeries["CETES28_RENDIMIENTO"],'oportuno')

    