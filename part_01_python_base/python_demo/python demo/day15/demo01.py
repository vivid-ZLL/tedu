"""
    模块相关概念
"""

# from module01 import *
#
# fun01()
# # 1. 隐藏成员，不能通过from 模块 import × 形式导入
# _fun02()


# from module01 import _fun02
#
# # 隐藏成员，可以通过其他形式调用
# _fun02()


# 2. 通过__all__指定可导出成员
from module01 import *

MyClass.fun03()
_fun02()

# 3.可以通过该属性，查看文档注释
print(__doc__)

# 4.返回当前模块的绝对路径（从系统根目录开始计算的）
print(__file__)


# 5.
# 现象：
# 主模块叫做：__main__
# 非主模块叫做：真名
print(__name__)
# 作用1： 不是主模块不执行。(测试代码)
# 作用2： 只有是主模块才执行。(主模块代码)
# 使用：
if __name__ == "__main__":
    pass