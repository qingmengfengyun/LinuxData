import mysql.connector
from mysql.connector import Error
import getpass


class MySQLCRUD:
    def __init__(self):
        self.connection = None
        self.current_db = None

    def connect(self, host, user, password, database=None):
        """连接数据库"""
        try:
            self.connection = mysql.connector.connect(
                host="192.168.31.86", user="QingmPei", password="Pei19921022", database=database
            )
            if self.connection.is_connected():
                self.current_db = database
                print(f"✓ 成功连接到数据库: {database or '默认数据库'}")
                return True
        except Error as e:
            print(f"✗ 连接失败: {e}")
            return False

    def disconnect(self):
        """断开连接"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("✓ 连接已关闭")

    def execute_query(self, query, params=None):
        """执行查询并返回结果"""
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params or ())
            result = cursor.fetchall()
            cursor.close()
            return result, cursor.rowcount
        except Error as e:
            print(f"✗ 查询错误: {e}")
            return [], 0

    def execute_update(self, query, params=None):
        """执行更新操作"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params or ())
            self.connection.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            return affected_rows
        except Error as e:
            self.connection.rollback()
            print(f"✗ 更新错误: {e}")
            return 0

    def show_databases(self):
        """显示所有数据库"""
        databases, _ = self.execute_query("SHOW DATABASES")
        print("\n📁 数据库列表:")
        for db in databases:
            print(f"  - {db['Database']}")

    def show_tables(self):
        """显示当前数据库的所有表"""
        if not self.current_db:
            print("请先选择数据库！")
            return

        tables, _ = self.execute_query("SHOW TABLES")
        print(f"\n📊 数据库 '{self.current_db}' 中的表:")
        for table in tables:
            table_name = list(table.values())[0]
            print(f"  - {table_name}")

    def describe_table(self, table_name):
        """显示表结构"""
        result, _ = self.execute_query(f"DESCRIBE {table_name}")
        print(f"\n📋 表 '{table_name}' 结构:")
        for row in result:
            print(
                f"  字段: {row['Field']:15} 类型: {row['Type']:20} 空: {row['Null']:5} 键: {row['Key']}"
            )

    def select_data(self, table_name, condition=None):
        """查询数据"""
        query = f"SELECT * FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"

        result, count = self.execute_query(query)
        print(f"\n🔍 查询结果 ({count} 行):")
        if result:
            # 打印表头
            headers = result[0].keys()
            print(" | ".join(headers))
            print("-" * (len(" | ".join(headers)) + 10))

            # 打印数据
            for row in result:
                print(" | ".join(str(value) for value in row.values()))
        else:
            print("没有找到数据")

    def insert_data(self, table_name, data):
        """插入数据"""
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["%s"] * len(data))
        values = tuple(data.values())

        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        affected = self.execute_update(query, values)
        print(f"✓ 插入成功，影响 {affected} 行")

    def update_data(self, table_name, set_data, condition):
        """更新数据"""
        set_clause = ", ".join([f"{key} = %s" for key in set_data.keys()])
        values = tuple(set_data.values())

        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        affected = self.execute_update(query, values)
        print(f"✓ 更新成功，影响 {affected} 行")

    def delete_data(self, table_name, condition):
        """删除数据"""
        query = f"DELETE FROM {table_name} WHERE {condition}"
        affected = self.execute_update(query)
        print(f"✓ 删除成功，影响 {affected} 行")

    def create_table(self, table_name, columns):
        """创建表"""
        columns_def = ", ".join(columns)
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_def})"
        self.execute_update(query)
        print(f"✓ 表 '{table_name}' 创建成功")


def main():
    """主函数"""
    crud = MySQLCRUD()

    print("🐍 Python MySQL CRUD 程序")
    print("=" * 50)

    # 获取连接信息
    host = input("数据库主机 (默认 localhost): ") or "localhost"
    user = input("用户名 (默认 root): ") or "root"
    password = getpass.getpass("密码: ")

    # 连接数据库
    if crud.connect(host, user, password):
        crud.show_databases()

        # 选择数据库
        db_name = input("\n请输入要使用的数据库名: ")
        if db_name:
            crud.disconnect()
            crud.connect(host, user, password, db_name)

        while True:
            print("\n" + "=" * 50)
            print("1. 显示所有表")
            print("2. 查看表结构")
            print("3. 查询数据")
            print("4. 插入数据")
            print("5. 更新数据")
            print("6. 删除数据")
            print("7. 创建表")
            print("8. 执行自定义SQL")
            print("9. 退出")

            choice = input("\n请选择操作 (1-9): ")

            if choice == "1":
                crud.show_tables()

            elif choice == "2":
                table_name = input("请输入表名: ")
                crud.describe_table(table_name)

            elif choice == "3":
                table_name = input("请输入表名: ")
                condition = input("查询条件 (可选): ")
                crud.select_data(table_name, condition)

            elif choice == "4":
                table_name = input("请输入表名: ")
                print("请输入要插入的数据 (格式: 字段1=值1, 字段2=值2): ")
                data_input = input().split(",")
                data = {}
                for item in data_input:
                    if "=" in item:
                        key, value = item.split("=", 1)
                        data[key.strip()] = value.strip()
                crud.insert_data(table_name, data)

            elif choice == "5":
                table_name = input("请输入表名: ")
                print("请输入要更新的数据 (格式: 字段1=新值1, 字段2=新值2): ")
                set_input = input().split(",")
                set_data = {}
                for item in set_input:
                    if "=" in item:
                        key, value = item.split("=", 1)
                        set_data[key.strip()] = value.strip()
                condition = input("更新条件: ")
                crud.update_data(table_name, set_data, condition)

            elif choice == "6":
                table_name = input("请输入表名: ")
                condition = input("删除条件: ")
                crud.delete_data(table_name, condition)

            elif choice == "7":
                table_name = input("请输入新表名: ")
                print(
                    "请输入字段定义 (格式: id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100)): "
                )
                columns = input().split(",")
                crud.create_table(table_name, columns)

            elif choice == "8":
                sql = input("请输入SQL语句: ")
                if sql.strip().lower().startswith("select"):
                    result, count = crud.execute_query(sql)
                    print(f"查询结果 ({count} 行):")
                    for row in result:
                        print(row)
                else:
                    affected = crud.execute_update(sql)
                    print(f"操作成功，影响 {affected} 行")

            elif choice == "9":
                print("再见！")
                break

            else:
                print("无效选择，请重新输入！")

        crud.disconnect()


if __name__ == "__main__":
    main()
