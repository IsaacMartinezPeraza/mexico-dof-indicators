# Mexico-DOF-Indicators
## Description
Module to obtain official exchange rate of MXN to USD from Mexico [DOF](https://dof.gob.mx/indicadores.php)

## First use
To start using this module first import it to your code
```py
from getDOFIndicators import getExchangeRate
```

## getExchangeRate()
```py
getExchangeRate(fechaInicio, fechaFinal = '0'):
```

The function expects one or two string parameters, in the format `"dd/mm/yyyy"`, it will return a dictionary with the *'key'* being the date as a `string`, and the *'value'* the exchange rate as a `float`. If no exchange rate is found in the date or range of dates provided, the function will return an empty dictionary.

You can call it with only the start date `fechaInicio` which will return the exchange rate of that date if there is any, or call it with a start date `fechaInicio` and end date `fechaFinal`. Be aware if the end date is before the start date the function will return an empty dictionary.
```py
getExchangeRate("24/04/2017")
# Returns: {'24-04-2017': 18.8413}

getExchangeRate("24/04/2017", "24/07/2017")
# Returns:
# {'24-04-2017': 18.8413, '25-04-2017': 18.6521, '26-04-2017': 18.9225, '27-04-2017': 19.1119, '28-04-2017': 19.067,
# '02-05-2017': 18.9594, '03-05-2017': 18.7731, '04-05-2017': 18.8031, '05-05-2017': 19.0019, '08-05-2017': 19.0137,
# '09-05-2017': 19.1164, '10-05-2017': 19.1364, '11-05-2017': 18.9587, '12-05-2017': 18.9039, '15-05-2017': 18.7594,
# '16-05-2017': 18.67, '17-05-2017': 18.6183, '18-05-2017': 18.6761, '19-05-2017': 18.8898, '22-05-2017': 18.6859,
# '23-05-2017': 18.6633, '24-05-2017': 18.615, '25-05-2017': 18.5689, '26-05-2017': 18.4185, '29-05-2017': 18.4849,
# '30-05-2017': 18.5121, '31-05-2017': 18.6643, '01-06-2017': 18.6909, '02-06-2017': 18.5941, '05-06-2017': 18.6204,
# '06-06-2017': 18.3819, '07-06-2017': 18.2762, '08-06-2017': 18.2278, '09-06-2017': 18.1946, '12-06-2017': 18.1939,
# '13-06-2017': 18.1802, '14-06-2017': 18.0725, '15-06-2017': 17.9343, '16-06-2017': 18.1154, '19-06-2017': 17.9321,
# '20-06-2017': 17.9519, '21-06-2017': 18.1167, '22-06-2017': 18.157, '23-06-2017': 18.127, '26-06-2017': 17.99,
# '27-06-2017': 17.8775, '28-06-2017': 17.9862, '29-06-2017': 17.8973, '30-06-2017': 18.0279, '03-07-2017': 18.0626,
# '04-07-2017': 18.2064, '05-07-2017': 18.2036, '06-07-2017': 18.3556, '07-07-2017': 18.3227, '10-07-2017': 18.1394,
# '11-07-2017': 17.9751, '12-07-2017': 17.9482, '13-07-2017': 17.7708, '14-07-2017': 17.7422, '17-07-2017': 17.5613,
# '18-07-2017': 17.5836, '19-07-2017': 17.5134, '20-07-2017': 17.4937, '21-07-2017': 17.526, '24-07-2017': 17.5618}

getExchangeRate("29/04/2017")
# Returns: {}

getExchangeRate("29/04/2017", "24/04/2017")
# Returns: {}
```
