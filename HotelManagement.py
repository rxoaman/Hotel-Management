import datetime
import mysql.connector as sqlc
con = sqlc.connect(host='localhost', user ='root', password='root123')
cur=con.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS HotelManagement")
cur.execute("USE HotelManagement")
cur.execute("CREATE TABLE IF NOT EXISTS guests (Name VARCHAR(25) NOT NULL, PhoneNo VARCHAR(10) NOT NULL, Address VARCHAR(255) NOT NULL, Check_In VARCHAR(10) NOT NULL, Check_Out VARCHAR(10) NOT NULL)")
cur.execute("CREATE TABLE IF NOT EXISTS rooms (PhoNo VARCHAR(10), TypeOfRoom VARCHAR(20))")
def validate_name(name):
    if name.replace(' ', '').isalpha():
        return True
    else:
        return False

def validate_phone_number(phone):
    if phone.isdigit() and len(phone) == 10:
        return True
    else:
        return False
def validate_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False
while True:
	print("-----------Options------------")
	print("1.Booking \n2.Room Service \n3.Record \n0.Exit")
	m1=int(input('Enter Your Selection \n'))
	if m1==1:
		while True:
			d1 = input("Your Name: \n")
			if validate_name(d1):
				break
			else:
				print("Invalid name! Please enter a valid name.")
		while True:
			d2 = input("Enter Your Mobile Number (10 Digits): \n")
			if validate_phone_number(d2):
				break
			else:
				print("Invalid phone number! Please enter a valid 10-digit number.")
		d3=input("Enter Your Address: \n")
		while True:
			d4 = input('Check In Date (YYYY-MM-DD): \n')
			if validate_date(d4):
				break
			else:
				print("Invalid date format! Please enter a date in YYYY-MM-DD format.")
		while True:
			d5=input("Check Out Date(YYYY-MM-DD) \n")
			if validate_date(d5):
				break
			else:
				print("Invalid date format! Please enter a date in YYYY-MM-DD format.")
		
		cur.execute("INSERT INTO guests (Name, PhoneNo, Address, Check_In, Check_Out) VALUES ('%s','%s','%s','%s','%s')"%(d1,d2,d3,d4,d5))
		con.commit()
		cur.execute(f"select * from guests where PhoneNo={d2}")
		d=cur.fetchone()
		print(d)
		while True:
			m12=int(input("1.AC Room \n2.Non-AC Room \n0.Exit"))
			if m12==1:
				AC="AC Room"
				print("Your Booking Has Been Registered")
				cur.execute("INSERT INTO rooms (PhoNo, TypeOfRoom) VALUES (%s, '%s')"%(d2,AC))
				con.commit()
				print("--------------------------------")
				break
			elif m12==2:
				NAC="Non-AC Room"
				print("Your Booking Has Been Registered")
				cur.execute("INSERT INTO rooms (PhoNo, TypeOfRoom) VALUES (%s, '%s')"%(d2,NAC))
				con.commit()
				print("--------------------------------")
				break
			elif m12==0:
				print("--------------------------------")
				break
			else:
				print("You've Entered Wrong Value")
				print("--------------------------------")
	if m1==2:
		z=1
		k=str(z)
		y='bill'+k
		cur.execute("CREATE TABLE %s (Item VARCHAR(200) ,  Price int(3) );" %y)
		while True:
			con.commit()
			print("1.Food \n2.Beverages \n0.Exit")
			m21=int(input("Enter What You Want To Order? \n"))
			z1=[]
			if m21==1:
				while True:
					print("----------×Menu×----------")
					print("1. Pizza(Rs290) \n2.Sphagetti(Rs380) \n3.Paneer Tikka(Rs220) \n4.Dal Makhni(Rs190) \n5.Pan Tossed Momos(Rs180) \n6.Chilli Chicken(Rs720) \n0.Exit")
					m22=int(input("Enter your Order \n"))
					if m22==1:
						z1.append(int(290))
						cur.execute("INSERT INTO {} (Item, Price) VALUES ('Pizza', 290)".format(y))
						con.commit()
						print("Your order has been placed")
						print("--------------------------------")
					elif m22==2:
						z1.append(int(380))
						cur.execute("INSERT INTO {} (Item, Price) VALUES ('Sphagetti', 380)".format(y))
						con.commit()
						print("Your order has been placed")
						print("--------------------------------")
					elif m22==3:
						z1.append(int(220))
						cur.execute("INSERT INTO {} (Item, Price) VALUES ('Paneer Tikka', 220)".format(y))
						con.commit()
						print("Your order has been placed")
						print("--------------------------------")
					elif m22==4:
						z1.append(int(190))
						cur.execute("INSERT INTO {} (Item, Price) VALUES ('Dal Makhni', 190)".format(y))
						con.commit()
						print("Your order has been placed")
						print("--------------------------------")
					elif m22==5:
						z1.append(int(190))
						cur.execute("INSERT INTO {} (Item, Price) VALUES ('Pan Tosssed Momos', 180)".format(y))
						con.commit()
						print("Your order has been placed")
						print("--------------------------------")
					elif m22==6:
						z1.append(int(190))
						cur.execute("INSERT INTO {} (Item, Price) VALUES ('Chilli Chicken',720)".format(y))
						con.commit()
						print("Your order has been placed")
						print("--------------------------------")
					elif m22==0:
						print("--------------------------------")
						break
					else:
						print("--------------------------------")
			if m21==2:
				while True:
					print("----------×Menu×----------")
					print("1. Cappuccino(Rs290) \n2.Cold Coffe(Rs380) \n3.Espresso(Rs220) \n0.Exit")
					m23=int(input("Enter your Order \n"))
					if m23==1:
						z1.append(int(290))
						cur.execute("INSERT INTO {} (Item, Price) VALUES ('Cappuccin0 ', 290)".format(y))
						con.commit()
						print("Your order has been placed")
						print("--------------------------------")
					elif m23==2:
						z1.append(int(380))
						cur.execute("INSERT INTO {} (Item, Price) VALUES ('Cold Coffee', 380)".format(y))
						con.commit()
						print("Your order has been placed")
						print("--------------------------------")
					elif m23==3:
						z1.append(int(220))
						cur.execute("INSERT INTO {} (Item, Price) VALUES ('Espresso', 220)".format(y))
						con.commit()
						print("Your order has been placed")
						print("--------------------------------")
					elif m23==0:
						print("--------------------------------")
						break
					else:
						print("--------------------------------")
			elif m21==0:
				print("--------------------------------")
				cur.execute("select * from %s" %y)
				i2=cur.fetchall()
				print("Your Bill No. Is",z)
				print(i2)
				v2=sum(z1)
				total=(v2)
				print("Ordered")
				print("--------------------------------")
				break
			else:
				print("--------------------------------")
	if m1==3:
		while True:
			print("1.Your Booking Details \n2.Check Your Bill \n3.Check Type of Room \n0.Exit ")
			m31=int(input("Enter Your Choice \n"))
			if m31==1:
				y12=input("Enter Your Phone Number! \n")
				cur.execute("select * from guests where PhoneNO='%s'"%y12)
				d92=cur.fetchall()
				print(d92)
				print("--------------------------------")
				continue
			elif m31==2:
				y13=input("Enter Your Bill Number!(ex:- bill4)")
				cur.execute("select * from %s" %y13)
				i3=cur.fetchall()
				print("Your Bill Is:- \n", i3)
				print("--------------------------------")
				continue
			elif m31==3:
				y14=input("Enter Phone Number! \n")
				cur.execute("select * from rooms where PhoNo=%s" %y14)
				i4=cur.fetchall()
				print("Your Data", i4)
				continue
			elif m31==0:
				print("--------------------------------")
				break
			else:
				print("You've Entered A Wrong Value!")
				print("--------------------------------")
	if m1==0:
		print("Thank You For Joining Us!")
		print("--------------------------------")
		break
	cur.close()
	con.close()
print('Topic:-Hotel Management \n Made By:- Purushottam Kumar')