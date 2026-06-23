# YouGov - 1_Retrieving organizations list

Type: Exercise

# Exercise description

Based on the conclusions of the previous exercise, in this part we are going to focus on retrieving the list of the first 20 organizations visible on the page. At the end of the script we should get a list with the information about the organization name and its url, according to the example below:

``` python
[
 {'name': 'NSPCC',
  'link': 'https://yougov.co.uk/topics/health/explore/not-for-profit/NSPCC'},
 {'name': 'Prostate Cancer UK',
  'link': 'https://yougov.co.uk/topics/health/explore/not-for-profit/Prostate_Cancer_UK'},
 {'name': 'British Red Cross', ...}
 ...
]
```

# List of steps

To complete this exercise you need to do the following:

- import appropriate libraries in the notebook,
- complete the implementation of the `get_organization_list()` method - the function responsible for retrieving and generating the data we're interested in.

## Hints

- for the page to finish loading you need to **accept** cookies, otherwise it does not fully load,
- remember to set `implicitly_wait(s)` when going to the page,
- apart from setting `implicitly_wait` it is also good to add `sleep(1)` from the built-in `time` library before searching for the required page element,
- remember to close the browser at the end of the script,
- main page  link:

``` python
url = 'https://yougov.co.uk/ratings/politics/popularity/charities-organisations/all'
```
