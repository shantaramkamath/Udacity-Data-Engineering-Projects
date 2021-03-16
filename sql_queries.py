# DROP TABLES

songplay_table_drop   =    "DROP TABLE IF EXISTS songplays"
#print("Table songplays dropped")
user_table_drop       =    "DROP TABLE IF EXISTS users"
#print("Table users dropped")
song_table_drop       =    "DROP TABLE IF EXISTS songs"
#print("Table songs dropped")
artist_table_drop     =    "DROP TABLE IF EXISTS artists"
#print("Table artists dropped")
time_table_drop       =    "DROP TABLE IF EXISTS time"
#print("Table time dropped")

# CREATE TABLES

user_table_create     = ("""CREATE TABLE IF NOT EXISTS users(
                            user_id TEXT CONSTRAINT users_pk PRIMARY KEY, 
                            first_name TEXT, 
                            last_name TEXT, 
                            gender TEXT, 
                            level TEXT)
""")
#print("Table users created")

artist_table_create   = ("""CREATE TABLE IF NOT EXISTS artists(
                            artist_id TEXT CONSTRAINT artists_pk PRIMARY KEY,  
                            name TEXT, 
                            location TEXT, 
                            latitude DECIMAL, 
                            longitude DECIMAL)
""")
#print("Table artists created")

time_table_create     = ("""CREATE TABLE IF NOT EXISTS time(
                            start_time TIMESTAMP CONSTRAINT time_pk PRIMARY KEY, 
                            hour INT, 
                            day INT, 
                            week INT, 
                            month INT, 
                            year INT,  
                            weekday INT)
""")
#print("Table time created")

song_table_create     = ("""CREATE TABLE IF NOT EXISTS songs(
                            song_id TEXT CONSTRAINT songs_pk PRIMARY KEY, 
                            title TEXT, 
                            artist_id TEXT, 
                            year INT, 
                            duration DECIMAL
                            )
""")
"""
,
                            CONSTRAINT fk_artists
                            FOREIGN KEY(artist_id) 
                            REFERENCES artists(artist_id)
"""
#print("Table songs created")

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(
                            songplay_id SERIAL CONSTRAINT songplay_pk PRIMARY KEY, 
                            start_time TIMESTAMP, 
                            user_id TEXT, 
                            level TEXT, 
                            song_id TEXT, 
                            artist_id TEXT, 
                            session_id TEXT, 
                            location TEXT, 
                            user_agent TEXT
                            )
""")
"""
,
                            CONSTRAINT fk_artists_songplays
                            FOREIGN KEY(artist_id) 
                            REFERENCES artists(artist_id),
                            CONSTRAINT fk_time
                            FOREIGN KEY(start_time) 
                            REFERENCES time(start_time),
                            CONSTRAINT fk_users
                            FOREIGN KEY(user_id) 
                            REFERENCES users(user_id),
                            CONSTRAINT fk_songs
                            FOREIGN KEY(song_id) 
                            REFERENCES songs(song_id)
"""
#print("Table songplays created")



# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays VALUES(DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s)
""")
#print("Table songplays values inserted")

user_table_insert     = ("""INSERT INTO users VALUES(%s, %s, %s, %s, %s) 
                            ON CONFLICT (user_id) DO UPDATE 
                            SET level = EXCLUDED.level
""")
#print("Table users values inserted")

song_table_insert     = ("""INSERT INTO songs VALUES(%s, %s, %s, %s, %s)
                            ON CONFLICT (song_id) DO NOTHING
""")
#print("Table songs values inserted")

artist_table_insert   = ("""INSERT INTO artists(artist_id, name, location, latitude, longitude) VALUES(%s, %s, %s, %s, %s)
                            ON CONFLICT (artist_id) DO UPDATE 
                            SET location  = EXCLUDED.location,
                                latitude  = EXCLUDED.latitude,
                                longitude = EXCLUDED.longitude
""")
#print("Table artists values inserted")

time_table_insert     = ("""INSERT INTO time VALUES(%s, %s, %s, %s, %s, %s, %s)
                            ON CONFLICT (start_time) DO NOTHING
""")
#print("Table time values inserted")

# FIND SONGS

song_select           = ("""SELECT song_id, artists.artist_id
                            FROM songs JOIN artists ON songs.artist_id = artists.artist_id
                            WHERE songs.title = %s
                            AND artists.name = %s  
                            AND songs.duration = %s
""")

# QUERY LISTS

create_table_queries  = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries    = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]