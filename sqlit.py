import sqlite3
conn=sqlite3.connect('dbs1.db')
c = conn.cursor()

re = c.execute("SELECT id FROM data where id = (select max(id) from data) ").fetchone()
mx = re[0]
print(type(mx))
print(mx)
results = c.execute(""" select lon ,lat ,temp from data;""" \
                     ).fetchall()

print(results)
conn.commit()
conn.close()
