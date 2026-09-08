from utils import parse_log_lines


def parse_log_file(filepath:str):
    """Return list of parsed log entries (tuples)"""
    entries:list[tuple[str,str,str,str]] = []

    with open(filepath,"r") as file:
      for line in file:
        data = parse_log_lines(line.strip())
        if data is None:
          continue
        entries.append(data)

    return entries

def get_unique_log_levels(logs:list[tuple[str, str, str, str]]):
    """Return set of all log levels found"""
    log_levels_set:set[str] = set()

    for log in logs:
      log_levels_set.add(log[2])

    return log_levels_set


def filter_by_level(logs:list[tuple[str, str, str, str]], level:str):
    """Return list of logs with specific level"""
    level = level.upper()
    specific_level_logs:list[tuple[str, str, str, str]] = []
    for log in logs:
      if level in log:
        specific_level_logs.append(log)

    return specific_level_logs

def extract_errors(logs):
    """Return list of error tuples"""
    pass

def count_logs_by_level(logs):
    """Return dict: {level: count}"""
    pass

def get_logs_after_time(logs, timestamp):
    """Return logs after given timestamp"""
    pass


# print(parse_log_file("./sample.log"))
parsed_logs = parse_log_file("./sample.log")
print("GET UNIQUE LOG LEVELS: \n",get_unique_log_levels(parsed_logs),"\n")
print("FILTER BY LEVLE: \n",filter_by_level(parsed_logs,"error"),"\n")
