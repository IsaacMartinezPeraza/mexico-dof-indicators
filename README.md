# Mexico-DOF-Indicators
## Description
Module to obtain official exchange rate of MXN to USD from Mexico [DOF](https://dof.gob.mx/indicadores.php)

## First use
To start using this module first import it to your code
```py
from getDOFIndicators import *
```
## Methods
### getIndicator()
```py
getIndicator(indicator, startDate, endDate)
```
The function expects three string parameters, the first `indicator` as a `string` with the number of the indicators[^1], the `startDate` and `endDate` in the format `"dd/mm/yyyy"`. This function will return a dictionary with the *'key'* being the date as a `string`, and the *'value'* the rate as a `float`. If no rate is found in the date or range of dates provided, the function will return an empty dictionary.

Be aware if the end date is before the start date the function will return an empty dictionary.
```py
getIndicator("158","24/04/2017", "24/07/2017")
# Returns:
# {'24-04-2017': 18.8413, '25-04-2017': 18.6521, '26-04-2017': 18.9225, '27-04-2017': 19.1119,
# '28-04-2017': 19.067, '02-05-2017': 18.9594, '03-05-2017': 18.7731, '04-05-2017': 18.8031,
# '05-05-2017': 19.0019, '08-05-2017': 19.0137, '09-05-2017': 19.1164, '10-05-2017': 19.1364,
# '11-05-2017': 18.9587, '12-05-2017': 18.9039, '15-05-2017': 18.7594, '16-05-2017': 18.67,
# '17-05-2017': 18.6183, '18-05-2017': 18.6761, '19-05-2017': 18.8898, '22-05-2017': 18.6859,
# '23-05-2017': 18.6633, '24-05-2017': 18.615, '25-05-2017': 18.5689, '26-05-2017': 18.4185,
# '29-05-2017': 18.4849, '30-05-2017': 18.5121, '31-05-2017': 18.6643, '01-06-2017': 18.6909,
# '02-06-2017': 18.5941, '05-06-2017': 18.6204, '06-06-2017': 18.3819, '07-06-2017': 18.2762,
# '08-06-2017': 18.2278, '09-06-2017': 18.1946, '12-06-2017': 18.1939, '13-06-2017': 18.1802,
# '14-06-2017': 18.0725, '15-06-2017': 17.9343, '16-06-2017': 18.1154, '19-06-2017': 17.9321,
# '20-06-2017': 17.9519, '21-06-2017': 18.1167, '22-06-2017': 18.157, '23-06-2017': 18.127,
# '26-06-2017': 17.99, '27-06-2017': 17.8775, '28-06-2017': 17.9862, '29-06-2017': 17.8973,
# '30-06-2017': 18.0279, '03-07-2017': 18.0626, '04-07-2017': 18.2064, '05-07-2017': 18.2036,
# '06-07-2017': 18.3556, '07-07-2017': 18.3227, '10-07-2017': 18.1394, '11-07-2017': 17.9751,
# '12-07-2017': 17.9482, '13-07-2017': 17.7708, '14-07-2017': 17.7422, '17-07-2017': 17.5613,
# '18-07-2017': 17.5836, '19-07-2017': 17.5134, '20-07-2017': 17.4937, '21-07-2017': 17.526, 
# '24-07-2017': 17.5618}

getIndicator("158","29/04/2017", "24/04/2017")
# Returns: {}
```

### getExchangeRate()
```py
getExchangeRate(startDate, endDate = '0')
```
The function expects one or two string parameters, in the format `"dd/mm/yyyy"`, it will return a dictionary with the *'key'* being the date as a `string`, and the *'value'* the exchange rate as a `float`. If no exchange rate is found in the date or range of dates provided, the function will return an empty dictionary.

You can call it with only the start date `startDate` which will return the exchange rate of that date if there is any, or call it with a start date `startDate` and end date `endDate`. Be aware if the end date is before the start date the function will return an empty dictionary.
```py
getExchangeRate("24/04/2017")
# Returns: {'24-04-2017': 18.8413}

getExchangeRate("24/04/2017", "24/07/2017")
# Returns:
# {'24-04-2017': 18.8413, '25-04-2017': 18.6521, '26-04-2017': 18.9225, '27-04-2017': 19.1119,
# '28-04-2017': 19.067, '02-05-2017': 18.9594, '03-05-2017': 18.7731, '04-05-2017': 18.8031,
# '05-05-2017': 19.0019, '08-05-2017': 19.0137, '09-05-2017': 19.1164, '10-05-2017': 19.1364,
# '11-05-2017': 18.9587, '12-05-2017': 18.9039, '15-05-2017': 18.7594, '16-05-2017': 18.67,
# '17-05-2017': 18.6183, '18-05-2017': 18.6761, '19-05-2017': 18.8898, '22-05-2017': 18.6859,
# '23-05-2017': 18.6633, '24-05-2017': 18.615, '25-05-2017': 18.5689, '26-05-2017': 18.4185,
# '29-05-2017': 18.4849, '30-05-2017': 18.5121, '31-05-2017': 18.6643, '01-06-2017': 18.6909,
# '02-06-2017': 18.5941, '05-06-2017': 18.6204, '06-06-2017': 18.3819, '07-06-2017': 18.2762,
# '08-06-2017': 18.2278, '09-06-2017': 18.1946, '12-06-2017': 18.1939, '13-06-2017': 18.1802,
# '14-06-2017': 18.0725, '15-06-2017': 17.9343, '16-06-2017': 18.1154, '19-06-2017': 17.9321,
# '20-06-2017': 17.9519, '21-06-2017': 18.1167, '22-06-2017': 18.157, '23-06-2017': 18.127,
# '26-06-2017': 17.99, '27-06-2017': 17.8775, '28-06-2017': 17.9862, '29-06-2017': 17.8973,
# '30-06-2017': 18.0279, '03-07-2017': 18.0626, '04-07-2017': 18.2064, '05-07-2017': 18.2036,
# '06-07-2017': 18.3556, '07-07-2017': 18.3227, '10-07-2017': 18.1394, '11-07-2017': 17.9751,
# '12-07-2017': 17.9482, '13-07-2017': 17.7708, '14-07-2017': 17.7422, '17-07-2017': 17.5613,
# '18-07-2017': 17.5836, '19-07-2017': 17.5134, '20-07-2017': 17.4937, '21-07-2017': 17.526, 
# '24-07-2017': 17.5618}

getExchangeRate("29/04/2017")
# Returns: {}

getExchangeRate("29/04/2017", "24/04/2017")
# Returns: {}
```

### getUDIS()
```py
getExchangeRate(startDate, endDate = '0')
```

The function expects one or two string parameters, in the format `"dd/mm/yyyy"`, it will return a dictionary with the *'key'* being the date as a `string`, and the *'value'* the UDIS as a `float`. If no UDIS is found in the date or range of dates provided, the function will return an empty dictionary.

You can call it with only the start date `startDate` which will return the UDIS of that date if there is any, or call it with a start date `startDate` and end date `endDate`. Be aware if the end date is before the start date the function will return an empty dictionary.

```py
getUDIS("24/04/2017")
# Returns: {'24-04-2017': 5.750421}

getUDIS("24/04/2017", "24/07/2017")
# Returns:
# {'24-04-2017': 5.750421, '25-04-2017': 5.751477, '26-04-2017': 5.750899, '27-04-2017': 5.750322,
# '28-04-2017': 5.749745, '29-04-2017': 5.749167, '30-04-2017': 5.74859, '01-05-2017': 5.748013,
# '02-05-2017': 5.747436, '03-05-2017': 5.746859, '04-05-2017': 5.746282, '05-05-2017': 5.745705,
# '06-05-2017': 5.745128, '07-05-2017': 5.744552, '08-05-2017': 5.743975, '09-05-2017': 5.743398,
# '10-05-2017': 5.742822, '11-05-2017': 5.743865, '12-05-2017': 5.744909, '13-05-2017': 5.745952,
# '14-05-2017': 5.746996, '15-05-2017': 5.74804, '16-05-2017': 5.749085, '17-05-2017': 5.750129,
# '18-05-2017': 5.751174, '19-05-2017': 5.752219, '20-05-2017': 5.753264, '21-05-2017': 5.754309,
# '22-05-2017': 5.755354, '23-05-2017': 5.7564, '24-05-2017': 5.757446, '25-05-2017': 5.758492,
# '26-05-2017': 5.757274, '27-05-2017': 5.756057, '28-05-2017': 5.75484, '29-05-2017': 5.753623,
# '30-05-2017': 5.752406, '31-05-2017': 5.75119, '01-06-2017': 5.749974, '02-06-2017': 5.748758,
# '03-06-2017': 5.747542, '04-06-2017': 5.746327, '05-06-2017': 5.745112, '06-06-2017': 5.743897,
# '07-06-2017': 5.742683, '08-06-2017': 5.741469, '09-06-2017': 5.740255, '10-06-2017': 5.739041,
# '11-06-2017': 5.739672, '12-06-2017': 5.740303, '13-06-2017': 5.740934, '14-06-2017': 5.741566,
# '15-06-2017': 5.742197, '16-06-2017': 5.742829, '17-06-2017': 5.74346, '18-06-2017': 5.744092,
# '19-06-2017': 5.744724, '20-06-2017': 5.745356, '21-06-2017': 5.745988, '22-06-2017': 5.746619,
# '23-06-2017': 5.747251, '24-06-2017': 5.747884, '25-06-2017': 5.748516, '26-06-2017': 5.749095,
# '27-06-2017': 5.749675, '28-06-2017': 5.750255, '29-06-2017': 5.750835, '30-06-2017': 5.751414,
# '01-07-2017': 5.751994, '02-07-2017': 5.752574, '03-07-2017': 5.753154, '04-07-2017': 5.753734,
# '05-07-2017': 5.754315, '06-07-2017': 5.754895, '07-07-2017': 5.755475, '08-07-2017': 5.756055,
# '09-07-2017': 5.756636, '10-07-2017': 5.757216, '11-07-2017': 5.757347, '12-07-2017': 5.757477,
# '13-07-2017': 5.757608, '14-07-2017': 5.757739, '15-07-2017': 5.757869, '16-07-2017': 5.758,
# '17-07-2017': 5.75813, '18-07-2017': 5.758261, '19-07-2017': 5.758391, '20-07-2017': 5.758522,
# '21-07-2017': 5.758653, '22-07-2017': 5.758783, '23-07-2017': 5.758914, '24-07-2017': 5.759044}

getUDIS("29/04/2017", "24/04/2017")
# Returns: {}
```

### getCCP()
```py
getCCP(startDate, endDate = '0', tipo = 'none')
```

The function expects one to three string parameters, the first two in the format `"dd/mm/yyyy"`, the last in the type of CCP rate[^2], it will return a dictionary with the *'key'* being the date as a `string`, and the *'value'* the CCP rate as a `float`. If no CCP rate is found in the date or range of dates provided, the function will return an empty dictionary.

You can call it with only the start date `startDate` which will return the CCP rate of that date if there is any, or call it with a start date `startDate` and end date `endDate`. Be aware if the end date is before the start date the function will return an empty dictionary.

```py
getCCP("25/04/2017")
# Returns: {'25-04-2017': 5.6}

getCCP("24/04/2017", "24/07/2017")
# Returns:
# {'25-04-2017': 5.6, '25-05-2017': 5.74, '26-06-2017': 5.9}

getCCP("24/04/2017", "24/07/2017",'usd')
# Returns:
# {'12-05-2017': 4.1, '12-06-2017': 4.01, '12-07-2017': 3.98}

getCCP("24/04/2017", "24/07/2017",'udis')
# Returns:
# {'25-04-2017': 4.48, '25-05-2017': 4.48, '26-06-2017': 4.48}

getCCP("29/04/2017", "24/04/2017")
# Returns: {}
```

### getTIICdep()
```py
getTIICdep(startDate, endDate = '0', period = '60')
```

The function expects one to three string parameters, the first two in the format `"dd/mm/yyyy"`, the last in the period of TIIC Deposits rate[^3], it will return a dictionary with the *'key'* being the date as a `string`, and the *'value'* the TIIC rate as a `float`. If no TIIC rate is found in the date or range of dates provided, the function will return an empty dictionary.

You can call it with only the start date `startDate` which will return the TIIC rate of that date if there is any, or call it with a start date `startDate` and end date `endDate`. Be aware if the end date is before the start date the function will return an empty dictionary.

```py
getTIICdep("25/04/2006")
# Returns: {'25-04-2006': 3.29}

getTIICdep("24/04/2006", "24/07/2006", '90')
# Returns:
# {'24-04-2006': 3.24, '25-04-2006': 3.24, '26-04-2006': 3.24, '27-04-2006': 3.24, '28-04-2006': 3.23,
#  '02-05-2006': 3.23, '03-05-2006': 3.23, '04-05-2006': 3.23, '05-05-2006': 3.23, '08-05-2006': 3.23,
#  '09-05-2006': 3.23, '10-05-2006': 3.23, '11-05-2006': 3.23, '12-05-2006': 3.23, '15-05-2006': 3.23,
#  '16-05-2006': 3.23, '17-05-2006': 3.23, '18-05-2006': 3.23, '19-05-2006': 3.23, '22-05-2006': 3.23,
#  '23-05-2006': 3.23, '24-05-2006': 3.23, '25-05-2006': 3.23, '26-05-2006': 3.23, '29-05-2006': 3.23,
#  '30-05-2006': 3.23, '31-05-2006': 3.23, '01-06-2006': 3.23, '02-06-2006': 3.23, '05-06-2006': 3.23,
#  '06-06-2006': 3.23, '07-06-2006': 3.23, '08-06-2006': 3.23, '09-06-2006': 3.23, '12-06-2006': 3.23,
#  '13-06-2006': 3.23, '14-06-2006': 3.23, '15-06-2006': 3.23, '16-06-2006': 3.23, '19-06-2006': 3.12,
#  '20-06-2006': 3.12, '21-06-2006': 3.12, '22-06-2006': 3.12, '23-06-2006': 3.12, '26-06-2006': 3.12,
#  '27-06-2006': 3.12, '28-06-2006': 3.11, '29-06-2006': 3.11, '30-06-2006': 3.11, '03-07-2006': 3.11,
#  '04-07-2006': 3.11, '05-07-2006': 3.11, '06-07-2006': 3.11, '07-07-2006': 3.09, '10-07-2006': 3.09,
#  '11-07-2006': 3.09, '12-07-2006': 3.09, '13-07-2006': 3.09, '14-07-2006': 3.09, '17-07-2006': 3.09,
#  '18-07-2006': 3.09, '19-07-2006': 3.09, '20-07-2006': 3.09, '21-07-2006': 3.09, '24-07-2006': 3.09}

getTIICdep("24/04/2006", "24/07/2006", '180')
# Returns:
# {'24-04-2006': 3.26, '25-04-2006': 3.26, '26-04-2006': 3.26, '27-04-2006': 3.26, '28-04-2006': 3.21,
#  '02-05-2006': 3.21, '03-05-2006': 3.21, '04-05-2006': 3.21, '05-05-2006': 3.19, '08-05-2006': 3.19,
#  '09-05-2006': 3.19, '10-05-2006': 3.19, '11-05-2006': 3.19, '12-05-2006': 3.19, '15-05-2006': 3.19,
#  '16-05-2006': 3.19, '17-05-2006': 3.19, '18-05-2006': 3.19, '19-05-2006': 3.19, '22-05-2006': 3.19,
#  '23-05-2006': 3.19, '24-05-2006': 3.19, '25-05-2006': 3.19, '26-05-2006': 3.19, '29-05-2006': 3.19,
#  '30-05-2006': 3.19, '31-05-2006': 3.19, '01-06-2006': 3.19, '02-06-2006': 3.19, '05-06-2006': 3.19,
#  '06-06-2006': 3.19, '07-06-2006': 3.19, '08-06-2006': 3.19, '09-06-2006': 3.19, '12-06-2006': 3.19,
#  '13-06-2006': 3.19, '14-06-2006': 3.19, '15-06-2006': 3.19, '16-06-2006': 3.19, '19-06-2006': 3.19,
#  '20-06-2006': 3.19, '21-06-2006': 3.19, '22-06-2006': 3.19, '23-06-2006': 3.19, '26-06-2006': 3.19,
#  '27-06-2006': 3.19, '28-06-2006': 3.17, '29-06-2006': 3.17, '30-06-2006': 3.17, '03-07-2006': 3.17,
#  '04-07-2006': 3.17, '05-07-2006': 3.17, '06-07-2006': 3.17, '07-07-2006': 3.17, '10-07-2006': 3.17,
#  '11-07-2006': 3.17, '12-07-2006': 3.17, '13-07-2006': 3.17, '14-07-2006': 3.17, '17-07-2006': 3.17,
#  '18-07-2006': 3.17, '19-07-2006': 3.17, '20-07-2006': 3.17, '21-07-2006': 3.17, '24-07-2006': 3.17}

getTIICdep("29/04/2017", "24/04/2017")
# Returns: {}
```

### getTIICpag()
```py
getTIICpag(startDate, endDate = '0', period = '28')
```

The function expects one to three string parameters, the first two in the format `"dd/mm/yyyy"`, the last in the period of TIIC Promissory note rate[^4], it will return a dictionary with the *'key'* being the date as a `string`, and the *'value'* the TIIC rate as a `float`. If no TIIC rate is found in the date or range of dates provided, the function will return an empty dictionary.

You can call it with only the start date `startDate` which will return the TIIC rate of that date if there is any, or call it with a start date `startDate` and end date `endDate`. Be aware if the end date is before the start date the function will return an empty dictionary.

```py
getTIICpag("25/04/2006")
# Returns: {'25-04-2006': 2.65}

getTIICpag("24/04/2006", "24/07/2006")
# Returns:
# {'24-04-2006': 2.65, '25-04-2006': 2.65, '26-04-2006': 2.65, '27-04-2006': 2.65, '28-04-2006': 2.56,
#  '02-05-2006': 2.56, '03-05-2006': 2.56, '04-05-2006': 2.56, '05-05-2006': 2.56, '08-05-2006': 2.56,
#  '09-05-2006': 2.56, '10-05-2006': 2.56, '11-05-2006': 2.56, '12-05-2006': 2.54, '15-05-2006': 2.54,
#  '16-05-2006': 2.54, '17-05-2006': 2.54, '18-05-2006': 2.54, '19-05-2006': 2.54, '22-05-2006': 2.54,
#  '23-05-2006': 2.54, '24-05-2006': 2.54, '25-05-2006': 2.54, '26-05-2006': 2.51, '29-05-2006': 2.51,
#  '30-05-2006': 2.51, '31-05-2006': 2.51, '01-06-2006': 2.51, '02-06-2006': 2.51, '05-06-2006': 2.51,
#  '06-06-2006': 2.51, '07-06-2006': 2.51, '08-06-2006': 2.51, '09-06-2006': 2.47, '12-06-2006': 2.47,
#  '13-06-2006': 2.47, '14-06-2006': 2.47, '15-06-2006': 2.47, '16-06-2006': 2.47, '19-06-2006': 2.47,
#  '20-06-2006': 2.47, '21-06-2006': 2.47, '22-06-2006': 2.47, '23-06-2006': 2.47, '26-06-2006': 2.47,
#  '27-06-2006': 2.47, '28-06-2006': 2.47, '29-06-2006': 2.47, '30-06-2006': 2.47, '03-07-2006': 2.47,
#  '04-07-2006': 2.47, '05-07-2006': 2.47, '06-07-2006': 2.47, '07-07-2006': 2.47, '10-07-2006': 2.46,
#  '11-07-2006': 2.46, '12-07-2006': 2.46, '13-07-2006': 2.46, '14-07-2006': 2.46, '17-07-2006': 2.46,
#  '18-07-2006': 2.46, '19-07-2006': 2.46, '20-07-2006': 2.46, '21-07-2006': 2.42, '24-07-2006': 2.42}

getTIICpag("24/04/2006", "24/07/2006", '182')
# Returns:
# {'24-04-2006': 3.36, '25-04-2006': 3.36, '26-04-2006': 3.36, '27-04-2006': 3.36, '28-04-2006': 3.28,
#  '02-05-2006': 3.28, '03-05-2006': 3.28, '04-05-2006': 3.28, '05-05-2006': 3.28, '08-05-2006': 3.28,
#  '09-05-2006': 3.28, '10-05-2006': 3.28, '11-05-2006': 3.28, '12-05-2006': 3.25, '15-05-2006': 3.25,
#  '16-05-2006': 3.25, '17-05-2006': 3.25, '18-05-2006': 3.25, '19-05-2006': 3.25, '22-05-2006': 3.25,
#  '23-05-2006': 3.25, '24-05-2006': 3.25, '25-05-2006': 3.25, '26-05-2006': 3.23, '29-05-2006': 3.23,
#  '30-05-2006': 3.23, '31-05-2006': 3.23, '01-06-2006': 3.23, '02-06-2006': 3.24, '05-06-2006': 3.24,
#  '06-06-2006': 3.24, '07-06-2006': 3.24, '08-06-2006': 3.24, '09-06-2006': 3.21, '12-06-2006': 3.21,
#  '13-06-2006': 3.21, '14-06-2006': 3.21, '15-06-2006': 3.21, '16-06-2006': 3.22, '19-06-2006': 3.22,
#  '20-06-2006': 3.22, '21-06-2006': 3.22, '22-06-2006': 3.22, '23-06-2006': 3.23, '26-06-2006': 3.23,
#  '27-06-2006': 3.23, '28-06-2006': 3.23, '29-06-2006': 3.23, '30-06-2006': 3.2, '03-07-2006': 3.2,
#  '04-07-2006': 3.2, '05-07-2006': 3.2, '06-07-2006': 3.2, '07-07-2006': 3.16, '10-07-2006': 3.13,
#  '11-07-2006': 3.13, '12-07-2006': 3.13, '13-07-2006': 3.13, '14-07-2006': 3.13, '17-07-2006': 3.13,
#  '18-07-2006': 3.13, '19-07-2006': 3.13, '20-07-2006': 3.13, '21-07-2006': 3.11, '24-07-2006': 3.11}

getTIICpag("29/04/2017", "24/04/2017")
# Returns: {}
```

### getTIIE()
```py
getTIIE(startDate, endDate = '0', period = '28')
```

The function expects one to three string parameters, the first two in the format `"dd/mm/yyyy"`, the last in the period of TIIE rate[^5], it will return a dictionary with the *'key'* being the date as a `string`, and the *'value'* the TIIE rate as a `float`. If no TIIE rate is found in the date or range of dates provided, the function will return an empty dictionary.

You can call it with only the start date `startDate` which will return the TIIE rate of that date if there is any, or call it with a start date `startDate` and end date `endDate`. Be aware if the end date is before the start date the function will return an empty dictionary.

```py
getTIIE("05/03/2021")
# Returns: {'05-03-2021': 4.2825}

getTIIE("01/01/2021","10/02/2025",'27')
# Returns:
# {'04-03-2021': 4.2825, '19-08-2021': 4.755, '05-10-2021': 4.9825, '17-03-2022': 6.2523,
#  '19-08-2022': 8.7728, '05-10-2022': 9.5453, '09-03-2023': 11.2962, '22-03-2023': 11.02,
#  '05-10-2023': 11.4983, '14-11-2023': 11.5064, '03-04-2024': 11.2475, '03-09-2024': 10.9976,
#  '14-11-2024': 10.6825, '27-11-2024': 10.485, '04-12-2024': 10.4663}

getTIIE("01/01/2021","10/02/2025",'181')
# Returns:
# {'18-03-2021': 4.2505, '13-10-2021': 5.3162, '06-10-2022': 10.2682, '04-05-2023': 11.9135,
#  '28-09-2023': 11.509, '01-11-2023': 11.525, '02-04-2024': 11.6555, '13-06-2024': 11.5498,
#  '26-06-2024': 11.5498, '03-07-2024': 11.6344, '31-10-2024': 11.0642}

getTIIE("29/04/2017", "24/04/2017")
# Returns: {}
```


## List of indicators

|  Indicator  |          Description          |
|    :----:   |              ----             |
|    '158'    |  Exchange rate of MXN to USD  |
|    '159'    |  UDIS                         |
|    '160'    |  CCP                          |
|    '161'    |  CCP-UDIS                     |
|    '162'    |  CPP                          |
|    '163'    |  CCP-USD                      |
|    '165'    |  TIIE 28 DIAS                 |
|    '166'    |  TIIE 91 DIAS                 |
|    '167'    |  TIIC DEPOSITOS 60 DIAS       |
|    '168'    |  TIIC DEPOSITOS 90 DIAS       |
|    '169'    |  TIIC DEPOSITOS 180 DIAS      |
|    '170'    |  TIIC PAGARES 28 DIAS         |
|    '171'    |  TIIC PAGARES 91 DIAS         |
|    '172'    |  TIIC PAGARES 182 DIAS        |
|    '174'    |  TIIE 182 DIAS                |
|    '175'    |  TIIE DE FONDEO               |
|    '176'    |  TIIE 90 DIAS                 |
|    '177'    |  TIIE 29 DIAS                 |
|    '178'    |  TIIE 27 DIAS                 |
|    '179'    |  TIIE 26 DIAS                 |
|    '180'    |  TIIE 181 DIAS                |
|    '181'    |  TIIE 92 DIAS                 |
|    '182'    |  TIIE 89 DIAS                 |
|    '183'    |  TIIE 183 DIAS                |
|    '184'    |  TIIE 180 DIAS                |

## List of CCP Types
|  Parameter  | Description |  Indicator  |
|   :----:    |    ----     |    :----:   |
|   'none'    |  CCP        |    '160'    |
|   'udis'    |  CCP-UDIS   |    '161'    |
|    'usd'    |  CCP-USD    |    '163'    |

## List of TIIC Periods
### TICC Deposits Periods
|   Period    |         Description       |  Indicator  |
|   :----:    |           ----            |    :----:   |
|    '60'     |  TIIC DEPOSITOS 60 DIAS   |    '167'    |
|    '90'     |  TIIC DEPOSITOS 90 DIAS   |    '168'    |
|    '180'    |  TIIC DEPOSITOS 180 DIAS  |    '169'    |

### TICC Promissory note Periods
|   Period    |        Description      |  Indicator  |
|   :----:    |          ----           |    :----:   |
|    '28'     |  TIIC PAGARES 28 DIAS   |    '170'    |
|    '91'     |  TIIC PAGARES 91 DIAS   |    '171'    |
|    '182'    |  TIIC PAGARES 182 DIAS  |    '172'    |

## List of TIIE Periods
|   Period    |   Description    |  Indicator  |
|   :----:    |       ----       |    :----:   |
|   'none'    |  TIIE FONDEO     |    '175'    |
|    '26'     |  TIIE 26 DIAS    |    '179'    |
|    '27'     |  TIIE 27 DIAS    |    '178'    |
|    '28'     |  TIIE 28 DIAS    |    '165'    |
|    '29'     |  TIIE 29 DIAS    |    '177'    |
|    '89'     |  TIIE 89 DIAS    |    '182'    |
|    '90'     |  TIIE 90 DIAS    |    '176'    |
|    '91'     |  TIIE 91 DIAS    |    '166'    |
|    '92'     |  TIIE 92 DIAS    |    '181'    |
|    '180'    |  TIIE 180 DIAS   |    '184'    |
|    '181'    |  TIIE 181 DIAS   |    '180'    |
|    '182'    |  TIIE 182 DIAS   |    '174'    |
|    '183'    |  TIIE 183 DIAS   |    '183'    |

[^1]: [See list of indicators](https://github.com/IsaacMartinezPeraza/mexico-dof-indicators?tab=readme-ov-file#list-of-indicators)
[^2]: [See list of CCP types](https://github.com/IsaacMartinezPeraza/mexico-dof-indicators?tab=readme-ov-file#list-of-CCP-Types)
[^3]: [See list of TIIC Deposits Periods](https://github.com/IsaacMartinezPeraza/mexico-dof-indicators?tab=readme-ov-file#ticc-deposits-periods)
[^4]: [See list of TIIC Promissory note Periods](https://github.com/IsaacMartinezPeraza/mexico-dof-indicators?tab=readme-ov-file#ticc-promissory-note-periods)
[^5]: [See list of TIIE Periods](https://github.com/IsaacMartinezPeraza/mexico-dof-indicators?tab=readme-ov-file#list-of-TIIE-Periods)
