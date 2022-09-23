from utils.db_helper import tableInit
import sqlite3

cur = tableInit()


cur.execute("""
             SELECT BuildingID, Count(*)
             FROM Apartments JOIN Requests ON Requests.AptID = Apartments.ApartmentID
             WHERE Status = "Open"
             GROUP BY BuildingID;
            """)
rows = cur.fetchall()

for row in rows:
    print(row)