def add_time(start, duration, day = False):
  #takes given numbers and separtes them into different variables/lists
  startList = start.split()
  morn_eve = startList[1]
  startTime = startList[0].split(':')
  durationTime = duration.split(':')

  #Figures out the what new time is
  newMinutes = (int(startTime[1]) + int(durationTime[1])) % 60
  if len(str(newMinutes)) == 1:
    newMinutes = '0' + str(newMinutes)
  extraHours = int((int(startTime[1]) + int(durationTime[1])) / 60)
  newHours = (int(startTime[0]) + int(durationTime[0]) + extraHours) % 12
  if newHours == 0:
    newHours = 12

  #Figures out how many half days have past and switches AM/PM if needed.
  halfDaysPast = int((int(startTime[0]) + int(durationTime[0]) + extraHours) / 12)

  if halfDaysPast % 2 == 1:
    if morn_eve == 'PM':
      newMornEve = 'AM'
    elif morn_eve == 'AM':
      newMornEve = 'PM'
  else:
    newMornEve = morn_eve

  if morn_eve == 'PM':
    halfDaysPast += 1
  
  fullDaysPast = int(halfDaysPast / 2)

  #Figures out the new day of the week if needed
  if day != False:
    days_of_the_week = ['monday', 'tuesday', 'wednesday', 'thursday' ,'friday', 'saturday', 'sunday']

    try:
      dayIndex = days_of_the_week.index(day.lower())
    except:
      return "Error: Day of the week was typed in wrong."
    newWeekDay = (fullDaysPast % 7) + dayIndex
    if newWeekDay > 6:
      newWeekDay -= 7
    newWeekDay = days_of_the_week[newWeekDay]
  
  #Prints new time, how many days have past, and the new day if needed
  new_time = str(newHours) + ':' + str(newMinutes) + " " + newMornEve
  if day != False:
    new_time += ", " + newWeekDay.capitalize()
  if fullDaysPast == 1:
    new_time += " (next day)"
  elif fullDaysPast > 1:
    new_time += " (" + str(fullDaysPast) + " days later)"

  return new_time
