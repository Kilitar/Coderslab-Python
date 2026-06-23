# What web scraping is

Type: Article

In previous classes, we learned how to retrieve data from websites using their APIs. Not every site is equipped with such an API; many of them were created with the assumption that only humans would be the recipients of their content. This doesn't mean that it's impossible to retrieve this content using Python - you just need to use other tools.

WebScraping is a technique for downloading and extracting information from websites. It consists in retrieving the contents of a website (for instance using the `requests` library you already know), transforming it (retrieved content is one long string) into a structure that is easier to search through, and extract the needed information from. Sometimes we will additionally pull out links to know the next pages to be processed.

## Is this legal?

Scraping data from a website is legal. So is using a web browser to browse it.

The problem arises when a program written in Python fetches this data at a high frequency, so that the server is under a heavy load. This can be treated as an attack on the site. That is why learning the `sleep(time_in_seconds)` function from the `time` module is useful. It allows you to put the program execution to sleep for a certain amount of time between queries, so that we will not "attack" the site:

``` python
import time

time.sleep(5)
```

The above code will stop program execution for 5 seconds.

## Why web scraping is difficult

Compared to retrieving data via API, web scraping has some very significant drawbacks, making it reasonable to retrieve data this way only if it is impossible to retrieve it otherwise.

### You need to know the structure of the site well

There is no way to count on getting any documentation. We have to pick out for ourselves what the links look like, how the content of the site is laid out, and how to get to the sections that interest us. From time to time, we will have to make more of an effort to make our script look human (!) from the server's point of view, since the site is intended for human browsing - so we will have to take care of passing cookies or sending forms.

### The data in the page content is not as structured as in the API.

The content of a page in HTML is subordinate to how the page should look. If the page creator has chosen an unconventional way to present the information, we will have to spend more time to make sense out of the page content.

### The site may change without warning

The author of the site does not guarantee that the site will always look the way it does. On the contrary, if the site is developing then it will change its structure very often. People adapt to such changes almost immediately and it is not a problem for them. Unfortunately, if our script relied on the fact that an element has an amaranth color, and the author changed it to crimson, then finding this element by color will fail. In practice, it is also impossible to predict what changes to expect in order to prepare the script for them in advance - rather, you have to accept the fact that from time to time the script will stop working and will need corrections.

### The site may be dynamic

JavaScript may be involved in the retrieval of data. Such a page does not have information in its content, it only attaches a JavaScript script that fetches this content with a separate query. If this is the case, then there is a good chance that the site does have its API after all, it just doesn't announce this fact to everyone. If we can draw some conclusions based on observation of queries and responses, we can use such an API - if not, we have to use yet another tool to interact with such a site: Selenium. You will find out more about it from the following articles and presentations.
