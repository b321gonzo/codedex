import datetime, bday_messages

today = datetime.date.today()

mnb = datetime.date(2022,5,7) # mnb = my next birthday

days_away = mnb - today

while days_away.days < 0:
    mnb = datetime.date(mnb.year + 1, mnb.month, mnb.day)
    days_away = mnb - today

if today == mnb:
    print(bday_messages.random_message)
elif days_away.days==1:
    print("My birthday is tomorrow! 😀")
else:
    print("My next birthday is " + str(days_away.days) + " days away from today! 🎂")