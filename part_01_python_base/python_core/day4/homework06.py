# 100 + 50 + 50 + 25 + 25 +
sum_height = 0
start_height = 100
agent_height = 100
count = 0

while agent_height / 2 > 0.01:
    count += 1
    agent_height /= 2
    sum_height += agent_height * 2
    print(agent_height)
result = sum_height + start_height
print(result) # 13次 299.9755859375
print(count)
