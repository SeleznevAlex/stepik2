import sys
import re

pattern = 'human'
for line in sys.stdin:
    line = line.rstrip()
    # process line
    print(re.sub(pattern, 'computer', line))
