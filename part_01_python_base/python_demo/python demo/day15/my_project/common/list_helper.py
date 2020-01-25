# 15:50
print("common -- list_helper")

import sys
# 如果不再pycharm中运行当前模块，则导包失败.
# 将项目根目录加入path中，导包才会成功.
sys.path.append("/home/tarena/1905/month01/code/day15/my_project")
print(sys.path)

from main import *

main_fun01()




