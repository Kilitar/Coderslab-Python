# Age table

Type: Exercise

In the file **wpb_votes_list_2019.csv** you will find data about the votes within the Wroclaw Citizens' Budget, downloaded from the page [Wrocław Open Data](https://www.wroclaw.pl/open-data/dataset/wroclawski-budzet-obywatelski-glosowanie).

Read this data and filter it to get the following series:

1. Women under the age of 100.
2. Men under the age of 100.

Next, draw a cumulative plot showing how many people of a given age voted (broken down by gender).

> **Hint:**
> To generate the plot correctly, you need to ensure that both series are of the same length. To do so, use the `reindex` method with the `fill_value` option:
> `s_reindexed = s.reindex(range(0, 100), fill_value=0)`

After creating the plot, generate a table that displays this data below it. The table with the contents of the cells and the table with the description of the rows, should be generated using a loop:

``` 
cells = []
cellLabels = []
for i in range(0,100):
    cells.append([f'Number of female voters aged f{i}', f'Number of female voters aged f{i}'])
    cellLabels.append(f'aged {i}')
```

(Of course, instead of the captions, the corresponding values should be shown).

Review the options in the [documentation](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.codes) – what parameters can be used to make the table more readable?
