#C:\Users\Ania\Desktop\Music Master\scheduler.py

import sys
import MySQLdb
import os
from random import randint

order = ['AC', 'BC', 'AA', 'C1', 'BA', 'AA', 'CC', 'C2', 'AC', 'BC', 'CA', 'C3', 'BA']
songs = []
#each song is an array [name, artist, dur, cat, starttime]
time = 0
#86400 seconds

def select_song(cat):
    query = ("SELECT title, artist, runs FROM songs WHERE category=\"%s\"" %(cat))
    cursor.execute(query)
    s = cursor.fetchall()
    size = cursor.rowcount
    n = randint(0, size-1)
    title = s[n][0]
    artist = s[n][1]
    runs = s[n][2]
    tsec = runs.total_seconds()
    return [title, artist, runs, tsec]


db = MySQLdb.connect('localhost','root','kwiecien','music_lib')

cursor = db.cursor()


t = 0
while time < 94000:
    song = select_song(order[t])
    songs.append(song)
    time += song[3]
    t += 1
    if t == len(order):
        t = 0

db.close()
print('DB done')


#one day's playlist
playlist = open('C:\Users\Ania\Desktop\Music Master\playlist.txt', 'w')
stime = 0
i = 0


playlist.write('## 2AM - 6AM\n\n')
while stime < 15600:
    s = songs[i]
    stime += s[3]
    offset = 50 - len(s[0])
    playlist.write(s[0] + ' '*offset + s[1] + '\n')
    i += 1
playlist.write('\n')
stime = 0

playlist.write('## 6AM - 9AM\n\n')
while stime < 11700:
    s = songs[i]
    stime += s[3]
    offset = 50 - len(s[0])
    playlist.write(s[0] + ' '*offset + s[1] + '\n')
    i += 1
playlist.write('\n')
stime = 0

playlist.write('## 9AM - 12PM\n\n')
while stime < 11700:
    s = songs[i]
    stime += s[3]
    offset = 50 - len(s[0])
    playlist.write(s[0] + ' '*offset + s[1] + '\n')
    i += 1
playlist.write('\n')
stime = 0

playlist.write('## 12PM - 4PM\n\n')
while stime < 15600:
    s = songs[i]
    stime += s[3]
    offset = 50 - len(s[0])
    playlist.write(s[0] + ' '*offset + s[1] + '\n')
    i += 1
playlist.write('\n')
stime = 0

playlist.write('## 4PM - 7PM\n\n')
while stime < 11700:
    s = songs[i]
    stime += s[3]
    offset = 50 - len(s[0])
    playlist.write(s[0] + ' '*offset + s[1] + '\n')
    i += 1
playlist.write('\n')
stime = 0

playlist.write('## 7PM - 11PM\n\n')
while stime < 15600:
    s = songs[i]
    stime += s[3]
    offset = 50 - len(s[0])
    playlist.write(s[0] + ' '*offset + s[1] + '\n')
    i += 1
playlist.write('\n')
stime = 0

playlist.write('## 11PM - 2AM\n\n')
while stime < 11700:
    s = songs[i]
    stime += s[3]
    offset = 50 - len(s[0])
    playlist.write(s[0] + ' '*offset + s[1] + '\n')
    i += 1


playlist.close()


print('Text done')
