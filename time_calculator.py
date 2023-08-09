def add_time(start, duration, day=False):

  daysI ={"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}

  daysA = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]
  
  
  duration_T = duration.partition(":")
  print(duration_T)
  duration_H = int(duration_T[0])
  duration_M = int(duration_T[2])

  start_T = start.partition(":")
  start_M_T = start_T[2].partition(" ")
  start_H = int(start_T[0])
  star_M = int(start_M_T[0])
  am_or_pm = start_M_T[2]
  am_and_pm_flip = {"AM": "PM", "PM": "AM"}
  
  amount_of_days = int(duration_H / 24)
  
  end_M = star_M + duration_M
  if(end_M >= 60):
    start_H += 1
    end_M = end_M % 60
  amount_of_am_pm_flip = int((start_H + duration_H) / 12)  
  end_H = (start_H + duration_H) % 12
  
  end_M = end_M if end_M > 9 else "0" + str(end_M)
  end_H = end_H = 12 if end_H == 0 else end_H
  if(am_or_pm == "PM" and start_H + (duration_H % 12) >= 12):
    amount_of_days += 1

  am_or_pm = am_and_pm_flip[am_or_pm] if amount_of_am_pm_flip % 2 == 1 else am_or_pm

  returnTime = str(end_H) + ":" + str(end_M) + " " + am_or_pm
  if(day):
    day = day.lower()
    index = int((daysI[day]) + amount_of_days) % 7
    new_day = daysA[index]
    returnTime += ", " + new_day
    
  if(amount_of_days == 1):
    return returnTime + " " + "(next day)"
  elif(amount_of_days > 1):
    return returnTime + " (" + str(amount_of_days) + " days later)"

  return returnTime