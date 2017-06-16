#C:\Users\Ania\Desktop\Music Master\init_db.py



import csv
import sys
import MySQLdb
import glob
import os

break
with open('C:\Users\Ania\Desktop\Music Master\music master data.txt') as f:
    reader = csv.reader(f, delimiter="\t")
    d = list(reader)
    l = len(d)

    db = MySQLdb.connect('localhost','root','kwiecien','music_lib')
    cursor = db.cursor()



    for n in range(1, l):
        
        category = d[n][0]
        title =  d[n][1]
        artist = d[n][2]
        runs = '00:' + d[n][4]
        ending = d[n][5]
        keywords = d[n][6]
        gender = d[n][7]
        tempo = d[n][8]
        power = d[n][9]
        daypart = d[n][10]

        if tempo != '':
            tempo = int(tempo)
        else:
            tempo = 0
        if power != '':
            power = int(power)
        else:
            power = 0
        if len(gender) > 1:
            gender = ''

        sql = "insert into songs VALUES('%s', \"%s\", \"%s\", NULL, '%s', '%s', \"%s\", '%s', %d, %d, '%s')" % \
 (category, title , artist, runs, ending, keywords, gender, tempo, power, daypart)
        print(sql)
        cursor.execute(sql)
        db.commit()
    db.close()
