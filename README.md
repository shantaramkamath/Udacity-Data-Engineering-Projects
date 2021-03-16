# Project: Data Modeling with Postgres

A startup named Sparkify wants to analyze user activities using their song and user data. The current data is spread among several JSON files, making it hard to query and analyze.

This project aims to create an ETL pipeline to load song and user data to a Postgres database, making it easier to query and analyze data.

## Datasets

Data is currently collected for song and user activities, in two directories: data/log_data and data/song_data, using JSON files.

### Song dataset format

>
>{
> "num_songs": 1,
> "artist_id": "ARGSJW91187B9B1D6B",
> "artist_latitude": 35.21962,
> "artist_longitude": -80.01955,
> "artist_location": "North Carolina",
> "artist_name": "JennyAnyKind",
> "song_id": "SOQHXMF12AB0182363",
> "title": "Young Boy Blues",
> "duration": 218.77506,
> "year": 0
>}
>

### Log dataset format

>
>{
> "artist": "Survivor",
> "auth": "Logged In",
> "firstName": "Jayden",
> "gender": "M",
> "itemInSession": 0,
> "lastName": "Fox",
> "length": 245.36771,
> "level": "free",
> "location": "New Orleans-Metairie, LA",
> "method": "PUT",
> "page": "NextSong",
> "registration": 1541033612796,
> "sessionId": 100,
> "song": "Eye Of The Tiger",
> "status": 200,
> "ts": 1541110994796,
>  "userAgent": "\"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 > Safari/537.36\"",
> "userId": "101"
>}
>

## Schema

### Fact table
 
**songplays** - records in log data associated with song plays i.e. records with page NextSong    
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent  

### Dimension Tables

**users** - users in the app  
user_id, first_name, last_name, gender, level  
**songs** - songs in music database  
song_id, title, artist_id, year, duration  
**artists** - artists in music database  
artist_id, name, location, latitude, longitude  
**time** - timestamps of records in songplays broken down into specific units  
start_time, hour, day, week, month, year, weekday  

## Build

### Pre-requisites:

 - Python 3
 - pipenv
 - pyenv (optional)
 - PostgreSQL Database

To install project python dependencies, you should run:

> pipenv install

## Database

The database can be installed locally or ran using Docker, which is the preferred method.  

To use docker to run Postgres, you should run:

> docker run --net=host --name postgres -e POSTGRES_PASSWORD=your_password -d postgres

### Access and user setup

To initially access the database, you should run:

> psql -h localhost -U postgres

You should run the following commands under psql to setup user access to Postgres and create the initial sparkifydb database:

> - CREATE ROLE student WITH ENCRYPTED PASSWORD 'student';
> - ALTER ROLE student WITH LOGIN;
> - ALTER ROLE student CREATEDB;
> - CREATE DATABASE sparkifydb OWNER student;

## Running

To run the project locally, use pipenv to activate the virtual environment:

> pipenv shell

And run the scripts to create database tables:

> ./create_tables.py

and populate data into tables:

> ./etl.py

Data can be verified using the provided test.ipynb jupyter notebook:

> jupyter notebook