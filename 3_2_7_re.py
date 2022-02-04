import sys
import re

pattern = r'\b[Aa]+\b'
for line in sys.stdin:
    line = line.rstrip()
    # process line
    print(re.sub(pattern, "argh", line, count=1))
