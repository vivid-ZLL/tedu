import time

temp = open("time_recorder", "a+")
temp_read = open("time_recorder", "r")

count_times_of_record = 0
for re in temp_read:
    count_times_of_record += 1
    print(re)

count = count_times_of_record
while True:
    count += 1
    tuple_time = time.localtime()
    re = str("%s. " % count + time.strftime("%Y-%m-%d   %H:%M:%S", tuple_time))
    print(re)
    temp.write("%s\n" % re)
    time.sleep(1)
