"""
3.  按照以下格式，输出变量name = "悟空",age = 800,score = 99.5
     我叫xx,年龄是xx,成绩是xx。
"""
name = "悟空"
age = 800
score = 99.5
message = "我叫%s,年龄是%d,成绩是%.1f。" % (name, age, score)
print(message)
