# from datetime import datetime as dtdt, timezone as tz,  timedelta as td
# now = dtdt.now()

# print(dtdt.strptime("01/03/1998, 12:00:45","%d/%m/%Y, %H:%M:%S"))

# print(now.isoformat())
# print(dtdt.fromisoformat("2024-12-19T08:30:00.000000"))

# dt1 = dtdt(2023, 3, 14, 12, 0)
# dt2 = dtdt(2020, 3, 15, 11, 0)
# # print(dt1)
# # print(dt2)
# # print(dt1==dt2)
# # print(dir(td))
# tz1=tz(td(hours=2), "UTC+2")
# dt1 = dtdt(2023, 3, 14, 12, 0, tzinfo=tz1)

# # print(dt1)

# import time
# now = time.time()
# # print(now)
# rnow=time.ctime(now)
# # print(rnow)

# # t1=time.struct_time([2023,12,1,12,35,44,1,125,-1])
# # print(t1)

# print(now)
# start=time.perf_counter()
# time.sleep(4)
# end=time.perf_counter()
# print(end-start)

import random
import math
# dice=random.randint(1,6)
# print(dice)

# f1=random.random()
# print(f1)
print(random.randrange(11))
print(random.randint(0,10))

cards=[2,3,7,3,5,8,5,8,5,"j","k","a"]
print(cards)
random.shuffle(cards)
print(cards)
print(math.p)
print(math.pow())