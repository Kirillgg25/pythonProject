import sqlite3
connection = sqlite3.connect("itstep_DB.sl3", 5)
cur = connection.cursor()
try:
    cur.execute("CREATE TABLE first_table (name);")
    connection.commit()
except :
    cur.execute("DROP TABLE first_table;")
    connection.commit()
# def teble():
#     if table == 0:
#         cur.execute("CREATE TABLE first_table (name);")
#         connection.commit()
#         table += 1
#     elif table == 1:
#         cur.execute("DROP TABLE first_table;")
#         connection.commit()
#         table == 0
# print(teble())
cur.execute("SELECT rowid, name FROM first_table;")
connection.commit()
cur.execute("INSERT INTO first_table (name) VALUES ('Ann');")
cur.execute("INSERT INTO first_table (name) VALUES ('Kats');")
cur.execute("INSERT INTO first_table (name) VALUES ('John');")
cur.execute("INSERT INTO first_table (name) VALUES ('Kirill');")
connection.commit()
cur.execute("UPDATE first_table SET name='Kate' WHERE rowid =3;")
connection.commit()
res = cur.fetchall()
print(res)

connection.close()