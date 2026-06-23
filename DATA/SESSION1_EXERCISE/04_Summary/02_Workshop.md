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

# Solution

> It is important to understand that each solution that meets the set criteria is correct; the one presented here is just an example. It also aims to demonstrate the process of building Python applications directly based on connections with external services.

This is how we will create our solution.

1. We are going to use a specific example and based on it create a solution *mockup*,
2. Based on the previous step, we will create the actual, working solution.

## Configuring the shared parts of the solution

Regardless of the stage we're on we need to prepare the following:

- import required libraries,
- prepare `constants` such as the API address, key, etc.

### Importing libraries

Because we are going to send requests to API we need the `requests` library. Also notice that the documentation clearly states that we are restricted to 1000 calls/minute: this is where the `sleep` method from the `time` library can help.

``` python
import requests
from time import sleep
```

## Constants

Next, we will define the constants

- `API_KEY`- the key from the exercise instructions,
- `API_URL`- the address of our API,
- `SLEEP` - time in seconds that our code will wait for after executing a request. To be on the safe side, in the notebook we're going to set 950 API calls per minute as the maximum value.

Documentation tells us that authentication is done with the `authorization` parameter. We will write that down too and reuse as needed (`AUTH` constant).

``` python
API_KEY = "Ft85HgGtY6Rt"
API_URL = "https://api-pad.coderslab.com/api"

AUTH = {'authorization': API_KEY}

SLEEP = 60/950  # time is seconds between consecutive requests
```

## Solution mockup

This part of the solution is focused on creating the code used as a basis for our work later. We will be making calls based on specific examples. The steps performed to do so are:

1. Based on a specific artist name we will retrieve their ID,
2. We will retrieve the list of available albums and select one of them,
3. For the selected album, we will retrieve its list of tracks and also select one of them,
4. Eventually we will retrieve the data for the selected track.
  This is going to show us how the API works and make our next steps easier.

In the exercise instructions we have the information to get the artist's name from the user with the `input` function: for now let's skip it and define the artist. We will store their name in the `artist` variable.

``` python
artist = 'metallica'
```

### Retrieving available albums

According to the requirements we are to start by retrieving the albums available for the artist. In the documentation we can check that this data can be retrieved from the `artist/albums` endpoint.

This is the first challenge, making calls to `artist/albums` requires passing `artist_id` that we do not have yet: so far we only passed the name of the band.

To get the `artist_id` we need to use a different endpoint: `artist/find`, that requires using their name in the address: e.g.: `artists/find/metallica` for the artist we're interested in.

Let's test sending this API call first:

``` python
r = requests.get(
    f"{API_URL}/artist/find/{artist}", 
    params=AUTH,
)

print(f"Request status: {r.status_code}")
print(f"response: {r.text}")
```

``` 
Request status: 200
Response: {"artist_id":4588}
```

We have received the correct response and the information formatted as a dictionary; to get the `artist_id` we want we need to use the `json()` method and then get the value of the `artist_id` key.

``` python
artist_id = r.json()['artist_id']
```

Let's try one more example: an ID request for a non-existent artist: `coderslaber`. Based on the documentation we expect that the API returns `status_code==204`:

``` python
r = requests.get(
    f"{API_URL}/artist/find/coderslaber", 
    params=AUTH,
)

print(f"Request status: {r.status_code}")
```

``` 
Request status: 204
```

Everything is as expected. We can move on to the next part of the main task: retrieving albums: From the documentation we learn that in this case `artist_id` is passed as the address. We only need a small change in the earlier code:

``` python
r = requests.get(
    f"{API_URL}/artist/albums/{artist_id}",
    params=AUTH,
)

print(f"Request status: {r.status_code}")
print(f"response: {r.text}")
```

``` 
Request status: 200
Response: [{"artist_name":"metallica","album_name":"Master of Puppets (Remastered Deluxe Box Set)","album_id":14991,"artist_id":4588},{"artist_name":"metallica","album_name":"Metallica","album_id":15193,"artist_id":4588},{"artist_name":"metallica","album_name":"Greatest Hits","album_id":15196,"artist_id":4588},
...
"album_name":"Hardwired…To Self-Destruct","album_id":16206,"artist_id":4588}]
```

Based on these results we can see that once again we a received a list of albums (with id and the corresponding name) formatted as `json`, so just like before:

``` python
albums = r.json()
```

Let's also print the data we got:

