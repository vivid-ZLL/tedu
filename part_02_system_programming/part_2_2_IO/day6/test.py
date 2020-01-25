import random
from list_helper import *
list_landlord = []

list01 = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6,
          7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11,
          12, 12, 12, 12, 13, 13, 13, 13, 14, 15
          ]

random.shuffle(list01)
list_landlord.append(list01.pop(-1))
list_landlord.append(list01.pop(-1))
list_landlord.append(list01.pop(-1))
list_player01 = list01[0:16]
list_player02 = list01[17:33]
list_player03 = list01[34:60]
c01 = ListHelper()
c01.order_by_rise(list_player01,lambda item : item)
c01.order_by_rise(list_player02,lambda item : item)
c01.order_by_rise(list_player03,lambda item : item)


print(list01)
print(list_player01)
print(list_player02)
print(list_player03)

print(list_landlord)

