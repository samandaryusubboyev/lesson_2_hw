import random
import time
from datetime import datetime

info = []

for a in range(30):
    info.append(random.randint(100, 200))

info_l = len(info) - 1
info.sort()
print(info)

search = int(input('Qidirayotgan soningizni kiriting: '))
min = 0
sanoq = 0
print(datetime.now())

while True:
    time.sleep(1)
    sanoq += 1
    mid =  (info_l + min) // 2
    if info[mid] < search:
        min = mid + 1
    elif info[mid] == search:
        print(search)
        print(f"Urinishlar soni {sanoq}")
        break
    else:
        info_l = mid

print(datetime.now())