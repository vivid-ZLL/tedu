"""
    列表助手模块 v2.0
"""


class ListHelper:
    """
        列表助手类
    """

    @staticmethod
    def is_sub_list(child_list, father_list):
        try:
            for item in child_list:
                father_list.remove(item)
            return True
        except Exception:
            return False


if __name__ == '__main__':
    l01 = ListHelper()
    print(l01.is_sub_list([7, 7, 7, ], [7, 7, 7, 7]))
    print(l01.is_sub_list([7, 7, 7, ], [7, 7]))
