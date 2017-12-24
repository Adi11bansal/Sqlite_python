import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style
style.use('fivethirtyeight')


conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1352549219,'2017-01-11 18:53:39','jython',8)")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():

    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)

    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
          (unix, date, keyword, value))

    conn.commit()
##
##
##def read_from_db():
##    c.execute('SELECT * from stuffToPlot ')
##    #data = c.fetchall()
##    #print(data)
##    for row in c.fetchall():
##        #print(row)
##
##
##    c.execute('SELECT * FROM stuffToPlot WHERE value = 3')
##    data = c.fetchall()
##    #print(data)
##    for row in data:
##        print(row)
##
##    c.execute('SELECT * FROM stuffToPlot WHERE unix > 1452554972')
##    data = c.fetchall()
##    #print(data)
##    for row in data:
##        print(row)
##
##    c.execute('SELECT value, datestamp FROM stuffToPlot WHERE unix > 1452554972')
##    data = c.fetchall()
##    #print(data)
##    for row in data:
##        print(row[1])
##
##def graph_data():
##    c.execute('SELECT datestamp, value FROM stuffToPlot')
##    data = c.fetchall()
##
##    dates = []
##    values = []
##    
##    for row in data:
##        dates.append(parser.parse(row[0]))
##        values.append(row[1])
##
##    plt.plot_date(dates,values,'-')
##    plt.show()
##
##def del_and_update():
##    c.execute('SELECT * FROM stuffToPlot')
##    data = c.fetchall()
##    [print(row) for row in data]
##
##
##    c.execute('UPDATE stuffToPlot SET value = 98 WHERE value = 1')
##    conn.commit()
##
##    c.execute('SELECT * FROM stuffToPlot')
##    data = c.fetchall()
##    [print(row) for row in data]
##
##
##    c.execute('DELETE FROM stuffToPlot WHERE value = 98')
##    conn.commit()
##
##    c.execute('SELECT * FROM stuffToPlot')
##    data = c.fetchall()
##    [print(row) for row in data]
##
##    
##
##create_table()
##data_entry()
for i in range(1000):
    dynamic_data_entry()
    time.sleep(1)

##del_and_update()
####graph_data()
#read_from_db()
c.close
conn.close()








    


