
def timeConversion(s):
    # Write your code here
    time = "00:00:00"
    if s.endswith("AM"):
        time = s[0:len(s)-2]
        test_time = int(s[0:2]) - 12
        if test_time == 0:
            
            time = f"00{s[2:len(s)-2]}"
        else:
        # time = str(time) + str(s[2:len(s)-2])
            time = f"{str(time)}" #{s[2:len(s)-2]
    else:
        if int(s[:2]) < 12:
            prefix = str(int(s[:2]) + 12)
            time = prefix + s[2:len(s)-2]
        else:
            time = s[:len(s)-2]
    print(time)
    return time

timeConversion("12:01:00AM")
timeConversion("12:01:00PM")
timeConversion("10:01:00PM")
timeConversion("02:01:00AM")
timeConversion("11:01:00AM")
timeConversion("06:01:00AM")
timeConversion("01:01:00PM")
timeConversion("10:01:00PM")
timeConversion("02:01:00AM")
timeConversion("09:01:00PM")
timeConversion("12:45:54PM")