# Wrocław city bikes

Type: Exercise

In the file **Ride_history.csv** you will find data on the rentals of Wroclaw City Bicycles - you can find current data with column names in Polish [here](https://www.wroclaw.pl/open-data/dataset/wrmprzejazdy_data). If you have problems with Polish letters, the file is using "Windows-1250" encoding.

Read the data from the file, and then select only those where the rental and return stations are the same and the rentals are shorter than 100 minutes. Show on the graph how many rentals of a given duration there were (first bar: rentals with a duration of one minute, the second - two minutes, etc.).

Rentals that start and end at the same station and last no more than three minutes are probably rentals of defective bikes, which the users return as soon as they realize the problem. Draw a red line that separates rentals shorter and longer than 3 minutes.

Also give it an annotation explaining what this line is.
