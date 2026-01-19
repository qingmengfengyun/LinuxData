FROM ubuntu:latest

# 设置环境变量
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Shanghai
ENV LANG=zh_CN.UTF-8
ENV LC_ALL=zh_CN.UTF-8
ENV LANGUAGE=zh_CN:zh

# 设置构建参数
ENV USERNAME=qingm
ENV PASSWORD=Pei19921022
ENV USER_UID=1000
ENV USER_GID=1000

# 更新系统并安装必要软件
RUN apt-get update && \
    apt-get install -y \
    curl \
    wget \
    sudo \
    git \
    zsh \
    fish \
    stow \
    locales \
    htop \
    python3-dev \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libffi-dev \
    pkg-config \
    neofetch \
    neovim \
    net-tools \
    iputils-ping \
    openssh-server \
    && rm -rf /var/lib/apt/lists/*

# 设置ubuntu用户构建参数
ARG UBUNTU_UID=1002
ARG UBUNTU_GID=1002

# 修改现有 ubuntu 用户的 UID 和 GID
RUN if id "ubuntu" >/dev/null 2>&1; then \
        usermod -u $UBUNTU_UID ubuntu && \
        groupmod -g $UBUNTU_GID ubuntu && \
        chown -R $UBUNTU_UID:$UBUNTU_GID /home/ubuntu; \
    else \
        groupadd -g $UBUNTU_GID ubuntu && \
        useradd -m -u $UBUNTU_UID -g $UBUNTU_GID -s /bin/bash ubuntu; \
    fi

# 创建用户组和用户
RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    echo "$USERNAME:$PASSWORD" | chpasswd

# 配置 sudo 权限
RUN echo "$USERNAME ALL=(ALL) ALL" > /etc/sudoers.d/$USERNAME && \
    chmod 0440 /etc/sudoers.d/$USERNAME

# 配置时区
RUN ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime && \
    echo ${TZ} > /etc/timezone

# 生成语言环境
RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
    sed -i '/zh_CN.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen && \
    update-locale LANG=zh_CN.UTF-8 LC_ALL=zh_CN.UTF-8

# 设置用户和工作目录
ENV HOME=/home/$USERNAME
WORKDIR /home/$USERNAME
USER $USERNAME

# 复制文件
COPY . .

# 默认命令
CMD ["zsh"]
