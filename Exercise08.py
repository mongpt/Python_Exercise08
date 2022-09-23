# NOTE: This whole exercise must be run from the top to button to utilize below common function.
import mysql.connector
testDB = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit= True
)

# Part 1: Write a program that asks the user to enter the ICAO code of an airport. The program fetches and prints out
# the corresponding airport name and location (town) from the airport database used on this course.
icao = input("Please input ICAO code: ")
mycursor = testDB.cursor()
mycursor.execute(f"select name as 'airport name', municipality as 'location' from airport where ident = '{icao}';")
for x in mycursor:
  print(x)
print(mycursor.rowcount, 'rows in set')

# Part 2: Write a program that asks the user to enter the area code (for example FI) and prints out the airports located
# in that country ordered by airport type. For example, Finland has 65 small airports, 15 helicopter airports and so on.
areaCode = input("Input the area code (i.e. FI): ")
mycursor = testDB.cursor()
mycursor.execute(f"select country.name as 'country name', airport.name as 'airport name', airport.type as 'airport type' from country, airport where country.iso_country = airport.iso_country and airport.iso_country = '{areaCode}' order by airport.type;")
for x in mycursor:
  print(x)
print(mycursor.rowcount, 'rows in set')

# Part 3: Write a program that asks the user to enter the ICAO codes of two airports. The program prints out the
# distance between the two airports in kilometers. The calculation is based on the airport coordinates fetched from the
# database. Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/. Install the library
# by selecting View / Tool Windows / Python Packages in your PyCharm IDE, write geopy into the search field and finish the installation.
from geopy import distance
mycursor = testDB.cursor()
icao1 = input("Input the first ICAO code: ")
mycursor.execute(f"select name from airport where ident = '{icao1}';")
for x in mycursor:
    print(x)
icao2 = input("Input the second ICAO code: ")
mycursor.execute(f"select name from airport where ident = '{icao2}';")
for x in mycursor:
    print(x)
mycursor.execute(f"select latitude_deg, longitude_deg from airport where ident = '{icao1}' or ident = '{icao2}';")
listDeg = []
for x in mycursor:
    listDeg.append(x)
print(f"The distance between 2 airports is", f"{distance.distance(listDeg[0], listDeg[1]).km:.2f} km")
