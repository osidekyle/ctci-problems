import sqlite3

def tableInit():
    conn = sqlite3.connect(':memory:')


    cur = conn.cursor()

    cur.execute("CREATE TABLE Apartments(AptID int PRIMARY KEY, ApartmentAddress varchar(100), BuildingID int)")
    cur.execute("INSERT INTO Apartments(AptID, ApartmentAddress, BuildingID) values(1, '123 Main Rd', 1)")
    cur.execute("INSERT INTO Apartments(AptID, ApartmentAddress, BuildingID) values(2, '123 Main Rd', 2)")
    cur.execute("INSERT INTO Apartments(AptID, ApartmentAddress, BuildingID) values(3, '123 Main Rd', 2)")

    cur.execute("CREATE TABLE Tenants(TenantID int PRIMARY KEY, TenantName varchar(100), TenantAddress varchar(500))")
    cur.execute("INSERT INTO Tenants(TenantID, TenantName, TenantAddress) values(1, 'Joe Smith', '123 Main Rd')")
    cur.execute("INSERT INTO Tenants(TenantID, TenantName, TenantAddress) values(2, 'Joe Johnson', '123 Main Rd')")

    cur.execute("CREATE TABLE TenantApartments(TenantID int, ApartmentID int, PRIMARY KEY (TenantID, ApartmentID))")
    cur.execute("INSERT INTO TenantApartments(TenantID, ApartmentID) values(1, 1)")
    cur.execute("INSERT INTO TenantApartments(TenantID, ApartmentID) values(1, 2)")
    cur.execute("INSERT INTO TenantApartments(TenantID, ApartmentID) values(2, 3)")

    cur.execute("CREATE TABLE Buildings(BuildingID int PRIMARY KEY, ComplexID int, BuildingName varchar(100), Address varchar(500))")
    cur.execute("INSERT INTO Buildings(BuildingID, ComplexID, BuildingName, Address) values(1, 1, 'oof', '123 Main Rd')")
    cur.execute("INSERT INTO Buildings(BuildingID, ComplexID, BuildingName, Address) values(2, 1, 'ugh', '124 Main Rd')")
    cur.execute("INSERT INTO Buildings(BuildingID, ComplexID, BuildingName, Address) values(3, 1, 'yuh', '125 Main Rd')")

    cur.execute("CREATE TABLE Requests(RequestID int PRIMARY KEY, Status varchar(100), AptID int, Description varchar(500))")
    cur.execute("INSERT INTO Requests(RequestID, Status, AptID, Description) values(1,'Open', 1, 'fgsfsfage')")
    cur.execute("INSERT INTO Requests(RequestID, Status, AptID, Description) values(2, 'Open', 2, 'fgsfsfage')")
    cur.execute("INSERT INTO Requests(RequestID, Status, AptID, Description) values(3, 'Closed', 3, 'fgsfsfage')")



    conn.commit()

    return cur