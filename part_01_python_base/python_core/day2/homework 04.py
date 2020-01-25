initial_speed = float(input("请输入初速度："))
acceleration = float(input("请输入加速度："))
time = float(input("请输入时间："))

distance = initial_speed * time + (acceleration
           * time ** 2) / 2
print("距离是："+str(distance))
