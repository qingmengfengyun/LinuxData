# Dockerfile
FROM ubuntu

# 设置环境变量
ENV DEBIAN_FRONTEND=noninteractive

# 更新并安装基础工具
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    sudo \
    git \
    zsh \
    stow \
    htop \
    neofetch \
    neovim \
    net-tools \
    iputils-ping \
    openssh-server \
    && rm -rf /var/lib/apt/lists/* \
    && adduser qingm


# 设置工作目录
WORKDIR /home/qingm

# 复制文件
COPY . .

# 设置默认命令
CMD ["zsh"]

