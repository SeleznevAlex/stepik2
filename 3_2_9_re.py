import sys
import re

pattern = r'(\w)\1*'
for line in sys.stdin:
    line = line.rstrip()
    # process line

    match = re.match(pattern, line)
    print(re.sub(pattern, r'\1', line))
