# Exercise 1

Type: Exercise

## Exercise 1

Register on [openweathermap.org](https://openweathermap.org/) if you haven't done it yet. Remember to confirm the email address.

Copy your key from [home.openweathermap.org/api_keys](https://home.openweathermap.org/api_keys) and put it in the `APIKEY` variable below.

Once the key is active, the following code should display the current weather in London (the same code is prepared in the Jupyter file for this task):

``` 
import requests

# Edit here!
APIKEY = '...'

response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=London&appid={APIKEY}')

if response.status_code == 401:
    print('Incorrect or inactive key: key activation takes between 10 minutes and 2 hours!')
elif response.status_code == 200:
    print('Weather in London:', response.json()['weather'][0]['main'])
else:
    print('We are not ready to handle this response code!')
```
