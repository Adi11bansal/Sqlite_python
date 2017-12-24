import pandas as pd
import sqlite3



conn = sqlite3.connect('tutorial.db')
c = conn.cursor()
c.execute('SELECT * from stuffToPlot ')
data= c.fetchall()
df=pd.DataFrame(data)
print(df.head())
c.close()
