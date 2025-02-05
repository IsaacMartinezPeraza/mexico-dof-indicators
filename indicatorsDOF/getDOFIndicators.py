from bs4 import BeautifulSoup
import requests


def getExchangeRate(fechaInicio, fechaFinal = '0'):
    # Define the date range for the request.
    # In case of 'fechaFinal' not defined, the 'fechaInicio' is used.
    if fechaFinal == '0':
        fechaFinal = fechaInicio
    
    # Create the URL with the date range.
    url = f"https://dof.gob.mx/indicadores_detalle.php?cod_tipo_indicador=158&dfecha={fechaInicio}&hfecha={fechaFinal}"

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
