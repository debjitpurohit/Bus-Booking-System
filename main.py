import mysql.connector
from datetime import date
import random
import string

# '''-------------asansol to kolkata busbooking---------------
def bus1(connection , cur):
    pname = input("enter your name :")
    pAge = int(input("enter your Age:"))
    pcon = int(input("enter your Contact Number :"))
    date_components = input('enter a date formatted as YYYY-MM-DD : ').split('-')
    year, month, day = [int(item) for item in date_components]
    journeyDate = date(year, month, day)
    from_place = "Asansol"
    to_place = "Kolkata"
    ticket_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))

    query= "insert into bus1 (passenger_name,passenger_age,contact,journey_date,from_place,to_place,ticket_number) values(%s,%s,%s,%s,%s,%s,%s)"
    value= (pname, pAge, pcon, journeyDate, from_place, to_place, ticket_number)
    cur.execute(query, value)
    connection.commit()
    print("BUS BOOKED SuccessFully")

    print("------------------")
    print("BOOKING Details:")
    print("------------------")
    print("Passenger Name :", pname);
    print("Passenger Age :", pAge);
    print("contact number  :", pcon);
    print("Journey Date :", journeyDate)
    print("Deperture place :", from_place)
    print("Arrival Place :", to_place)
    print("Ticket Number :", ticket_number)


# '''-------------asansol to Dhanbad busbooking ---------------
def bus2(connection, cur):
    pname = input("enter your name :")
    pAge = int(input("enter your age:"))
    pcon = int(input("enter your contact number :"))
    date_components = input('enter a date formatted as YYYY-MM-DD : ').split('-')
    year, month, day = [int(item) for item in date_components]
    journeyDate = date(year, month, day)
    from_place = "Asansol";
    to_place = "Dhanbad";
    ticket_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))

    query = "insert into bus2 (passenger_name,passenger_age,contact,journey_date,from_place,to_place,ticket_number) values(%s,%s,%s,%s,%s,%s,%s)"
    value = (pname, pAge, pcon, journeyDate, from_place, to_place, ticket_number)
    cur.execute(query, value)
    connection.commit()
    print("BUS BOOKED SuccessFully")

    print("------------------")
    print("BOOKING Details:")
    print("------------------")
    print("Passenger Name :", pname);
    print("Passenger Age :", pAge);
    print("contact number  :", pcon);
    print("Journey Date :", journeyDate)
    print("Deperture place :", from_place)
    print("Arrival Place :", to_place)
    print("Ticket Number :", ticket_number)

#python to mysql connection
def main():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="busbooking"
    )
    cur=connection.cursor()
    if(cur):
        print("database connection established successfully")
        choice = 0
        while choice <= 2:
            print("\n---------Python Travels")
            print("1.Asansol to kolkata")
            print("2.Asansol to dhanbad")
            print("3.Exit application")
            print("\n-----------------")
            choice = int(input("choose your journey :"))
            if(choice==1):
                bus1(connection,cur)
            elif(choice==2):
                bus2(connection,cur)
            else:
                print("Thanks for visiting us")
                exit()
    else:
        print("Databse connection not establissed")



main()

