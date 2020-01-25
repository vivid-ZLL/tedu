set_manager = {"曹操", "刘备", "孙权"}
set_tec = {"曹操", "刘备", "张飞", "关羽"}
print("1.是经理也是技术的人:", ",".join(list(set_manager & set_tec)))
print("2.是经理,不是技术的人:", ",".join(list(set_manager - set_tec)))
print("3.是技术不是经理的人", ",".join(list(set_tec - set_manager)))
print("4.张飞是经理吗?", "张飞" in set_manager)
print("5.身兼一职的是:", ",".join(list(set_manager ^ set_tec)))
print("6.经理和技术共有人数:",len(set_manager | set_tec))
