def test(sum):
    if sum > 1:
        return sum * test(sum - 1)
    else:
        return sum


def main():
    """启动函数"""
    sum = int(input("请输入要阶乘的数字:"))
    jiecheng = test(sum)
    print(jiecheng)


if __name__ == "__main__":
    main()
