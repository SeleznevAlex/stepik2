import sys
import re

pattern = r'\b(\w)(\w)(\w*)\b'
for line in sys.stdin:
    line = line.rstrip()
    # process line

    match = re.match(pattern, line)
    print(re.sub(pattern, r'\2\1\3', line))
