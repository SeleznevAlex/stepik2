import sys
import re

pattern = r'.*cat.*cat.*'
for line in sys.stdin:
    line = line.rstrip()
    if re.match(pattern, line):
        print(*re.findall(pattern, line))
