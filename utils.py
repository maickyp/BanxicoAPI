import requests
import json
from os import path

class BanxicoAPI():
    def __init__(self, token):
        self.headers={'Bmx-Token': token}
        # print(path.dirname(path.abspath(__file__)))
        with open(path.join(path.dirname(path.abspath(__file__)),"idSeries.json"), "r") as jsonfile:
            self.idSeries = json.load(jsonfile)

    def __getRequest__(self, catalogo:str, opts="oportuno") ->json:
        response = requests.get(catalogo+opts, headers=self.headers)
        json_response = json.loads(response.content)
        return json_response['bmx']['series'][0]["datos"]
    
    def __url(self, idSeries:str):
        return self.idSeries['API_URI']+idSeries+"/datos/"
    
    def getIDSeries(self, key):
        return self.idSeries[key]
    
    def callAPI(self, idSerie:str, opts=None):
        return self.__getRequest__(self.__url(idSerie),opts)