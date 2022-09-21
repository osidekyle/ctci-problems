import sqlite3

def tableInit():
    conn = sqlite3.connect(':memory:')


    cur = conn.cursor()

    cur.execute("CREATE TABLE Apartments(ApartmentID int PRIMARY KEY, ApartmentAddress varchar(100), BuildingID int)")
    cur.execute("INSERT INTO Apartments(ApartmentID, ApartmentAddress, BuildingID) values(1, '123 Main Rd', 1)")
    cur.execute("INSERT INTO Apartments(ApartmentID, ApartmentAddress, BuildingID) values(2, '123 Main Rd', 1)")
    cur.execute("INSERT INTO Apartments(ApartmentID, ApartmentAddress, BuildingID) values(3, '123 Main Rd', 1)")

    cur.execute("CREATE TABLE Tenants(TenantID int PRIMARY KEY, TenantName varchar(100), TenantAddress varchar(500))")
    cur.execute("INSERT INTO Tenants(TenantID, TenantName, TenantAddress) values(1, 'Joe Smith', '123 Main Rd')")
    cur.execute("INSERT INTO Tenants(TenantID, TenantName, TenantAddress) values(2, 'Joe Johnson', '123 Main Rd')")

    cur.execute("CREATE TABLE TenantApartments(TenantID int, ApartmentID int, PRIMARY KEY (TenantID, ApartmentID))")
    cur.execute("INSERT INTO TenantApartments(TenantID, ApartmentID) values(1, 1)")
    cur.execute("INSERT INTO TenantApartments(TenantID, ApartmentID) values(1, 2)")
    cur.execute("INSERT INTO TenantApartments(TenantID, ApartmentID) values(2, 3)")

    conn.commit()

    return cur