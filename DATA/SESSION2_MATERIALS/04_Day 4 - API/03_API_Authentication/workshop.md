# Workshop

Type: Exercise

# Description

The aim of the workshop is to consolidate information on what APIs are and how to work with them.

We are going to retrieve the data about selected artist's albums and songs. Later, the data should be presented as a report.

Using the `input` function we will ask the user about the name of their favorite band. Next, we will:

1. retrieve the albums available for the given artist,
2. for the albums, retrieve the list of available songs,
3. retrieve the data for these songs,
4. create a report with the collected information (detailed specification below).

To do steps 1-3 we are going to use a dedicated API, created for this purpose, and documented [here](https://api-pad.coderslab.com/docs). The API is available at: [click](https://api-pad.coderslab.com/docs); to authenticate use the key: `Ft85HgGtY6Rt`.

> It is possible to do this using a multiple-level nested loop but, to keep the code readable, we advise against it. For each of the points above try to create a dedicated function first, and then use them to generate the result in a clean and readable way.

### Note

> Some endpoints require a dictionary to be passed in the `body`; read this [thread](https://stackoverflow.com/questions/9733638/how-to-post-json-data-with-python-requests), to find out how to pass a dictionary to an endpoint.

## API Documentation

API documentation has been created with [swagger](https://swagger.io/); before we start coding, together with the lecturer we're going to discuss its elements such as: endpoints, methods, authentication, etc.

The documentation website also includes the key information on how to use it.

## Report

For the chosen artist we should get a report that displays information about their albums and songs in each of them. It should be structured as a directory. For example, if we search for `metallica` the report should look like:

``` 
Artist: metallica
|___ Album: Master Of Puppets
    |___ Tracklist:
          1. battery (remastered): Playcount: 393621 | Listeners: 62346 | Duration: 0 | Topic: sadness
          ....
```

A report like this one should be displayed at the end of the script execution.

## Report in the `csv` file format (optional)

Based on the retrieved data we also want to create and save a `csv` file with the following specification:

- encoding `UTF-8`,
- separator `|`,
- output file name: `{artist}.csv`
- file heading: `"artist", "album", "track", "listeners", "likes", "duration", "topic"`

## Retrieving entire available database (optional)

In the materials there is an `artists.csv` file, with the list of artists available in the API. Modify your script so that it reads the file and for every artist retrieves available data and creates a dedicated `csv` file.

The solution should be based on the one you create when working with one artist.

## Hint

To generate a report displayed in the notebook you can use the following template for the song.

``` python
msg_template = ("{nb}. {track_name}: " 
                "Playcount: {playcount} | "
                "Listeners: {listeners} | "
                "Duration: {duration} | "
                "Topic: {topic}"
                )
```

You can use the `msg_template.format(...)` to build the report.
