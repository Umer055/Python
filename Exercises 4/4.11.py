year=int(input("Enter the year:\n"))
int_month=int(input("Enter the number of the month:\n"))
if int_month>0 and int_month<13:
    if int_month==1:
        month="January"
        days=31
        print("The year is",year,"and the month is",month,"and the days of the month are",days)
    elif int_month==2:
        month="February"
        if year%4==0:
            days=29
            print("The year is",year,"and the month is",month,"and the days of the month are",days)
        else:
            days=28
            print("The year is",year,"and the month is",month,"and the days of the month are",days)
    elif int_month==3:
        month="March"
        days=31
        print("The year is",year,"and the month is",month,"and the days of the month are",days)
    elif int_month==4:
        month="April"
        days=30
        print("The year is",year,"and the month is",month,"and the days of the month are",days)
    elif int_month==5:
        month="May"
        days=31
        print("The year is",year,"and the month is",month,"and the days of the month are",days)
    elif int_month==6:
        month="June"
        days=30
        print("The year is",year,"and the month is",month,"and the days of the month are",days)
    elif int_month==7:
        month="July"
        days=31
        print("The year is",year,"and the month is",month,"and the days of the month are",days)
    elif int_month==8:
        month="August"
        days=31
        print("The year is",year,"and the month is",month,"and the days of the month are",days)
    elif int_month==9:
        month="September"
        days=30
        print("The year is",year,"and the month is",month,"and the days of the month are",days)
    elif int_month==10:
        month="Octuber"
        days=31
        print("The year is",year,"and the month is",month,"and the days of the month are",days)
    elif int_month==11:
        month="November"
        days=30
        print("The year is",year,"and the month is",month,"and the days of the month are",days)
    else :
        month="December"
        days=31
        print("The year is",year,"and the month is",month,"and the days of the month are",days)
else:
    print("You have not entered the correct month number")

