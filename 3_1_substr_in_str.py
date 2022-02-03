s = input()
a = input()
b = input()
count = 0

print(a.replace.__doc__)

while a in s:
    count += 1
    s = s.replace(a, b)
    if count >= 1000:
        print('Impossible')
        break
if count < 1000:
    print(count)
