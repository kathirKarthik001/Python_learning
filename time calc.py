#program to find the exact time using given seconds
def time (a):
    hour = a//3600
    minutes = (a-hour*3600)//60
    sec = a - hour*3600 - minutes*60
    return hour, minutes,sec
    
a = int(input("enter the seconds:"))
hour, minutes,sec = time(a)

txt = "......{0} hrs....{1} mins....{2} secs....left buddy"

print(txt.format (hour,minutes,sec))