``` python
for album in albums:
    print(album)
```

``` 
{'artist_name': 'metallica', 'album_name': 'Master of Puppets (Remastered Deluxe Box Set)', 'album_id': 14991, 'artist_id': 4588}
{'artist_name': 'metallica', 'album_name': 'Metallica', 'album_id': 15193, 'artist_id': 4588}
...
{'artist_name': 'metallica', 'album_name': 'Hardwired…To Self-Destruct', 'album_id': 16206, 'artist_id': 4588}
```

This ends exercise 1.

## Retrieving list of songs

The following part is much simpler. Now that we already have the `album_id` it is enough to find in the documentation the endpoint responsible for our current task.

It's important to notice that the data is passed in the `body` in this case: additionally it must be formatted as `json`. Reading the thread from the hint: [click](https://stackoverflow.com/questions/9733638/how-to-post-json-data-with-python-requests), tells us that the information needs to be passed using the `json=...` parameter.

Because `albums` already has several elements let's isolate an example and use it to create a request:

``` python
album = albums[0] # isolate single case
print(f"Album data: {album}")
```

``` 
Album data: {'artist_name': 'metallica', 'album_name': 'Master of Puppets (Remastered Deluxe Box Set)', 'album_id': 14991, 'artist_id': 4588}
```

``` python
album_id = album['album_id']
r = requests.post(
    f"{API_URL}/album/tracks",
    params=AUTH,
    json={'album_id': album_id},
)

print(f"Request status: {r.status_code}")
print(f"Response: {r.text}") # displays IDs of tracks in the album - in this case the list has one element
```

``` 
Request status: 200
Response: [74813]
```

In the response we received another list: this time containing `track ids`. This concludes our work with this part of the exercise.

``` python
tracks = r.json()
```

## Retrieving song data

Now we have all the information we need to retrieve data for a selected track. To do so, get familiar with the `track/get` endpoint documentation.

This case is similar to retrieving the track list information: it is only necessary to change the endpoint address and correctly pass the `track_id` in the `body`.

Just as before let's isolate one track and create a request based in it:

``` python
track_id = tracks[0]
print(f"Track id: {track_id}")
```

``` 
Track id: 74813
```

now the request:

``` python
r = requests.post(
    f"{API_URL}/track/get",
    params=AUTH,
    json={'track_id': track_id}
)
print(f"Request status: {r.status_code}")
print(f"Response: {r.text}")
```

``` 
Request status: 200
Response: {"id":74813,"artist_name":"metallica","track_name":"battery (remastered)","lyrics":"lash action return reaction weak rip tear away hypnotize power crush cower battery stay smash boundaries lunacy stop battery pound aggression turn obsession kill battery kill family battery battery battery lyric commercial","release_date":"1986","len":32,"age":0.48571428571428504,"topic":"sadness","album_name":"Master of Puppets (Remastered Deluxe Box Set)","playcount":393621,"listeners":62346,"duration":0,"album_id":14991,"artist_id":4588}
```

Again, this gives us a dictionary with the data. This time, however, the data concerns a single track and we do not need to retrieve anything else. The information we get includes:

- song title - `track_name`,
- number of times played - `playcount`,
- count of listeners - `listeners`,
- age of listeners - `age`,
- song duration - `duration`,
- song topic- `topic`.

This ends the current part of the workshop.

### Creating the report

Because so far we only created a mockup based on single examples for our requests, let's skip this step for now.

## Summary

In this part we retrieved the data according to the requirements of the exercise. In each case we selected one sample album/song and used them to formulate our requests.

Next we will focus on creating a complete solution for the workshop and preparing the procedures to facilitate executing the entire code.

# Final solution

In this part we are going to finish our solution. We will wrap the code from the earlier steps as functions: this way it will follow the best practices. Based on the API structure, we are going to create the following methods:

- based directly on the API:
  
  - `get_artist_id`, that retrieves artist `id` based on their name,
  - `get_artist_albums`, that returns albums by the artist,
  - `get_album_tracks` - that retrieves a list of tracks on the album,
  - `get_track_data` - that retrieves track information,
- high level methods that combine the above:
  
  - `download_album_tracks` - using `get_album_tracks` and `get_track_data` considering the structure of their results,
  - `download_artist_albums` - as a combination of `get_artist_albums` and `download_album_tracks`.

