def add_time(start, duration, start_day=None):
  # deal with the start time first
  start_time, period = start.split()
  start_hour, start_minute = map(int, start_time.split(':'))
  start_hour = start_hour % 12 + 12 * (period == 'PM')

  # deal with the duration of time here
  duration_hour, duration_minute = map(int, duration.split(':'))

  # calculate the number of minutes
  total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute

  # calculate new time
  new_hour = total_minutes // 60 % 24
  new_minute = total_minutes % 60

  # if it needs to be the next day or not
  days_later = total_minutes // (24 * 60)
  next_day_str = " (next day)" if days_later == 1 else "" if days_later == 0 else f" ({days_later} days later)"

  # deals with the day of the week arg
  if start_day:
      start_day = start_day.capitalize()
      days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
      start_index = days_of_week.index(start_day)
      new_day_index = (start_index + days_later) % 7
      new_day = days_of_week[new_day_index]
      day_str = f", {new_day}"
  else:
      day_str = ""

  # deals with either AM or PM
  new_period = "AM" if new_hour < 12 else "PM"

  # format result
  result = f"{new_hour % 12}:{new_minute:02d} {new_period}{day_str}{next_day_str}"

  # print the result
  return print(result)
