# Docker&Docker-Compose安装文档

## RHEL/RockyLinux安装Docker

1. 更新软件包索引并安装依赖项：
    ```bash
    sudo dnf update
    ```

2. 添加 Docker 仓库：
    ```bash
    # 安装dnf插件核心
    sudo dnf -y install dnf-plugins-core

    # 添加docker官方源
    sudo dnf config-manager --add-repo https://download.docker.com/linux/rhel/docker-ce.repo

    # 更换为清华源
    sed -i 's+https://download.docker.com+https://mirrors.tuna.tsinghua.edu.cn/docker-ce+' /etc/yum.repos.d/docker-ce.repo
    ```

3. 安装 Docker CE：
    ```bash
    sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ```

4. 启动并启用 Docker 服务：
    ```bash
    sudo systemctl start docker
    sudo systemctl enable docker
    ```

5. 验证 Docker 安装：
    ```bash
    sudo docker run hello-world
    ```

6. 添加docker用户组
   ```bash
   # 创建docker用户组
   sudo groupadd docker

   # 将用户添加到docker组
   sudo usermod -aG docker yourusername

   # 重新登录或重新启动docker服务
   sudo systemctl restart docker
   ```

## 安装 Docker Compose

1. 下载 Docker Compose 二进制文件：
    ```bash
    sudo curl -L "https://github.com/docker/compose/releases/download/v2.32.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    ```

2. 为二进制文件添加执行权限：
    ```bash
    sudo chmod +x /usr/local/bin/docker-compose
    ```

3. 验证 Docker Compose 安装：
    ```bash
    docker-compose --version
    ```