An important difference is that we need to handle multiple records at a time - earlier we were only working on single records. We will do it with a `for` loop where necessary.

## Generalizing the mockup

In this part we are going to define the methods described earlier. We will implement them starting with the *low* level ones: based on connecting with the API, so we will use the code that was created in the mockup phase. Once this is done, we will move on to the *higher* level methods.

### `get_artist_id`

In order to correctly define the method , we need to ensure that the `status_code` is also handled correctly:

- for `200` or `204`, it is enough to return the value of `artist_id`
- for other cases we are going to return `status_code` handle error, such as: `Unhandled status code: {status_code}`

``` python
def get_artist_id(artist):
    r = requests.get(
        f"{API_URL}/artist/find/{artist}", 
        params=AUTH,
    )
    sleep(SLEEP) # waiting pre-set time after executing the request

    if r.status_code in (200, 204):
        result = r.json()['artist_id']
        return result
    print(f"Unhandled status code: {r.status_code}")
```

### `get_artist_albums`

Again, we need to add `status_code` handling, we will do it in a similar way as earlier. A significant difference is going to be handling many records this time. Because the data will later need to be used in different ways: in other APIs or our final report, the method result in this solution will be structured as follows:

``` python
{0: 'Album A',
 1: 'Album B',
 2: 'Album C'
}
```

This is just a dictionary with album `id` as a key and its name as a value. To achieve this we need to add the following steps:

- create a dictionary to store the mapping of the album key to its name - `albums`,
- from the request result, get `album_id` and `album_name` for each album,
- add these elements to the `albums` variable.

> Why do we want to transform the resulting array into a dictionary? This gives us an easy way to reference each album and retrieve the necessary information. Returning the value directly from the API - that is an array with nested dictionaries, would require filtering in the following steps which could add complication to our solution.

``` python
def get_artist_albums(artist_id):
    r = requests.get(
        f"{API_URL}/artist/albums/{artist_id}",
        params=AUTH,
    )
    sleep(SLEEP) # waiting pre-set time after executing the request

    if r.status_code not in (200, 204):
        print(f"Unhandled status code: {r.status_code}")
        return []

    records = r.json()

    albums = {}  # define an empty array as a container for resulting data
    for record in records:  # iterate all available albums
        album_id = record['album_id']
        album_name = record['album_name']
        albums[album_id] = album_name  # adding new album to the collection
    return albums
```

### `get_album_tracks`

The aim of this function is to retrieve tracks for a specific album. In this part there's no need to additionally modify the output data - it can be returned as is from the API.

``` python
def get_album_tracks(album_id):
    r = requests.post(
        f"{API_URL}/album/tracks",
        params=AUTH,
        json={'album_id': album_id},
    )
    sleep(SLEEP)

    if r.status_code not in (200, 204):
        print(f"Unhandled status code: {r.status_code}")
        return []

    tracks_id = r.json()
    return tracks_id
```

### `get_track_data`

Similarly to the previous point, this function will be just a wrapper for the request:

``` python
def get_track_data(track_id):
    r = requests.post(
        f"{API_URL}/track/get",
        params=AUTH,
        json={'track_id': track_id}
    )
    sleep(SLEEP)

    if r.status_code not in (200, 204):
        print(f"Unhandled status code: {r.status_code}")
        return []
        
    result = r.json()
    return result
```

### `download_album_tracks`

Before we move on to defining the `download_album_tracks` functions let's sum up what we already have:

1. retrieving artist data
2. retrieving artist's available albums
3. retrieving a list of tracks available on an album
4. retrieving data for a single track.

The missing link is connecting steps 3 and 4 to retrieve data of all tracks available on the album: this is what the `download_album_tracks` function is going to handle.

``` python
def download_album_tracks(album_id):
    tracks_id = get_album_tracks(album_id)
    tracks = []

    for track_id in tracks_id:
        data = get_track_data(track_id)
        tracks.append(data)
    return tracks
```

### `download_artist_albums`

As mentioned earlier, this function's job is simply to retrieve the album data of the given artist. That's why it needs to implement the following logic:

- take `artist_id` as an argument,
- retrieve albums available for the artist - we'll use `get_artist_albums` here,
- retrieve data related to an album - here we can use the `download_album_tracks` function defined earlier.

It's worth noting here that from `get_artist_albums` we will get a dictionary. We want to keep this convention and so let's have this method return two variables:

