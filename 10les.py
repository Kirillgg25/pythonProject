import sqlite3
connection = sqlite3.connect("test.sl3", 5)
cur = connection.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS first_table (name TEXT);")
connection.commit()
cur.execute("SELECT rowid, name FROM first_table;")
connection.commit()
cur.execute("INSERT INTO first (data) VALUES ('Ann');")
cur.execute("INSERT INTO first (data) VALUES ('Kats');")
cur.execute("INSERT INTO first (data) VALUES ('John');")
cur.execute("INSERT INTO first (data) VALUES ('Kirill');")
connection.commit()
cur.execute("UPDATE first_table SET name='Kate' WHERE rowid =3;")
connection.commit()
# cur.execute("DROP TABLE first_table;")
# connection.commit()
res = cur.fetchall()
print(res)
connection.close()