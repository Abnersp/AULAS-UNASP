import requests
from datetime import datetime, timedelta

def cotar(data):
    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data}'&$top=100&$format=json"

    res = requests.get(url)
    res = res.json()

    if res['value']:
        return res['value'][0]['cotacaoCompra']
    else:
        dia_anterior = datetime.strptime(data, "%m-%d-%Y") - timedelta(1)
        dia_anterior = datetime.strftime(dia_anterior, "%m-%d-%Y")
        return cotar(dia_anterior)
        