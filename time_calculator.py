import re
def add_time(start, duration, week_day = False):

  # init variable
  day_count = 0

  # lowercase all weekday inputs
  # check day of week
  if(week_day):
    weekday = week_day.lower()
    match weekday:
      case 'sunday':
        day_num = 0
      case 'monday':
        day_num = 1
      case 'tuesday':
        day_num = 2  
      case 'wednesday':
        day_num = 3  
      case 'thursday':
        day_num = 4
      case 'friday':
        day_num = 5
      case 'saturday':
        day_num = 6
    # for correct casing on print
    days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

  # separate nums and AM/PM from start; uppercase AM/PM
  a = re.findall("\d+", start)
  hour =  int(a[0])
  min = int(a[1])
  a = re.findall("[A-Z]+", start.upper())
  noon = a[0]

  # separate duration into hours and minutes
  a = re.findall("\d+", duration)
  dur_hours =  int(a[0])
  dur_mins = int(a[1])

  # add minutes together. if min >= 60, add 1 to hours - sub 60 from mins
  # add hours together. if hours >= 12, sub 12, switch noon to AM/PM, add to day num if going to AM
  new_hour = hour + dur_hours
  new_min = min + dur_mins
  while(new_min >= 60):
    new_min -= 60
    new_hour += 1

  while(new_hour >= 12):
    new_hour -= 12
    # switch AM/PM
    if(noon == 'AM'):
      noon = 'PM'
    elif(noon == 'PM'):
      noon = 'AM'
      day_count += 1
    else:
      return 'invalid format'
      
  # determine # of days passed
  if(day_count == 0):
    days_later = ""
  elif(day_count == 1):
    days_later = " (next day)"
  elif(day_count > 1):
    days_later = " (" + str(day_count) + " days later)"
  
  # if day of week provided, determine new day. add day_num (rep of day of week) to day_count
  # this gets day_count starting with the correct starting day of week
  if(week_day):
    day_count += day_num
    while(day_count >= 7):
      day_count -= 7
    new_day = ", " + str(days[day_count])
  else:
    new_day = ""

 # if hour is 0, change into 12
  if(new_hour == 0):
    h = str(12)
  else:
    h = str(new_hour)
  
 # if min is 0, print as :00; if min is 1 digit, add a leading zero
  if(new_min == 0):
    m = ":00 "
  elif(new_min < 10):
    m = ':0' + str(new_min) + " "
  else:
    m = ":" + str(new_min) + " "
  
  new_time = h + m + noon + new_day + days_later
  return new_time