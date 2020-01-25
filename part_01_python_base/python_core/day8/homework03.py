str_project = "　校　训：自　强不息、厚德载物。　　"
# 1.查找空格的数量
# 2.删除字符串前后空格
# 3.删除字符串所有空格
# 4.查找"载物"的位置
# 5.判断字符串是否以"校训"开头.

project_1 = str_project.count("　")
print(project_1)

project_2 = str_project.strip()
print(project_2)

project_3 = str_project.replace("　", "")
print(project_3)

project_4 = str_project.find("载物")
print(project_4)  # str_project[13] = "载"
#                   str_project[14] = "物"

print(str_project.startswith("校训"))
