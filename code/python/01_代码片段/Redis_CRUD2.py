import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import redis
import json

class RedisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Redis 数据库管理器")
        self.root.geometry("800x600")
        
        self.redis_client = None
        self.setup_ui()
    
    def setup_ui(self):
        """设置用户界面"""
        # 连接框架
        conn_frame = ttk.LabelFrame(self.root, text="Redis 连接配置", padding=10)
        conn_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(conn_frame, text="主机:").grid(row=0, column=0, sticky="w")
        self.host_entry = ttk.Entry(conn_frame, width=15)
        self.host_entry.grid(row=0, column=1, padx=5)
        self.host_entry.insert(0, "localhost")
        
        ttk.Label(conn_frame, text="端口:").grid(row=0, column=2, sticky="w")
        self.port_entry = ttk.Entry(conn_frame, width=10)
        self.port_entry.grid(row=0, column=3, padx=5)
        self.port_entry.insert(0, "6379")
        
        ttk.Label(conn_frame, text="数据库:").grid(row=0, column=4, sticky="w")
        self.db_entry = ttk.Entry(conn_frame, width=5)
        self.db_entry.grid(row=0, column=5, padx=5)
        self.db_entry.insert(0, "0")
        
        ttk.Label(conn_frame, text="密码:").grid(row=1, column=0, sticky="w")
        self.password_entry = ttk.Entry(conn_frame, width=15, show="*")
        self.password_entry.grid(row=1, column=1, padx=5)
        
        self.connect_btn = ttk.Button(conn_frame, text="连接", command=self.connect_redis)
        self.connect_btn.grid(row=1, column=2, padx=5)
        
        self.disconnect_btn = ttk.Button(conn_frame, text="断开", command=self.disconnect_redis, state="disabled")
        self.disconnect_btn.grid(row=1, column=3, padx=5)
        
        # 操作框架
        op_frame = ttk.LabelFrame(self.root, text="数据操作", padding=10)
        op_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(op_frame, text="键名:").grid(row=0, column=0, sticky="w")
        self.key_entry = ttk.Entry(op_frame, width=30)
        self.key_entry.grid(row=0, column=1, padx=5)
        
        ttk.Label(op_frame, text="值:").grid(row=1, column=0, sticky="w")
        self.value_text = scrolledtext.ScrolledText(op_frame, height=4, width=40)
        self.value_text.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(op_frame, text="过期时间(秒):").grid(row=2, column=0, sticky="w")
        self.expire_entry = ttk.Entry(op_frame, width=10)
        self.expire_entry.grid(row=2, column=1, padx=5, sticky="w")
        
        btn_frame = ttk.Frame(op_frame)
        btn_frame.grid(row=3, column=1, pady=5)
        
        ttk.Button(btn_frame, text="创建", command=self.create_key).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="读取", command=self.read_key).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="更新", command=self.update_key).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="删除", command=self.delete_key).pack(side="left", padx=5)
        
        # 键列表框架
        list_frame = ttk.LabelFrame(self.root, text="键列表", padding=10)
        list_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.keys_tree = ttk.Treeview(list_frame, columns=("value", "type"), show="headings")
        self.keys_tree.heading("#0", text="键名")
        self.keys_tree.heading("value", text="值")
        self.keys_tree.heading("type", text="类型")
        
        vsb = ttk.Scrollbar(list_frame, orient="vertical", command=self.keys_tree.yview)
        hsb = ttk.Scrollbar(list_frame, orient="horizontal", command=self.keys_tree.xview)
        self.keys_tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        self.keys_tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")
        
        list_frame.grid_rowconfigure(0, weight=1)
        list_frame.grid_columnconfigure(0, weight=1)
        
        # 绑定双击事件
        self.keys_tree.bind("<Double-1>", self.on_key_double_click)
        
        # 状态栏
        self.status_var = tk.StringVar()
        self.status_var.set("就绪")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief="sunken")
        status_bar.pack(side="bottom", fill="x")
    
    def connect_redis(self):
        """连接Redis"""
        try:
            self.redis_client = redis.Redis(
                host=self.host_entry.get(),
                port=int(self.port_entry.get()),
                db=int(self.db_entry.get()),
                password=self.password_entry.get() or None,
                decode_responses=True,
                socket_timeout=5
            )
            
            # 测试连接
            self.redis_client.ping()
            
            self.connect_btn.config(state="disabled")
            self.disconnect_btn.config(state="normal")
            self.status_var.set(f"已连接到 {self.host_entry.get()}:{self.port_entry.get()}")
            
            # 刷新键列表
            self.refresh_keys()
            
            messagebox.showinfo("成功", "Redis连接成功！")
            
        except Exception as e:
            messagebox.showerror("连接失败", f"无法连接Redis: {e}")
    
    def disconnect_redis(self):
        """断开Redis连接"""
        if self.redis_client:
            self.redis_client.close()
            self.redis_client = None
        
        self.connect_btn.config(state="normal")
        self.disconnect_btn.config(state="disabled")
        self.status_var.set("连接已断开")
        
        # 清空键列表
        for item in self.keys_tree.get_children():
            self.keys_tree.delete(item)
    
    def create_key(self):
        """创建键"""
        if not self.check_connection():
            return
        
        key = self.key_entry.get().strip()
        value = self.value_text.get("1.0", tk.END).strip()
        expire = self.expire_entry.get().strip()
        
        if not key or not value:
            messagebox.showwarning("输入错误", "键和值不能为空！")
            return
        
        try:
            expire = int(expire) if expire else None
            
            if expire:
                self.redis_client.setex(key, expire, value)
            else:
                self.redis_client.set(key, value)
            
            self.status_var.set(f"创建成功: {key}")
            self.refresh_keys()
            messagebox.showinfo("成功", f"键 {key} 创建成功！")
            
        except Exception as e:
            messagebox.showerror("错误", f"创建失败: {e}")
    
    def read_key(self):
        """读取键"""
        if not self.check_connection():
            return
        
        key = self.key_entry.get().strip()
        if not key:
            messagebox.showwarning("输入错误", "请输入键名！")
            return
        
        try:
            value = self.redis_client.get(key)
            if value is None:
                messagebox.showinfo("结果", f"键 {key} 不存在")
            else:
                self.value_text.delete("1.0", tk.END)
                self.value_text.insert("1.0", value)
                self.status_var.set(f"读取成功: {key}")
                
        except Exception as e:
            messagebox.showerror("错误", f"读取失败: {e}")
    
    def update_key(self):
        """更新键（与创建相同）"""
        self.create_key()
    
    def delete_key(self):
        """删除键"""
        if not self.check_connection():
            return
        
        key = self.key_entry.get().strip()
        if not key:
            messagebox.showwarning("输入错误", "请输入键名！")
            return
        
        try:
            result = self.redis_client.delete(key)
            if result > 0:
                self.status_var.set(f"删除成功: {key}")
                self.refresh_keys()
                messagebox.showinfo("成功", f"键 {key} 删除成功！")
            else:
                messagebox.showinfo("结果", f"键 {key} 不存在")
                
        except Exception as e:
            messagebox.showerror("错误", f"删除失败: {e}")
    
    def refresh_keys(self):
        """刷新键列表"""
        if not self.redis_client:
            return
        
        try:
            # 清空现有列表
            for item in self.keys_tree.get_children():
                self.keys_tree.delete(item)
            
            # 获取所有键
            keys = self.redis_client.keys('*')
            for key in keys:
                value = self.redis_client.get(key)
                value_type = type(value).__name__
                
                # 截断长值
                display_value = str(value)[:50] + "..." if len(str(value)) > 50 else str(value)
                
                self.keys_tree.insert("", "end", text=key, values=(display_value, value_type))
            
            self.status_var.set(f"找到 {len(keys)} 个键")
            
        except Exception as e:
            messagebox.showerror("错误", f"刷新键列表失败: {e}")
    
    def on_key_double_click(self, event):
        """双击键列表事件"""
        selection = self.keys_tree.selection()
        if selection:
            item = self.keys_tree.item(selection[0])
            key = item["text"]
            self.key_entry.delete(0, tk.END)
            self.key_entry.insert(0, key)
            self.read_key()
    
    def check_connection(self):
        """检查连接状态"""
        if not self.redis_client:
            messagebox.showwarning("连接错误", "请先连接Redis服务器！")
            return False
        return True

def run_gui():
    """运行图形界面"""
    root = tk.Tk()
    app = RedisGUI(root)
    root.mainloop()

if __name__ == "__main__":
    # 运行图形界面
    run_gui()
    
    # 或者运行命令行界面
    # main()