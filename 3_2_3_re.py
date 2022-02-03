import sys
import re

pattern = r'z.{3}z'
for line in sys.stdin:
    line = line.rstrip()
    # process line
    if re.match(pattern, line):
        print(line)
