#1.获取要复制的文件名
old_file_name = input("请输入要复制的文件名:")

#2.读取要复制的文件
old_file = open(old_file_name, 'r')
content = old_file.read()

#3.创建新的文件名
position = old_file_name.rfind(".")
new_file_name = old_file_name[:position] + "[复件]" + old_file_name[position:]

#4.写入内容到新的文件
new_file = open(new_file_name, 'w')
new_file.write(content)

#5.关闭两个文件
old_file.close()
new_file.close()

def main():
    pass


if __name__ == "__main__":
    main()
