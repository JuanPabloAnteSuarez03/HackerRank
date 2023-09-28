def timeConversion(s):
    hours = 0
    pre_hours = s[0] + s[1]
    minutes = s[3] + s[4]
    minutes_and_seconds = s[2] + s[3] + s[4] + s[5] + s[6] + s[7]
    am_or_pm = s[8] + s[9]
    if(am_or_pm == 'AM' and pre_hours == '12'):
        hours = '00'
        return hours + minutes_and_seconds
    elif(am_or_pm == 'PM' and pre_hours == '12' and int(minutes) > 0):
        return pre_hours + minutes_and_seconds
    elif(am_or_pm == 'PM'):
        hours = int(pre_hours) + 12
        return str(hours) + minutes_and_seconds
    return pre_hours + minutes_and_seconds

print(timeConversion('12:45:54PM'))