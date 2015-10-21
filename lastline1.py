import time

attemps = 600
wait_sec = 5
fname = "/var/log/messages"

with open(fname, "r") as f:
    where = f.tell()
    for i in range(attemps):
        line = f.readline()
        if not line:
            time.sleep(wait_sec)
            f.seek(where)
        else:
            print line, # already has newline