- `albums`- the result of `get_artist_albums`; because it contains mapping the id to the name,
- `albums_tracks` - the list of tracks in an album; its structure is going to be similar to that from `get_artist_albums`:

``` python
{1: [{track data}]}
```

one difference being that the values will be formatted as a list of data on a track

``` python
def download_artist_albums(artist_id):
    albums = get_artist_albums(artist_id)

    albums_tracks = {}
    for id, album in enumerate(albums, 1):
        print(f"Downloading {id} of {len(albums)}")
        tracks = download_album_tracks(album)
        albums_tracks[album] = tracks
    return albums, albums_tracks
```

## Retrieving data for a selected band

Here we're going to create a place that our entire code will get executed from. We'll also add the element that has been missing so far: getting the name of the artist using `input`.

``` python
artist = input('Enter band name')
print(f"Entered band: {artist}")
```

``` 
Entered band: madonna
```

``` python
artist_id = get_artist_id(artist)
albums, tracks = download_artist_albums(artist_id)
```

``` 
Downloading 1 of 10
Downloading 2 of 10
Downloading 3 of 10
Downloading 4 of 10
Downloading 5 of 10
Downloading 6 of 10
Downloading 7 of 10
Downloading 8 of 10
Downloading 9 of 10
Downloading 10 of 10
```

### Previewing data

``` python
albums
```

``` 
{1476: 'Madonna',
 1830: 'Like a Virgin',
 1838: 'Frozen',
 1913: 'True Blue',
 2138: 'Like a Prayer',
 2209: 'The Immaculate Collection',
 2355: 'The Girlie Show: Live Down Under',
 2532: 'Bedtime Stories',
 2773: 'Ray of Light',
 3287: 'The Confessions Tour'}
```

``` python
tracks
```

``` 
{1476: [{'id': 7386,
   'artist_name': 'madonna',
   'track_name': 'holiday',
   'lyrics': 'holiday celebrate holiday celebrate take holiday take time celebrate life nice everybody spread word gonna celebration world nation time good time forget time yeah come release pressure need holiday take holiday take time celebrate life nice turn world bring days trouble time celebrate shine come things better need holiday take holiday take time celebrate life nice holiday celebrate holiday celebrate take holiday take time celebrate life nice holiday celebrate holiday celebrate come nation',
   'release_date': '1979',
   'len': 73,
   'age': 0.5857142857142851,
   'topic': 'world/life',
   'album_name': 'Madonna',
   'playcount': 2310260,
   'listeners': 444332,
   'duration': 241000,
   'album_id': 1476,
   'artist_id': 427},
...
  {'id': 15429,
   'artist_name': 'madonna',
   'track_name': 'hung up',
   'lyrics': 'time go slowly time go slowly time go slowly time go slowly time go slowly time go slowly little thing hang hang wait baby night tire wait time go slowly time hesitate catch know time go slowly time go slowly time go slowly know little thing hang hang wait baby night tire wait little thing hang hang wait baby night tire wait ring ring ring go telephone light home tick tick tock quarter hang wait know hesitate cause late little thing hang hang wait baby night tire wait little thing hang hang wait baby night tire wait little thing little thing hang hang wait wait tire wait time go slowly time go slowly time go slowly time go slowly slowly slowly slowly slowly slowly slowly slowly slowly slowly slowly slowly slowly slowly know little thing hang hang wait baby night tire wait little thing hang hang wait baby night tire wait little thing little thing hang hang wait wait tire wait',
   'release_date': '2005',
   'len': 161,
   'age': 0.21428571428571402,
   'topic': 'night/time',
   'album_name': 'The Confessions Tour',
   'playcount': 7532416,
   'listeners': 940190,
   'duration': 338000,
   'album_id': 3287,
   'artist_id': 427}]}
```

## Creating reports

In the last part of the workshop we present and store data.

### Displaying data in notebook

We're going to start from displaying the data in the notebook: that's why we're going to copy the code from the hint.

``` python
msg_template = ("{nb}. {track_name}: " 
                "Playcount: {playcount} | "
                "Listeners: {listeners} | "
                "Duration: {duration} | "
                "Topic: {topic}"
       )
```

Now we only need to generate the report, remember the required format:

``` 
Artist: metallica
|___ Album: Master Of Puppets
    |___ Tracklist:
          1. battery (remastered): Playcount: 393621 | Listeners: 62346 | Age: 0.48571428571428504 | Duration: 0 | Topic: sadness
          ....
```

