from utils.db_helper import tableInit
import sqlite3

cur = tableInit()

cur.execute("SELECT Tenants.TenantName FROM Tenants INNER JOIN TenantApartments ON Tenants.TenantID = TenantApartments.TenantID GROUP BY Tenants.TenantID HAVING Count(*) > 1")

rows = cur.fetchall()

for row in rows:
    print(row)