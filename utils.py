from datetime import datetime

LOG_LEVELS = ("ERROR","INFO","WARNING")
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

def parse_log_lines(log:str):
  """Return tuple of log (day,level,message)"""
  splited_log = log.split(" ",3)

  if len(splited_log) < 3:
    return

  date = splited_log[0]
  time = splited_log[1]

  if validate_date_time(date + " " + time) is False:
    return

  level = splited_log[2]

  if validate_log_levels(level) is False:
    return

  message = splited_log[3:]

  return (date + " " + time,level," ".join(str(x) for x in message))

def validate_date_time(date_time:str):
  try:
    _ = datetime.strptime(date_time,DATETIME_FORMAT).astimezone()
    return True
  except ValueError:
    return False

def validate_log_levels(log:str):
  return log in LOG_LEVELS

def is_after_timestamp(log_timestamp:str,reference_timestamp:str):
  log_time = datetime.strptime(log_timestamp,DATETIME_FORMAT).astimezone()
  reference_time = datetime.strptime(reference_timestamp,DATETIME_FORMAT).astimezone()

  return log_time > reference_time
