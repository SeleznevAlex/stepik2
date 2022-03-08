import csv
import time
from collections import Counter

arrCrimes = []
with open("Crimes.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        date = row['Date']
        struct_date = time.strptime(date, "%m/%d/%Y %I:%M:%S %p")
        if struct_date.tm_year == 2015:
            arrCrimes.append(row['Primary Type'])
    countCrimes = Counter(arrCrimes)
    print(max(arrCrimes, key=lambda k: countCrimes[k]))
