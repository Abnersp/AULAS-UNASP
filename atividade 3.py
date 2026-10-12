import requests
from datetime import datetime, timedelta


def cotar():
    def cotar_dia(data):
        url = fr"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data}'&$top=100&$format=json&$select=cotacaoCompra"
        res = requests.get(url)
        res = res.json()
        if res['value']:
            return res['value'][0]['cotacaoCompra']
        else:
            dia_anterior = datetime.strptime(data, "%m-%d-%Y") - timedelta(1)
            dia_anterior = datetime.strftime(dia_anterior, "%m-%d-%Y")
            return cotar_dia(dia_anterior)

    hoje = datetime.today()
    dias = [datetime.strftime(hoje - timedelta(i), "%m-%d-%Y") for i in range(365)]
    return [cotar_dia(dia) for dia in dias]


print(cotar())