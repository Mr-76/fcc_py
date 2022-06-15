def add_time(hora_inicial,hora_adicional,day = ""):
    WEEK_DAYS= ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]
    
    #usar formato 24 horas
    list_time = hora_inicial.split(" ")
    list_time = list_time[0].split(":") + [list_time[1]]
    list_time.append(day)
    list_add_time = hora_adicional.split(":")

    print(list_time)

    hour = int(list_time[0])
    minute = int(list_time[1])
    hour_add = int(list_add_time[0])
    minute_add = int(list_add_time[1])

    if (list_time[2] == "AM"):
        add_12 = 0
    elif(list_time[2] == "PM"):
        add_12 = 12
    else:
        pass

    if (hour == 12 and list_time[2] == "AM"):
        hour = 0
    elif (hour == 12 and list_time[2] == "PM"):
        hour = 12
        add_12 = 0
    else:
        pass
   
    hour  = hour + add_12 # converting to 24 h

    final_hour = hour + hour_add 
    final_minute = minute + minute_add

    final_hour = (final_hour) + (final_minute//int(60)) 
    
    final_minute = (final_minute//60  + final_minute % 60) 
    string_time_day = '' 
    if (final_hour < 24):
        final_hour = final_hour
        string_time_day = ""
    else:
        days = final_hour//24
        final_hour = final_hour % 24
        if (days == 1):
            string_time_day = "(next day)"
        elif (days > 1):
            string_time_day = ("{} days later".format(days))
    
    if (final_hour > 12 and final_hour != 24):
        final_hour = (final_hour - 12)
        string_time = "PM"
    elif (final_hour < 12):
        final_hour = (final_hour - 0)
        string_time = "AM"
    elif (final_hour == 24):
        final_hour = 12
        string_time = "AM"
    elif (final_hour == 12):
        final_hour = 12
        string_time = "PM"
    else:
        print("dont know that case")
    
    return ("{}:{} {} {} ".format(final_hour,final_minute,string_time,string_time_day))

def main():
    print(add_time("11:43 PM","24:20","tueSday"))
    print(add_time("4:00 PM", "3:11","monday"))

if  __name__ == "__main__":
    main()
