from datetime import datetime

log_levels = ("ERROR","INFO","WARNING")

def parse_log_lines(log:str):
  """Return tuple of log (day,time,level,message)"""
  splited_log = log.split(" ")
  date = splited_log[0]
  time = splited_log[1]

  if validate_date_time(date + " " + time) is False:
    # print("Invalid date & Time")
    return

  level = splited_log[2]

  if validate_log_levels(level) is False:
    # print("Invalid level")
    return

  message = splited_log[3:]

  return (date,time,level," ".join(str(x) for x in message))

def validate_date_time(date_time:str):
  try:
    format = "%Y-%m-%d %H:%M:%S"
    _ = datetime.strptime(date_time,format).astimezone()
    return True
  except ValueError:
    return False

def validate_log_levels(log:str):
  return log in log_levels
