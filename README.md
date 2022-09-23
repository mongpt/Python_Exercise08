# Python_Exercise08
## 8. Using relational databases
### NOTE: This whole exercise must be run from the top to button to utilize below common function.
```python
import mysql.connector
testDB = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='root',
    password='xxxxxx',
    autocommit= True
)
```
1. Write a program that asks the user to enter the ICAO code of an airport. The program fetches and prints out the corresponding
airport name and location (town) from the airport database used on this course.
```python
icao = input("Please input ICAO code: ")
mycursor = testDB.cursor()
mycursor.execute(f"select name as 'airport name', municipality as 'location' from airport where ident = '{icao}';")
for x in mycursor:
  print(x)
print(mycursor.rowcount, 'rows in set')
```
Output console:
```
Please input ICAO code: VVTS
('Tan Son Nhat International Airport', 'Ho Chi Minh City')
1 rows in set
```
2. Write a program that asks the user to enter the area code (for example `FI`) and prints out the airports located in that country
ordered by airport type. For example, Finland has 65 small airports, 15 helicopter airports and so on.
```python
areaCode = input("Input the area code (i.e. FI): ")
mycursor = testDB.cursor()
mycursor.execute(f"select country.name as 'country name', airport.name as 'airport name', airport.type as 'airport type' from country, airport where country.iso_country = airport.iso_country and airport.iso_country = '{areaCode}' order by airport.type;")
for x in mycursor:
  print(x)
print(mycursor.rowcount, 'rows in set')
```
Output console:
```
Input the area code (i.e. FI): VN
('Vietnam', 'Red Beach Airfield', 'closed')
('Vietnam', 'Phu Quoc Airport', 'closed')
('Vietnam', 'Long Thanh International Airport (under construction)', 'closed')
('Vietnam', 'Phan Thiet Airport', 'closed')
('Vietnam', 'Nha Trang Air Base', 'closed')
('Vietnam', 'Duc My Airstrip', 'closed')
('Vietnam', 'Long Xuyên Airport', 'closed')
('Vietnam', 'Qu?ng Ngãi Airfield', 'closed')
('Vietnam', 'N??c M?n (Marble Mountain) Air Facility', 'closed')
('Vietnam', 'Keangnam Hanoi Landmark Tower Helipad', 'heliport')
('Vietnam', 'Keangnam Tower B Helipad', 'heliport')
('Vietnam', 'Keangnam Tower A Helipad', 'heliport')
('Vietnam', 'Central Pediatric Institute Helipad', 'heliport')
('Vietnam', 'N?m C?n Heliport', 'heliport')
('Vietnam', 'Bach Mai Heliport', 'heliport')
('Vietnam', '??o Nam Y?t (Namyit Island) Helipad', 'heliport')
('Vietnam', '?á Tây (West London Reef) Helipad', 'heliport')
('Vietnam', '?á L?n (Discovery Great Reef) Helipad', 'heliport')
('Vietnam', '??o Phan Vinh (Pearson Reef B) Helipad', 'heliport')
('Vietnam', 'Noi Bai International Airport', 'large_airport')
('Vietnam', 'Tan Son Nhat International Airport', 'large_airport')
('Vietnam', 'Gia Lam Air Base', 'medium_airport')
('Vietnam', 'Da Nang International Airport', 'medium_airport')
('Vietnam', 'Phu Bai International Airport', 'medium_airport')
('Vietnam', 'Pleiku Airport', 'medium_airport')
('Vietnam', 'Phu Quoc International Airport', 'medium_airport')
('Vietnam', 'Vinh Airport', 'medium_airport')
('Vietnam', 'Rach Gia Airport', 'medium_airport')
('Vietnam', 'Dong Tac Airport', 'medium_airport')
('Vietnam', 'Van Don International Airport', 'medium_airport')
('Vietnam', 'Phu Cat Airport', 'medium_airport')
('Vietnam', 'Lien Khuong Airport', 'medium_airport')
('Vietnam', 'Dien Bien Phu Airport', 'medium_airport')
('Vietnam', 'Can Tho International Airport', 'medium_airport')
('Vietnam', 'Buon Ma Thuot Airport', 'medium_airport')
('Vietnam', 'Cat Bi International Airport', 'medium_airport')
('Vietnam', 'Dong Hoi Airport', 'medium_airport')
('Vietnam', 'Cà Mau Airport', 'medium_airport')
('Vietnam', 'Cam Ranh International Airport / Cam Ranh Air Base', 'medium_airport')
('Vietnam', 'Con Dao Airport', 'medium_airport')
('Vietnam', 'Kontum Airport', 'medium_airport')
('Vietnam', 'Sóc Tr?ng Airport', 'small_airport')
('Vietnam', 'Vung Tau Airport', 'small_airport')
('Vietnam', 'Yên Bái Air Base', 'small_airport')
('Vietnam', '??o Tr??ng Sa (Spratly Island) Airport', 'small_airport')
('Vietnam', 'Tho Xuan Airport', 'small_airport')
('Vietnam', 'Nhon Co Airfield', 'small_airport')
('Vietnam', 'Phu Quy Airport', 'small_airport')
('Vietnam', 'Bien Hoa Air Base', 'small_airport')
('Vietnam', 'Phan Rang Airport', 'small_airport')
('Vietnam', 'Haiphong Kien An Airport', 'small_airport')
('Vietnam', 'Chu Lai Airport', 'small_airport')
('Vietnam', 'Cam Ly Airport', 'small_airport')
('Vietnam', 'Na-San Airport', 'small_airport')
('Vietnam', 'Kep Air Base', 'small_airport')
('Vietnam', 'Vinh Long Airfield', 'small_airport')
56 rows in set
```
3. Write a program that asks the user to enter the ICAO codes of two airports. The program prints out the distance between the two
airports in kilometers. The calculation is based on the airport coordinates fetched from the database. Calculate the distance using 
the `geopy` library:  https://geopy.readthedocs.io/en/stable/. Install the library by selecting **View / Tool Windows / Python Packages**
in your PyCharm IDE, write `geopy` into the search field and finish the installation.
```python
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
```
Output console:
```
Input the first ICAO code: VVTS
('Tan Son Nhat International Airport',)
Input the second ICAO code: VVNB
('Noi Bai International Airport',)
The distance between 2 airports is 1154.68 km
```
