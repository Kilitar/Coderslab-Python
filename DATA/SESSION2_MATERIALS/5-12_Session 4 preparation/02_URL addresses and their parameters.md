# URL addresses and their parameters

Type: Article

Every website (and, as we learned earlier, external APIs) is located at some web address. In this article we will learn how these addresses are constructed.

## URL components

What a URL consists of will be best described by example:

**http://host.name.eu:80/directory/index.html?param1=value1&param2=value2**

Elements of URL address:

1. `http://` or `https://` - the protocol we use. `https` is encrypted `http`.
2. `host.name.eu` - domain name that uniquely identifies our server.
3. `:80` - number of the server port we connect to. `80` is the default port number for `http`, and `443` is the default for `https`.
4. `/directory/index.html` - path to a file on the server. Currently, access paths are generated artificially and do not reflect real directories on the server. Usually the file name is not there either. This is done for the sake of better positioning of such a page by search engines.
5. `?param1=value1&param2=value2` - **querystring**: additional parameters we send to the server. They start from the `?` character and are separated with `&`. Nowadays, passing parameters in this form is very rare. Instead, the path from para. 4 is used (due to better positioning of such a page by search engines).

Another example of URL address:

**https://host.name.eu/article/2010/12/identifier**

Here, the path **/article/2010/12/identifier** does not point to a file on the server - instead, it points to the resource (article) in a search engine-friendly way. The article identifier here is the **2010/12/identifier** part.

A querystring can still occur in such an address, for example, to provide additional statistical information about where the user came to the site from:

**https://host.name.eu/article/2010/12/identifier?ref=newsletter**

## Sample Addresses

- **https://wynter.com/post/what-is-positioning/**
- **https://en.wikipedia.org/wiki/Raegma**
- **https://www.google.com/search?source=hp&q=google**

## Summary

A good knowledge of URL structure is crucial for web scraping; it will be discussed in the next class. For the same purpose, in addition to knowing address structure, intuition matters, and it comes with experience.
