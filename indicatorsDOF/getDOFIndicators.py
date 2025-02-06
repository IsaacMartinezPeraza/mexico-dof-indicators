from bs4 import BeautifulSoup
import requests

def getIndicator(indicator, startDate, endDate):
    # Create the URL with the date range.
    url = f"https://dof.gob.mx/indicadores_detalle.php?cod_tipo_indicador={indicator}&dfecha={startDate}&hfecha={endDate}"

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

# Function to obtain exchange rate from MXN to USD
def getExchangeRate(startDate, endDate = '0'):
    # Define the date range for the request.
    # In case of 'endDate' not defined, the 'startDate' is used.
    if endDate == '0':
        endDate = startDate
    indicator = '158'

    # Calls functions for GET request, if no data found, empty dictionary will be returned.
    exchangeRate = getIndicator(indicator, startDate, endDate)
    return exchangeRate

# Function to obtain UDIS rate
def getUDIS(startDate, endDate = '0'):
    # Define the date range for the request.
    # In case of 'endDate' not defined, the 'startDate' is used.
    if endDate == '0':
        endDate = startDate
    indicator = '159'

    # Calls functions for GET request, if no data found, empty dictionary will be returned.
    udis = getIndicator(indicator, startDate, endDate)
    return udis

# Function to obtain CPP rate
def getCPP(startDate, endDate = '0'):
    # Define the date range for the request.
    # In case of 'endDate' not defined, the 'startDate' is used.
    if endDate == '0':
        endDate = startDate
    indicator = '162'

    # Calls functions for GET request, if no data found, empty dictionary will be returned.
    cpp = getIndicator(indicator, startDate, endDate)
    return cpp

# Function to obtain CCP rate, and relations to UDIS and USD
def getCCP(startDate, endDate = '0', tipo = 'none'):
    match tipo.lower():
        case 'none':
            indicator = '160'
        case 'udis':
            indicator = '161'
        case 'usd':
            indicator = '163'
        case _:
            indicator = '160'

    # Define the date range for the request.
    # In case of 'endDate' not defined, the 'startDate' is used.
    if endDate == '0':
        endDate = startDate
    
    # Calls functions for GET request, if no data found, empty dictionary will be returned.
    ccp = getIndicator(indicator, startDate, endDate)
    return ccp

# Function to obtain TIIC DEPOSITOS rate
def getTIICdep(startDate, endDate = '0', period='60'):
    match period:
        case '60':
            indicator = '167'
        case '90':
            indicator = '168'
        case '180':
            indicator = '169'
        case _:
            indicator = '167'

    # Define the date range for the request.
    # In case of 'endDate' not defined, the 'startDate' is used.
    if endDate == '0':
        endDate = startDate

    # Calls functions for GET request, if no data found, empty dictionary will be returned.
    tiic = getIndicator(indicator, startDate, endDate)
    return tiic

# Function to obtain TIIC PAGARES rate
def getTIICpag(startDate, endDate = '0', period='28'):
    match period:
        case '28':
            indicator = '170'
        case '91':
            indicator = '171'
        case '182':
            indicator = '172'
        case _:
            indicator = '170'

    # Define the date range for the request.
    # In case of 'endDate' not defined, the 'startDate' is used.
    if endDate == '0':
        endDate = startDate

    # Calls functions for GET request, if no data found, empty dictionary will be returned.
    tiic = getIndicator(indicator, startDate, endDate)
    return tiic

# Function to obtain TIIE rate
def getTIIE(startDate, endDate = '0', period='26'):
    match period:
        case '26':
            indicator = '179'
        case '27':
            indicator = '178'
        case '28':
            indicator = '165'
        case '29':
            indicator = '177'
        case '89':
            indicator = '182'
        case '90':
            indicator = '176'
        case '91':
            indicator = '166'
        case '92':
            indicator = '181'
        case '180':
            indicator = '184'
        case '181':
            indicator = '180'
        case '182':
            indicator = '174'
        case '183':
            indicator = '183'
        case 'none':
            indicator = '175'
        case _:
            indicator = '179'

    # Define the date range for the request.
    # In case of 'endDate' not defined, the 'startDate' is used.
    if endDate == '0':
        endDate = startDate

    # Calls functions for GET request, if no data found, empty dictionary will be returned.
    tiie = getIndicator(indicator, startDate, endDate)
    return tiie