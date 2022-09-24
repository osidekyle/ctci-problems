from utils.db_helper import tableInit
import sqlite3

cur = tableInit()


cur.execute("""
            UPDATE Requests
            SET Status = 'Closed'
            WHERE
            AptID in (
                SELECT AptID
                FROM Apartments
                WHERE Apartments.BuildingID = 2
                );
            """)

cur.execute("SELECT * FROM Requests")
rows = cur.fetchall()

for row in rows:
    print(row)