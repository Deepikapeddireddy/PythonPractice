def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return 1
      else:
        return 0
    else:
      return 1
  else:
    return 0

def days_in_month(year , month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if month ==2 and is_leap(year) :
    return 29
  return month_days[month -1]
#   if month == 2:
#     if is_leap(year):
#       return  29
#     else:
#       return 28
#   else:
#     return month_days[month-1]
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
if month >12 or month <=0:
    print('You have entered invalid month😒😒. check it out...🙄🙄')
else:
    days = days_in_month(year, month)
    print(days)
