import hashlib
test_str = "a"
e01 = hashlib.md5()
e01.update(test_str.encode(encoding="utf-8"))

print(test_str)
print(e01.hexdigest())