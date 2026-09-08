from datetime import datetime

log_levels = ("ERROR","INFO","WARNING")


def validate_date_time(date_time:str):
  try:
    format = "%Y-%m-%d %H:%M:%S"
    _ = datetime.strptime(date_time,format).astimezone()
    return True
  except ValueError:
    return False

def validate_log_levels(log:str):
  return log in log_levels
