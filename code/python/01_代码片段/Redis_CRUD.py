import redis
import json
from typing import Any, Dict, List, Optional
import argparse

class RedisCRUD:
    def __init__(self, host='localhost', port=6379, db=0, password=None):
        """初始化Redis连接"""
        try:
            self.redis_client = redis.Redis(
                host=host,
                port=port,
                db=db,
                password=password,
                decode_responses=True,  # 自动解码为字符串
                socket_timeout=5,
                socket_connect_timeout=5
            )
            # 测试连接
            self.redis_client.ping()
            print(f"✅ 成功连接到 Redis 服务器: {host}:{port}")
        except redis.ConnectionError as e:
            print(f"❌ 连接失败: {e}")
            raise
    
    def create_key(self, key: str, value: Any, expire: int = None) -> bool:
        """创建键值对"""
        try:
            if isinstance(value, (dict, list)):
                value = json.dumps(value)
            
            if expire:
                self.redis_client.setex(key, expire, value)
            else:
                self.redis_client.set(key, value)
            
            print(f"✅ 创建成功: {key} = {value}")
            return True
        except Exception as e:
            print(f"❌ 创建失败: {e}")
            return False
    
    def read_key(self, key: str) -> Any:
        """读取键值"""
        try:
            value = self.redis_client.get(key)
            if value is None:
                print(f"⚠️  键不存在: {key}")
                return None
            
            # 尝试解析JSON
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return value
        except Exception as e:
            print(f"❌ 读取失败: {e}")
            return None
    
    def update_key(self, key: str, value: Any, expire: int = None) -> bool:
        """更新键值（与create相同，但会检查存在性）"""
        if not self.redis_client.exists(key):
            print(f"⚠️  键不存在，将创建新键: {key}")
        
        return self.create_key(key, value, expire)
    
    def delete_key(self, key: str) -> bool:
        """删除键"""
        try:
            result = self.redis_client.delete(key)
            if result > 0:
                print(f"✅ 删除成功: {key}")
                return True
            else:
                print(f"⚠️  键不存在: {key}")
                return False
        except Exception as e:
            print(f"❌ 删除失败: {e}")
            return False
    
    def list_keys(self, pattern: str = '*') -> List[str]:
        """列出所有匹配的键"""
        try:
            keys = self.redis_client.keys(pattern)
            return sorted(keys)
        except Exception as e:
            print(f"❌ 列出键失败: {e}")
            return []
    
    def get_info(self) -> Dict[str, Any]:
        """获取Redis服务器信息"""
        try:
            info = self.redis_client.info()
            return info
        except Exception as e:
            print(f"❌ 获取信息失败: {e}")
            return {}
    
    def hash_operations(self):
        """哈希表操作示例"""
        hash_key = 'user:1001'
        
        # 设置哈希字段
        self.redis_client.hset(hash_key, 'name', '张三')
        self.redis_client.hset(hash_key, 'age', 25)
        self.redis_client.hset(hash_key, 'email', 'zhangsan@email.com')
        
        # 获取所有字段
        user_data = self.redis_client.hgetall(hash_key)
        print(f"用户数据: {user_data}")
        
        # 获取单个字段
        age = self.redis_client.hget(hash_key, 'age')
        print(f"年龄: {age}")
    
    def list_operations(self):
        """列表操作示例"""
        list_key = 'tasks'
        
        # 添加元素
        self.redis_client.lpush(list_key, 'task1', 'task2', 'task3')
        
        # 获取所有元素
        tasks = self.redis_client.lrange(list_key, 0, -1)
        print(f"任务列表: {tasks}")
    
    def close(self):
        """关闭连接"""
        if hasattr(self, 'redis_client'):
            self.redis_client.close()
            print("连接已关闭")

def main():
    """命令行主函数"""
    parser = argparse.ArgumentParser(description='Redis CRUD 工具')
    parser.add_argument('--host', default='localhost', help='Redis 主机')
    parser.add_argument('--port', type=int, default=6379, help='Redis 端口')
    parser.add_argument('--db', type=int, default=0, help='数据库编号')
    parser.add_argument('--password', help='Redis 密码')
    
    args = parser.parse_args()
    
    try:
        # 创建Redis连接
        redis_crud = RedisCRUD(
            host=args.host,
            port=args.port,
            db=args.db,
            password=args.password
        )
        
        # 交互式操作
        while True:
            print("\n" + "="*50)
            print("Redis CRUD 操作菜单")
            print("1. 创建键值对")
            print("2. 读取键值")
            print("3. 更新键值")
            print("4. 删除键")
            print("5. 列出所有键")
            print("6. 服务器信息")
            print("7. 哈希表示例")
            print("8. 列表示例")
            print("9. 退出")
            
            choice = input("请选择操作 (1-9): ").strip()
            
            if choice == '1':
                key = input("请输入键名: ").strip()
                value = input("请输入值: ").strip()
                expire = input("过期时间(秒，可选): ").strip()
                expire = int(expire) if expire else None
                redis_crud.create_key(key, value, expire)
            
            elif choice == '2':
                key = input("请输入键名: ").strip()
                value = redis_crud.read_key(key)
                if value is not None:
                    print(f"值: {value} (类型: {type(value).__name__})")
            
            elif choice == '3':
                key = input("请输入键名: ").strip()
                value = input("请输入新值: ").strip()
                expire = input("过期时间(秒，可选): ").strip()
                expire = int(expire) if expire else None
                redis_crud.update_key(key, value, expire)
            
            elif choice == '4':
                key = input("请输入要删除的键名: ").strip()
                redis_crud.delete_key(key)
            
            elif choice == '5':
                pattern = input("键名模式(默认*): ").strip() or '*'
                keys = redis_crud.list_keys(pattern)
                print(f"找到 {len(keys)} 个键:")
                for i, key in enumerate(keys, 1):
                    print(f"{i}. {key}")
            
            elif choice == '6':
                info = redis_crud.get_info()
                print("服务器信息:")
                print(f"版本: {info.get('redis_version')}")
                print(f"内存使用: {info.get('used_memory_human')}")
                print(f"连接数: {info.get('connected_clients')}")
                print(f"数据库大小: {info.get('keyspace', {}).get(f'db{args.db}', {}).get('keys', 0)}")
            
            elif choice == '7':
                redis_crud.hash_operations()
            
            elif choice == '8':
                redis_crud.list_operations()
            
            elif choice == '9':
                print("再见！")
                break
            
            else:
                print("无效选择，请重新输入！")
    
    except Exception as e:
        print(f"程序错误: {e}")
    finally:
        if 'redis_crud' in locals():
            redis_crud.close()

if __name__ == "__main__":
    main()


'''
指定连接参数
python redis_crud.py --host 127.0.0.1 --port 6379 --db 0

# 带密码连接
python redis_crud.py --host redis-server.com --password your_password
'''
