from bs4 import BeautifulSoup
import requests


def getExchangeRate(fechaInicio, fechaFinal = '0'):
    # Define the date range for the request.
    # In case of 'fechaFinal' not defined, the 'fechaInicio' is used.
    if fechaFinal == '0':
        fechaFinal = fechaInicio
    indicador = '158'
    # Create the URL with the date range.
    url = f"https://dof.gob.mx/indicadores_detalle.php?cod_tipo_indicador={indicador}&dfecha={fechaInicio}&hfecha={fechaFinal}"

    # Perform the GET request.
    response = requests.get(url, headers={'user-agent': 'apiwebscraper'}, verify=False)
    content = BeautifulSoup(response.content, 'html.parser')

    # From the content we get all the exchange rate cells.
    dataTags = content.find_all('tr', class_='Celda 1')
    
    # From the last selection, the table is divided in a list, which each element contains a complete row (date and exchange rate).
    dataRows = list(map(lambda tag: tag.find_all('td', class_='txt'), dataTags))

    # From the 'dataRows' list, the date is used as a 'key' and the exchange rate is converted to a float and used as a 'value'.
    data = {}
    for row in dataRows:
        data[row[0].get_text()] = float(row[1].get_text())
    
    # The function returns a dictionary with the date as the 'key' and the exchange rate as the 'value' for each date.
    # If the specific date or range selected does not contain an exchange rate, the function will return an empty dictionary.
    return data

# indicador = 158: TASA DE CAMBIO MXN A USD
# indicador = 159: UDIS
# indicador = 160: CCP
# indicador = 161: CCP-UDIS
# indicador = 162: CPP
# indicador = 163: CCP-DOLARES

# indicador = 165: TIIE 28 DIAS
# indicador = 166: TIIE 91 DIAS
# indicador = 167: TIIC DEPOSITOS 60 DIAS
# indicador = 168: TIIC DEPOSITOS 90 DIAS
# indicador = 169: TIIC DEPOSITOS 180 DIAS
# indicador = 170: TIIC PAGARES 28 DIAS
# indicador = 171: TIIC PAGARES 91 DIAS
# indicador = 172: TIIC PAGARES 182 DIAS

# indicador = 174: TIIE 182 DIAS
# indicador = 175: TIIE DE FONDEO
# indicador = 176: TIIE 90 DIAS
# indicador = 177: TIIE 29 DIAS
# indicador = 178: TIIE 27 DIAS
# indicador = 179: TIIE 26 DIAS
# indicador = 180: TIIE 181 DIAS
# indicador = 181: TIIE 92 DIAS
# indicador = 182: TIIE 89 DIAS
# indicador = 183: TIIE 183 DIAS
# indicador = 184: TIIE 180 DIAS
