"""
4. 已知：加速度，初速度，时间
　　计算：距离
　　加速度　＝　(距离 - 初速度　×　时间) * 2 / 时间平方

    距离 = 加速度 * 时间平方 *0.5 ＋　初速度 * 时间
"""
accelerated_speed = int(input("请输入加速度:"))
time = int(input("请输入时间："))
initial_voloctiy = int(input("请输入初速度："))
distance = accelerated_speed * time ** 2 * 0.5 + initial_voloctiy * time
print("距离是：" + str(distance))
