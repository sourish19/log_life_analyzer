from pathlib import Path

from utils import is_after_timestamp, parse_log_lines, validate_date_time


def parse_log_file(filepath:str):
    """Return list of parsed log entries (tuples)"""
    path = Path(filepath)

    if path.exists() is False:
      return None

    entries:list[tuple[str,str,str]] = []

    with open(filepath,"r") as file:
      for line in file:
        data = parse_log_lines(line.strip())
        if data is None:
          continue
        entries.append(data)

    return entries

def get_unique_log_levels(logs:list[tuple[str, str, str]]):
    """Return set of all log levels found"""
    log_levels_set:set[str] = set()

    for log in logs:
      log_levels_set.add(log[1])

    return log_levels_set


def filter_by_level(logs:list[tuple[str, str, str]], level:str):
    """Return list of logs with specific level"""
    level = level.upper()
    specific_level_logs:list[tuple[str, str, str]] = []
    for log in logs:
      if level in log:
        specific_level_logs.append(log)

    return specific_level_logs

def extract_errors(logs:list[tuple[str, str, str]]):
    """Return list of error tuples"""
    return filter_by_level(logs,"error")

def count_logs_by_level(logs:list[tuple[str, str, str]]):
    """Return dict: {level: count}"""
    logs_count: dict[str,int] = {}

    for log in logs:
      level = log[1]
      if level in logs_count:
        logs_count[level] += 1
      else:
        logs_count[level] = 1

    return logs_count

def get_logs_after_time(logs:list[tuple[str, str, str]], timestamp:str):
    """Return logs after given timestamp"""
    if validate_date_time(timestamp) is False:
      print("Invalid Timestamp")
      return

    filtered_logs:list[tuple[str, str, str]] = []

    for log in logs:
      log_timestamp = log[0]

      if is_after_timestamp(log_timestamp,timestamp) is True:
        filtered_logs.append(log)

    return filtered_logs


def main():
  parsed_logs = parse_log_file("./sample.log")
  reference_timestamp = "2024-01-15 10:20:00"

  if parsed_logs is None or not parsed_logs :
    print("File dosen't exists or it's empty")
    return

  print("GET UNIQUE LOG LEVELS: \n",get_unique_log_levels(parsed_logs),"\n")
  print("FILTER BY LEVLE: \n",filter_by_level(parsed_logs,"error"),"\n")
  print("COUNT LOGS BY LEVLE: \n",count_logs_by_level(parsed_logs),"\n")
  print("GET LOGS AFTER TIME: \n",get_logs_after_time(parsed_logs,reference_timestamp),"\n")


main()
