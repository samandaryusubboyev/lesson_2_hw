import time
from datetime import datetime
info = [23, 878, 2, 56, 24, 98, 224, 1, 114, 119, 7, 6]
print(info)
son = int(input("Qidirayotgan soningizni kiriting: "))
urinish = 0
print(datetime.now())
for z in info:
    time.sleep(1)
    urinish += 1
    if z == son:
        print(z)
        print(f"{z} sonini topish uchun {urinish} ta qadam kerak bo'ldi")
print(datetime.now())

