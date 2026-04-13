import time

DEBUG = 0
INFO = 1
WARNING = 2
ERROR = 3

LABELS = { DEBUG: "DEBUG", INFO: "INFO", WARNING: "WARN", ERROR: "ERROR" }

def timestamp():
  now = time.localtime()

  return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
    now[0], now[1], now[2],  # year, month, day
    now[3], now[4], now[5]   # hour, minute, second
  )

def log(level, *args):
  msg = f"[{timestamp()}] [{LABELS[level]}] {" ".join(str(a) for a in args)}"

  print(msg)

  if level > DEBUG:
    with open("app.log", "a") as f:
      f.write(msg + "\n")

def debug(*args):
  log(DEBUG, *args)

def info(*args):
  log(INFO, *args)

def warning(*args):
  log(WARNING, *args)

def error(*args):
  log(ERROR, *args)
