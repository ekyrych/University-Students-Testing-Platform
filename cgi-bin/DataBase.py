import sqlite3
from datetime import datetime
conn = sqlite3.connect("Server.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

now=datetime.strftime(datetime.now(), "%Y/%m/%d")
print (now)
cursor.execute("""INSERT INTO Users
                  VALUES ('Dyordyak','Vasil','3','soloveiko','soloveikopass',(?),'true')""",(now,)
                  )
conn.commit()
#for a in range(1,5):
#cursor.execute("DELETE FROM Users WHERE Name_First='Admin'")

sql = "SELECT * FROM Users "
print("Here's a listing of all the records in the table:")

for row in cursor.execute("SELECT rowid, * FROM Users ORDER BY Name_First"):
    print(row)