Based on this template and the data we collected we can outline the next steps of our work:

1. Artist needs to be displayed only once:
2. For each album we need to display its name and tracklist,
3. For each song in the tracklist, we present the data as shown in the template.

In terms of Python, we need to write two loops:

- one that iterates the artist's albums
- another that iterates the tracks of one album

In code, this is:

``` python
print(f"Artist: {artist}")  # display the given artist

# iterating artist's albums
for album_id in albums:
    print(f"|___ Album: {albums[album_id]}")  # display album information
    print(f"    | Tracklist:")  # display header (4 spaces)

    album_tracks = tracks[album_id]  # retrieve album tracks
    for nb, track in enumerate(album_tracks, 1):  # iterating consecutive tracks on the album

        # filter the output template
        print("     " + msg_template.format(  # we added 6 spaces to nicely format the list
            nb=nb,
            track_name=track['track_name'],
            playcount=track['playcount'],
            listeners=track['listeners'],
            duration=track['duration'],
            topic=track['topic'],
            ))
```

``` 
Artist: madonna
|___ Album: Madonna
    | Tracklist:
     1. holiday: Playcount: 2310260 | Listeners: 444332 | Duration: 241000 | Topic: world/life
     2. lucky star: Playcount: 1551916 | Listeners: 296486 | Duration: 215000 | Topic: night/time
|___ Album: Like a Virgin
    | Tracklist:
     1. material girl: Playcount: 4414829 | Listeners: 805512 | Duration: 219000 | Topic: world/life
     2. stay: Playcount: 200731 | Listeners: 45311 | Duration: 0 | Topic: sadness
...
|___ Album: The Confessions Tour
    | Tracklist:
     1. jump: Playcount: 2340651 | Listeners: 342979 | Duration: 0 | Topic: night/time
     2. hung up: Playcount: 7532416 | Listeners: 940190 | Duration: 338000 | Topic: night/time
```

### Saving data to a CSV file

To save our data in a `csv` file we're going to need a dedicated Python library that we discussed in the first session:

``` python
import csv
```

Despite a different output format the solution will follow a similar framework: we'll create two loops that generate the consecutive rows for the `csv` file.

Additionally, we need to create a header before we start adding the rows.

``` python
file_name = f"{artist}.csv"  # create file name
f = open(file_name, mode='w+', encoding="UTF-8", newline='')  # set encoding and mode of working with the file

header = ["artist", "album", "track", "listeners", "likes", "duration", "topic"]  # header format copied from exercise instructions

# define csv file according to the requirements
writer = csv.writer(
    f, 
    delimiter="|", 
    quotechar='"',  # this will add quotes to "text"
    quoting=csv.QUOTE_NONNUMERIC,  # set that numbers will not be quoted as "123"
    doublequote=True  # songs and albums where " is used will be additionally enclosed in quotes """
)
writer.writerow(header)  # add header

for album_id in albums:  # iterating all albums
    album_tracks = tracks[album_id]  # retrieve album tracks
    for id, track in enumerate(album_tracks, 1):  # create new row with required data
        writer.writerow([
            artist,
            albums[album_id],
            track['track_name'],
            track['playcount'],
            track['listeners'],
            track['duration'],
            track['topic'],
        ])
f.close()
```

> Considering code readability (to avoid another indent level) we didn't use context manager to open the file in this solution. With this method it is important to remember to use `f.close()` when we finish working with the file.

## Summary

In this article we've seen a sample solution of the task. We started from creating a mockup: simply retrieving data from the API; then generalized it, and created dedicated functions:

- `get_artist_id`, that retrieves artist `id` based on their name,
- `get_artist_albums`, that returns albums by the artist,
- `get_album_tracks` - that retrieves a list of tracks on the album,
- `get_track_data` - that retrieves track information,
  whose job was to retrieve the data from the API without modifying it unless necessary - as in `get_artist_albums`, where we converted a list to a dictionary.

Based on them we also defined *higher* level methods whose job was to appropriately combine the API-based functions and in turn let us retrieve all data with two lines of code:

``` python
artist_id = get_artist_id(artist)
albums, tracks = download_artist_albums(artist_id)
```

This made our solution highly readable.

The last part of the task was was to create two reports:

- one to be displayed,
- another, saved in a csv file named: `{artist_name}.csv` depending on whose data we retrieved.
