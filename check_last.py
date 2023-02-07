import datetime
def last_day_of_month(day):
    next_month = day.replace(day=28) + datetime.timedelta(days=4)
    return next_month - datetime.timedelta(days=next_month.day)

last_day=[]
end_31=[]
end_30=[]
print("Here are the last dates of the months")
for month in range(1,13):
    print(last_day_of_month(datetime.date(2020,month,1)))
    last_day.append(last_day_of_month(datetime.date(2020,month,1)))

print("Here are the last but 2 days if available")
for i in last_day:
    #print(i.strftime('%y-%m-%d %a %H:%M:%S'))
    date_req=int(i.strftime('%d'))
    if date_req== 31:
        get_30 = i - datetime.timedelta(days=1)
        get_29= i - datetime.timedelta(days=2)
        #print("31 date append to 31 list")
        print(get_30)
        print(get_29)
    elif date_req==30:
        #print("append to 3 list")
        get_29 = i - datetime.timedelta(days=1)
        print(get_29)
    print("*"*20)
