BandBook
Version 1.0.0 Platform where you can find the entire collection of a specific band and various information about it. This is only the backend API.

Getting started
$ git clone BandBook

$ python -m venv venv

$ source venv/bin/activate

$ pip freeze > requirements.txt

$ pip install -r requirements.txt

$ configure the .env file

$ flask run

Routes
POST /api/band - creates band, POST api/band_profile - creates a band profile, POST /api/album - creates album, POST /api/music - creates music and relates them to a band and to an album, POST api/genre - creates genre, POST api/band_genre - relates band and genre, GET /api/band/id - list project by id

Examples of Requests:
Creating band: POST /api/band

{
"name": "Joana Bruni"
}

Creating profile: POST api/band_profile

{
"state":"LA",
"country":"USA",
"ein":"4457896",
"band_id":1
}

Creating album: POST /api/album

{
"name": "Chick",
"release_year": 1997,
"band_id":1
}

Creating music: POST /api/music

{
"name":"Enjoy the silence",
"band_id":1,
"album_id":1
}

Creating genre: POST api/genre

{
"name": "Pop"
}

Creating relationship between band and genre: POST api/band_genre

{
"band_id":1,
"genre_id":1
}

Getting band by id: GET /api/band/1
