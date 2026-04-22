class Dog:
    # 私有方法
    def __send_msg(self):
        print("--------正在发生短信-----------------")

    # 共有方法
    def send_msg(self, new_money):
        if new_money > 10000:
            self.__send_msg()
        else:
            print("余额不足，请先充值")


def main():
    dog = Dog()
    dog.send_msg(100000)


if __name__ == "__main__":
    main()
