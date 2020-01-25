#检查括号匹配的程序by Roy#
from sstacks import *
st = SStack()
class BracketError(Exception):
    pass

str_target = """Thanks to {the} flexibility of Python and the [powerful] ecosystem of 
pac(kages, {the Azure (CLI)} supports features such as autoc]ompletion 
(in shells that support it), persistent credentials, JMESPath 
result parsing, lazy initialization, network-less unit tests, and more."""

for i in range(len(str_target)):
    if str_target[i] in ("(", "[", "{"):
        st.push(str_target[i])

    elif str_target[i] in (")", "]", "}"):
        temp = st.pop()
        print((temp, str_target[i]))  # 打印检查括号
        if not (temp, str_target[i]) in (('{', '}'), ('[', ']'), ('(', ')')):
            raise BracketError("括号格式不对头oh yeah", (temp, str_target[i]), i)

print("格式检查完毕")
# 异常1 : (()
# 异常2 : ())
