import time
from datetime import datetime

jadval = list(set([1, 1, 6, 13, 14, 14, 23, 23, 26, 26, 30, 31, 32, 32, 37, 42, 44, 47, 48, 50]))



jadval_l = len(jadval) - 1
jadval.sort()
print(jadval)
search = int(input("Kerakli sonni kiriting: "))
minimum = 0
jadval_l = len(jadval) - 1
s = 0
print(datetime.now())
while True:
    time.sleep(1)
    s += 1
    middle = (jadval_l + minimum) // 2
    if jadval[middle] < search:  # false
        minimum = middle + 1
    elif jadval[middle] == search:
        print(search)
        print(f"Urinishlar soni {s}")
        break
    else:
        jadval_l = middle

print(datetime.now())