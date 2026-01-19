

def show_sys():
    print("*"*50)
    print("   名片管理系统       ")
    print("1.添加新的名片")
    print("2.删除名片")
    print("3.修改名片")
    print("4.查询名片")
    print("5.显示所有名片")
    print("6.退出系统")
    print("*"*50)


def usr_input():
    num = int(input("请输入功能编号："))
    return num


def mingpian(num):
    if num == 1:
        new_name = input("请输入新的姓名：")
        new_age = input("请输入年龄：")
        new_QQ = input("请输入QQ：")
        new_wechat = input("请输入微信：")
        new_mingpian = {}
        new_mingpian["name"] = new_name
        new_mingpian["age"] = new_age
        new_mingpian["QQ"] = new_QQ
        new_mingpian["wechat"] = new_wechat
        mingpian_list.append(new_mingpian)
    elif num == 2:
        pass
    elif num == 3:
        pass
    elif num == 4:
        pass
    elif num == 5:
        for temp in mingpian_list:
            print(temp)

    else:
        print("输入有误，请重新输入！")
        pass


def main():
    show_sys()
    while True:
        num = usr_input()
        if num == 6:
            break
        else:
            mingpian(num)


if __name__ == "__main__":
    mingpian_list = []
    main()
