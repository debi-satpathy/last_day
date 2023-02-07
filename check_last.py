import datetime
def last_day_of_month(day):
    next_month = day.replace(day=28) + datetime.timedelta(days=4)
    return next_month - datetime.timedelta(days=next_month.day)
end_date=[]
req_date_29=""
req_date_30=""
req_date_31=""
#print("Here are the last dates of the months")
for month in range(1,13):
    #print(last_day_of_month(datetime.date(2020,month,1)))
    end_date.append(last_day_of_month(datetime.date(2020,month,1)))


print("Here are the last but 2 days if available")
for i in end_date:
    #print(i.strftime('%y-%m-%d %a %H:%M:%S'))
    date_req=int(i.strftime('%d'))
    if date_req== 29:
        req_date_29+=str(i)+ "\n"
        #print(i)
    if date_req== 31:
        get_30 = i - datetime.timedelta(days=1)
        get_29= i - datetime.timedelta(days=2)
        req_date_29+=str(get_29)+ "\n"
        req_date_30+=str(get_30)+ "\n"
        req_date_31+=str(i)+ "\n"
    elif date_req==30:
        get_29 = i - datetime.timedelta(days=1)
        req_date_29+=str(get_29)+ "\n"
        req_date_30+=str(i)+ "\n"
    #print("*"*20)
print("29th of the Month")
print(req_date_29)
print("30th of the Month")
print(req_date_30)
print("31st of the Month")
print(req_date_31)