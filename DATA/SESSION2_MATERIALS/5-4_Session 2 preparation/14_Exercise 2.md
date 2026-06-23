# Exercise 2

Type: Exercise

## Exercise 2

Register on [exchangeratesapi.io](https://exchangeratesapi.io/) if you have not done it yet. After registration copy your key and put it in the `APIKEY` variable below.

Install the `requests` library - we will use it to communicate with the API for reading latest currency exchange rates.

Once the key is active, the following code should display the EURAUD exchange rate.

``` 
import requests

# Edit here!
APIKEY = '...'

response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=London&appid={APIKEY}')

response = requests.get(f'http://api.exchangeratesapi.io/latest?access_key={APIKEY}')

if response.json()['success']:
    print('EURAUD rate is currently', response.json()['rates']['AUD'])
else:
    print('Error:', response.json()['error']['info'])
```
