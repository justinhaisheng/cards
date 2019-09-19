# 空的名片列表
card_lists = []


def show_menu():
    """显示菜单"""
    print("*" * 20)
    print("欢迎使用[cards 管理系统]")
    print("")
    print("1.新建名片")
    print("2.显示全部")
    print("2.查询名片")
    print("")
    print("")
    print("0.退出")
    print("*" * 20)


def create_card():
    print("[新增名片]")
    name_str = input("姓名：")
    qq = int(input("qq:"))
    email = input("请输入邮箱：")
    card_dict = {"name_str", name_str, "qq", qq, "email", email}
    card_lists.append(card_dict)
    print("[名片:%s] 增加成功" % name_str)


def show_all():
    print("[显示所有名片]!")


def search_card():
    print("[查询名片]")
