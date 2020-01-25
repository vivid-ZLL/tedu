import bll_of_search as search
import os


class DictionaryViewer:
    def __init__(self):
        self.search = search.SearchDatabase()
        self.account = self.search.account

    def main(self):
        while True:
            self.print_primary_msg()
            self.choose_primary_menu()

    def choose_secondary_menu(self):
        while True:
            self.print_secondary_menu()
            select_code = input("请输入选项:")
            if select_code == "1":
                self.search.search_word(input("请输入单词:"))
            elif select_code == "2":
                self.search.print_history()
            elif select_code == "3":
                return False
            else:
                print("输入有误,请重新输入")

    def print_secondary_menu(self):
        menu_str = """
                    请选择功能
        ==================================
        1.查询    2.显示查询历史    3.注销登录
        ==================================
        """
        print(menu_str)

    def print_primary_msg(self):
        welcome_str = """
          欢迎使用英语字典查询系统
        ==========================
        1.登录     2.注册     3.退出
        ==========================
        """
        print(welcome_str)

    def choose_primary_menu(self):
        select_code = input("请选择功能:")

        if select_code == "1":
            if not self.verify_account():
                return
            self.choose_secondary_menu()

        elif select_code == "2":
            name = self.check_name()
            if not name:
                return
            password = self.check_password()
            if not password:
                return
            self.account.register_account(name, password)
            self.choose_secondary_menu()

        elif select_code == "3":
            os._exit(0)
        else:
            print("错误的选项,请重新输入")
            return False

    def check_password(self):
        while True:
            password = input("请输入密码,空行返回上一级:")
            if not password:
                return
            if self.account.check_password(password):
                break
        return password

    def check_name(self):
        while True:
            name = input("请输入用户名,空行返回上一级:")
            if not name:
                return
            if self.account.check_user_name(name):
                break
        return name

    def verify_account(self):
        while True:
            name = input("请输入用户名,空行返回:")
            if not name:
                return
            password = input("请输入密码,空行返回:")
            if not password:
                return
            if self.account.login(name, password):
                return True


if __name__ == "__main__":
    d01 = DictionaryViewer()
    d01.main()
