# mariadb安装文档


## RedHat/Rockylinux安装
1. 更新数据源 
   ```sh
   sudo dnf update
   ```

2. 安装mariadb
   ```sh
   sudo dnf install mariadb-server
   ```

3. 设置mariadb为开机自启
   ```sh
   # 查看mariadb运行情况
   sudo systemctl status mariadb
   # 设置开机自启
   sudo systemctl enable mariadb
   ```

4. mariadb初始化设置
   ```sh
   sudo mysql_secure_installation
   ```
   - 可以设置root密码、是否开启root远程登陆等内容

5. 创建管理员权限的用户
   ```sh
   # 用root登录
   mysql -uroot -p
   # 创建用户及密码 '%'表示任何地方都可以登录
   create user 'username'@'%' identified by 'password';
   # 给创建的用户权限
   grant all privileges on *.* to 'username'@'%' with grant option;
   # 刷新权限
   flush privieges;
   # 退出
   exit;
   ```

6. 修改配置，允许远程连接
   ```sh
   # 编辑配置文件 文件位置 /etc/my.cnf
   sudo vim /etc/my.cnf
   # 添加监听地址
   [mysqld]
   bind-address = 0.0.0.0
   # 保存退出
   ```

7. 重启服务
   ```sh
   sudo systemctl restart mariadb
   ```

8. 远程登陆测试
   ```sh
   mysql -h addr -P 3306 -u username -p
   ```