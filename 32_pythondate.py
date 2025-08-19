import datetime 
x = datetime.datetime.now()
print(x)     #Output: 2025-07-29 13:30:00.948196



# This will return the year and name of the weekday 
import datetime 
x = datetime.datetime.now()
print(x.year)   #Output: 2025
print(x.strftime("%A"))   #Output:   Tuesday

# Creating the Date Objects  - you can use datetime() for creating the date. 
import datetime 
x = datetime.datetime( 2022, 5, 16)
print(x) 

# The strftime() method
import datetime
x = datetime.datetime(2022, 6, 1)     #Output: 2022-05-16 00:00:00
print(x.strftime("%B"))    #Output: June

'''A reference of all the legal format datetime codes 
%a - weekday - Wed
%A - weekday - Wednesday
%w - wednesday as a number - 3
%d - days 1-31 - 31
%b - month short - Dec 
%B - month - December
%m - month as number - 12 
%y - year short - 22
%Y - year - 2022 
%H - hour24 - 17 
%I - Hour12 - 05 
%p - am/pm  - PM 
%M - minute - 41
%S - second - 30 
%f - microsecond 0000000 - 999999 - 365874
%Z - timezone - CST 
%j - daynumber of year - 365 
%U - week number - 52 
%C - century - 2000 / 20* 
%x - local ver of date - 05/15/2022'''