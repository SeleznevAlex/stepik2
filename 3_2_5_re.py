import sys
import re

pattern = r'.*\b(\w+)\1\b.*'
for line in sys.stdin:
    line = line.rstrip()
    # process line
    if re.match(pattern, line):
        print(line)
