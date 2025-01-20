# Zypper用法

## 用法
```sh
zypper [--全局选项] <命令> [--命令选项] [参数]
```
## 全局选项
   ```bash
       --help, -h              # 帮助
       --version, -V           # 输出版本号
       --quiet, -q             # 减少普通输出，仅打印错误信息
       --verbose, -v           # 增加信息的详细程度
       --no-abbrev, -A         # 表格中不出现缩写文本
       --table-style, -s       # 表格样式(整数)
       --rug-compatible, -r    # 开启与rug的兼容
       --non-interactive, -n   # 不询问任何问题，自动使用默认的回复
       --xmlout, -x            # 切换到XML输出
       --reposd-dir, -D <dir>  # 使用其他的安装源定义文件目录
       --cache-dir, -C <dir>   # 使用其他的元数据缓存数据库目录
       --raw-cache-dir <dir>   # 使用其他的原始元数据缓存目录
   ```

   ```sh
       # Repository Options:
       --no-gpg-checks         # 忽略GPG检查失败并继续
       --plus-repo, -p <URI>   # 使用额外的安装源
       --disable-repositories  # 不从安装源读取元数据
       --no-refresh            # 不刷新安装源
   ```

## 目标选项
   ```sh
       --root, -R <dir>        # 在不同的根目录下操作
       --disable-system-sources, -D            # 不读取系统安装的可解析项
   ```

## 命令
   ```sh
       help, ?                 # 打印帮助
       shell, sh               # 一次接受多个命令
   ```

   ```sh
       # 安装源操作：
       repos, lr               # 列出所有定义的安装源
       addrepo, ar             # 添加一个新的安装源。具体请看：http://hi.baidu.com/tunaisen/blog/item/4b2af73937ac7ff53b87cec8.html
       removerepo, rr          # 删除指定的安装源
       renamerepo, nr          # 重命名指定的安装源
       modifyrepo, mr          # 修改指定的安装源
       refresh, ref            # 刷新所有安装源
       clean                   # 清除本地缓存
   ```

   ```sh
       # 软件管理：
       install, in             # 安装软件包
       remove, rm              # 删除软件包
       verify, ve              # 检验软件包的依赖关系的完整性
       update, up              # 将已经安装的软件包更新到新的版本
       dist-upgrade, dup       # 执行整个系统的升级
       source-install, si      # 安装源代码软件包和它们的编译依赖
   ```

   ```sh
       # 查询 ：
       search, se              # 查找符合一个模式的软件包
       info, if                # 显示指定软件包的完整信息
       patch-info              # 显示指定补丁的完整信息
       pattern-info            # 显示指定模式的完整信息
       product-info            # 显示指定产品的完整信息
       patch-check, pchk       # 检查补丁
       list-updates, lu        # 列出可用的更新
       patches, pch            # 列出所有可用的补丁
       packages, pa            # 列出所有可用的软件包
       patterns, pt            # 列出所有可用的模式
       products, pd            # 列出所有可用的产品
       what-provides, wp       # 列出能够提供指定功能的软件包
   ```

   ```sh
       # 软件包锁定：
       addlock, al             # 添加一个软件包锁定
       removelock, rl          # 取消一个软件包锁定
       locks, ll               # 列出当前的软件包锁定
   ```
