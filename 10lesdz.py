import sqlite3
connection = sqlite3.connect("test.sl3", 5)
cur = connection.cursor()
# cur.execute("CREATE TABLE first_table (name TEXT);")
cur.execute("INSERT INTO first_table (name) VALUES ('Ann');")
cur.execute("INSERT INTO first_table (name) VALUES ('Kats');")
cur.execute("INSERT INTO first_table (name) VALUES ('John');")
connection.commit()
cur.execute("SELECT rowid, name FROM first_table WHERE rowid=1;")
connection.commit()

cur.execute("UPDATE first_table SET name = 'Sam' WHERE rowid=1; ")
res = cur.fetchall()
cur.execute("SELECT rowid, name FROM first_table")
connection.commit()
cur.execute("DELETE FROM first_table WHERE rowid=2;")
connection.commit()
res = cur.fetchall()
print(res)
connection.close()