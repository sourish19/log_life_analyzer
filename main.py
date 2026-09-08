from utils import validate_date_time


def parse_log_lines(log:str):
  """Return tuple of log (day,time,level,message)"""
  splited_log = log.split(" ")
  date_time = splited_log[0] + " " + splited_log[1]
  is_valid_date_time = validate_date_time(date_time)

  if is_valid_date_time is False:
    print("Invalid log")
    return

  level = splited_log[2]

  return (splited_log[0],splited_log[1])



def parse_log_file(filepath:str):
    """Return list of parsed log entries (tuples)"""
    entries:list[str] = []
    with open(filepath,"r") as file:
      for line in file:
        # entries.append(line.strip())
        parse_log_lines(line.strip())

    # return tuple(entries)

    # [(date,time,lvl,mssg),]

def get_unique_log_levels(logs):
    """Return set of all log levels found"""
    pass

def filter_by_level(logs, level):
    """Return list of logs with specific level"""
    pass

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
parse_log_file("./sample.log")
