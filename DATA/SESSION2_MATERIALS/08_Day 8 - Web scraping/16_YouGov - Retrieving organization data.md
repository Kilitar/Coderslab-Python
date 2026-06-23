# YouGov - Retrieving organization data

Type: Exercise

# Exercise description

Based on the conclusions from the previous exercise, in this notebook we will focus on retrieving the data available for [Macmillan cancer support](https://yougov.co.uk/topics/health/explore/not-for-profit/Macmillan_Cancer_Support?content=all). To do this, complete the implementation of the `get_organization_detailed_data(url)` method to retrieve the following data:

- from page header (next to the logo):
  
  - fame
  - popularity
  - disliked by
  - neutral

The data should be returned as a dictionary with the following structure:

``` python
{
    'Fame': '0%',
    'Popularity': '0%',
    'Disliked by': '0%',
    'Neutral': '0%'
}
```

### Hint

- In this exercise focus only on retrieving the information for a single page - this one. In the next part we will retrieve the information for all organizations.
- Just like earlier, you need to accept cookies here because the browser has been reopened - maybe it's a good idea to separate this element? (optional)
- Because it is necessary to accept the cookies for each attempt, remember to close the browser earlier.
