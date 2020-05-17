import  sqlite3

conn=sqlite3.connect("araz.db")
c=conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL )")

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(15,'2020-04-30','texxx', 105)")
    conn.commit()
    c.close()

create_table()
data_entry()
