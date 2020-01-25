import execjs

with open('translate.js', 'r') as f:
    js_data = f.read()
    # print(js_data)

# 执行js
exec_obj = execjs.compile(js_data)
res = exec_obj.eval('e("china","320305.131321201")')

print(res)

