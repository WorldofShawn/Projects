def add_time (start, duration, day=None):
    
    starth= start.split(":")[0]
    startm=start.split(":")[1].split()[0]
    starttimeAMPM = start.split(":")[1].split()[1]
    durationh = duration.split(":")[0]
    durationm= duration.split(":")[1]
    AMPMswap = {"AM":"PM", "PM":"AM"}
    week = {"Monday":0, "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "Saturday":5, "Sunday":6}
    weekarray = ("Monday", "Tuesday", "Wednesday", "Thursday","Friday","Saturday","Sunday")

    finalh = int(starth) + int(durationh)
    finalm = int(startm) + int(durationm)
    
    if finalm >= 60:
        finalh += 1
        finalm -= 60

    totalday=finalh/24

    #AM to PM vice versa swap
    if (int(finalh/12))%2!=0:
        starttimeAMPM = AMPMswap[starttimeAMPM]

    if totalday < 1:
        if finalh>=12 and starttimeAMPM == "AM":
            daysgonetxt = "(next day)"
        else:
            daysgonetxt = ""
    elif totalday > 1:
        totalday = round((finalh/24)+0.5)
        daysgonetxt = "(" + str(totalday) + " days later)"
    else:
        daysgonetxt = ""

    if day!=None:
        if totalday >=1:
            dayoftheweek = totalday%7 + week[day]
        
            if dayoftheweek > 6:
                dayname = weekarray [dayoftheweek-7]
            else:
                dayname = weekarray[dayoftheweek]
        else:
            dayname = day
    
    finalh = str(finalh % 12)
    
    #Formatting time text
    if int(finalh) <= 9:
        if int(finalh) == 0:
            finalh = "12"

    if finalm <= 9:
        finalm = "0"+ str(finalm)
    else:
        finalm = str(finalm)

    if day == None:
        time = finalh + ":" + finalm + " " + starttimeAMPM + " " + daysgonetxt
    else:
         time = finalh + ":" + finalm + " " + starttimeAMPM + ", " + dayname + " " + daysgonetxt       
    


    return time

print (add_time("3:00 PM", "3:10"))
print (add_time("11:30 AM", "2:32", "Monday"))
print (add_time("11:43 AM", "00:20"))
print (add_time("10:10 PM", "3:30"))
print (add_time("11:43 PM", "24:20", "Tuesday"))
print (add_time("6:30 PM", "205:12"))