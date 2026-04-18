# 使用最新的 Fedora 镜像
FROM fedora:latest

# 设置环境变量
ENV TZ=Asia/Shanghai
ENV LANG=zh_CN.UTF-8
ENV LC_ALL=zh_CN.UTF-8

# 设置构建参数
ENV USERNAME=zavier
ENV USER_UID=1000
ENV USER_GID=1000

# 更新系统并安装基本工具
RUN dnf update -y && \
    dnf install -y \
    glibc-langpack-zh \
    sudo \
    zsh \
    fish \
    python3 \
    python3-pip \
    git \
    neovim \
    ping \
    curl \
    stow \
    wget \
    tree \
    htop \
    procps-ng \
    net-tools \
    which \
    findutils \
    cracklib-dicts \
    && dnf clean all

# 配置时区（Fedora 标准方式）
RUN ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime

# 创建普通用户并赋予 sudo 免密权限（开发环境推荐）
RUN groupadd --gid ${USER_GID} ${USERNAME} && \
    useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} && \
    echo "${USERNAME} ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers


# 创建并设置工作目录权限
ENV HOME=/home/$USERNAME
WORKDIR /home/$USERNAME
USER $USERNAME

# 设置默认启动命令
CMD ["/bin/bash"]
