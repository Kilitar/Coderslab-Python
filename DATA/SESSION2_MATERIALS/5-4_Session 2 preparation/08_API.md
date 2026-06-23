# API

Type: Article

From this article you will learn what an API is, how you can work with it, its authentication capabilities, and its advantage over retrieving information from a file.

## GUI First

Surely you know what a GUI (Graphical User Interface) is - this is the interface that an application presents to a human to communicate with it. The data made available to a human is clearly formatted, relevant sections highlighted, and links and buttons are used for interaction.

People love working with GUIs, but programs don't need all these decorations - programs want to get clean data, in the simplest form possible, with clearly defined rules for retrieving and changing it. Since GUI is for people, we need a separate interface for applications.

## API

An API is an interface that allows an application (or a script that analyzes data) to communicate with another application (e.g., a server containing current exchange rates, weather, etc.). Communication consists in an application (our script) making a request to the specified server address (e.g. [https://api.exchangeratesapi.io/latest?base=PLN](https://api.exchangeratesapi.io/latest?base=PLN)), and in response the server returns the data in a certain format (e.g, JSON or XML – you will be reading more about them in the next articles).

The data itself has a well-defined structure, which can be learned by reading the documentation of a given API. Sometimes a glance at the server's response is enough to understand what to expect in reply to a given type of query.

When possible, we should rely on APIs instead of file data. It just makes more sense: APIs can return the most up-to-date data that only the server has access to. And files always have the same content - they are as up-to-date as the conscientious person who updates them.

## API architecture

In the case of APIs based on the HTTP protocol (and other one we are not going to discuss in this article), we are dealing with the **client-server** architecture. The client in our case will be a script (run by Python or Jupyter). The server should always be available - it does not connect to anyone by itself, it only waits until it the clients connect to it.

Using the `requests` library (it should be already installed) the script makes a **request** to the server. A query always consists of:

- methods: `GET`, `POST`, `PUT`, `DELETE`... conventionally the `GET` method is used for reading,
- address: also called an endpoint - you will read about it later in the article,
- headers: data that describe in more detail the client itself, the data sent in the request, expectations about the data that the server will return,
- data: (for the methods that require them): if the query causes some permanent changes to the server (for example, booking a room in a hotel), the details of this query will be in this section.

The server then returns a response that consists of:

- response status: `200 OK` means that the request was successful, and `404 NOT FOUND` suggests an error connected with the address the request was sent to. [Full list of possible statuses](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- headers: this time they describe the details of the server and the data returned (their format, how long the response remains valid, etc.)
- data: the content requested by the client; sometimes the response will not contain data, e.g. in response to the request to delete something – in that case the confirmation `204 NO CONTENT` is enough.

Sample request for current exchange rates, along with the display of the response:

``` python
import requests

response = requests.get('https://api.exchangeratesapi.io/latest')

print('Status:', response.status_code)
print('Full response content:', response.json())
print('GBP/EUR rate:', response.json()['rates']['GBP'])
print('Response format:', response.headers['Content-Type'])
```

Result:

``` 
Status: 200
Full response content: {'rates': {'CAD': 1.5307, ... 'MYR': 4.8844}, 'base': 'EUR', 'date': '2021-02-18'}
GBP/EUR rate: 0.8654
Response format: application/json
```

The example above illustrated the use of the `GET` method – used to read data. Methods used for modification include: `POST` and `PUT`, and to remove resources: `DELETE`.

## Endpoints

Endpoints are a feature of practically all APIs based on the HTTP protocol (it is the most popular type of API). Simply separate addresses, where different functionalities and data are available - under one address you can find current exchange rates:[/latest](https://api.exchangeratesapi.io/latest), and historical data at: [/history](https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-01-04).

The example above passes additional data to the `/history` endpoint. It does it with a  **querystring**, i.e. the part of address after the `?` character. A querystring always is a set of key=value pairs, separated with `&` characters if there is more than one pair. What if we want to use characters that have a special meaning in the key, or (much more often) in the value? Querystring `?name=Tom & Jerry` gets misinterpreted – "Tom" is the value of the "name" field, and "Jerry" the next key? And where is its value?

In such case, the `urllib.parse` module comes in handy. In it, we will find the `urlencode` function that takes a dictionary and returns a correctly encoded querystring:

``` python
import urllib.parse
print(urllib.parse.urlencode({"name": "Tom & Jerry"}))
```

Result:

``` 
name=Tom+%26+Jerry
```

## Authorization

Not all APIs allow reading data without any restrictions, and APIs that allow modifying their data are almost non-existent.

There are various ways to authenticate and authorize queries to a given API. One of the most popular is the use of a key (a text only the application owner has). Such a key is usually given as a header:

``` python
requests.get('https://moje-api.com/endpoint', headers={'Authorization': 'Token MY-S3CR3T-K3Y'})
```

less often as part of the address:

``` python
requests.get('https://moje-api.com/endpoint?apikey=MY-S3CR3T-K3Y'})
```

There is no one specific way to obtain such keys - it is an individual issue for each API. Sometimes keys will be given out to anyone who goes to the site, sometimes registration and confirmation of the email address will be required, sometimes contact with a representative of the company that owns the API....

## Summary

Different servers provide different APIs, and each API we must first learn from scratch: you'll encounter different addresses and data structures on a server that allows you to trade stocks on the stock market, others on a server that books hotel rooms, and still others on the server of a company that collects data about your health and suggests exercise and diet. Fortunately, there are some common elements (such as using JSON to pass data and GET methods to read it) that make it easier to get started with each of them.

You can find a list of interesting and public APIs [here](https://github.com/public-apis/public-apis).
