# pacman命令详解

## 1. 更新系统
在 Archlinux 中,使用一条命令即可对整个系统进行更新
```sh 
pacman -Syu
```
如果你已经使用 pacman -Sy 将本地的包数据库与远程的仓库进行了同步,也可以只执行
```sh
pacman -Su
```

## 2. 安装包
- `pacman -S <package>`   安装包，可以同时安装多个包, 只需以空格分隔包名即可
- `pacman -Sy <package>`  在同步包数据库后再执行安装
- `pacman -Sv <package>`  在显示一些操作信息后执行安装
- `pacman -U <package> `  安装本地包,其扩展名为 pkg.tar.gz

## 3. 删除包
- `pacman -R <package>` 只删除包,不包含该包的依赖
- `pacman -Rs <package>` 在删除包的同时,也将删除其依赖
- `pacman -Rd <package>` 在删除包时不检查依赖

## 4. 搜索包
- `pacman -Ss 关键字` 搜索含关键字的包
- `pacman -Qi <package>` 查看有关包的信息
- `pacman -Ql <package>` 列出该包的文件

## 5. 其他用法
- `pacman -Sw <package>` 只下载包,不安装
- `pacman -Sc:Pacman` 下载的包文件位于 /var/cache/pacman/pkg/ 目录。该命令将清理未安装的包文件
- `pacman -Scc` 清理所有的缓存文件

## 6.简单实例
- 安装或者升级单个软件包，或者一列软件包（包含依赖包），使用如下命令：
```sh 
pacman -S package_name1 package_name2
```
- 有时候在不同的软件仓库中，一个软件包有多个版本（比如extra和testing），可以选择一个来安装：
```sh
pacman -S extra/package_name
pacman -S testing/package_name
```
- 删除单个软件包，保留其全部已经安装的依赖关系:
```sh
pacman -R package_name
```
- 删除指定软件包，及其所有没有被其他已安装软件包使用的依赖关系：
```sh
pacman -Rs package_name
```
**缺省的，pacman会备份被删除程序的配置文件，将它们加上\*.pacsave扩展名**
- 删除软件包时要同时删除相应的配置文件（这种行为在基于Debian的系统中称为清除purging），使用命令：
```sh
pacman -Rn package_name
```
- 删除一个软件包、它的配置文件以及所有不再需要的依赖的命令如下：
```sh
pacman -Rsn package_name
```
- 用一个指令来升级系统中所有已安装的包。升级的时间取决于系统有多新:
```sh
pacman -Su
```
- 将升级系统和同步仓库数据合成为一条指令：
```sh
pacman -Syu
```
- 在包数据库中查询软件包，查询位置包含了包的名字和描述：
```sh
pacman -Ss package
```
- 查询已安装的软件包：
```sh
pacman -Qs package
```
- 如果得到了软件包的完整名字，可以获取关于它的更为详尽的信息：
```sh
pacman -Si package
pacman -Qi package
```
- 获取已安装软件包所包含文件的列表：
```sh
pacman -Ql package
```
- 通过查询数据库获知目前的文件系统中某个文件是属于哪个软件包:
```sh
pacman -Qo /path/to/a/file
```
- 罗列所有不再作为依赖的软件包(孤立orphans)：
```sh
pacman -Qdt
```
- Pacman使用-Q参数来查询本地软件包数据库：
```sh
pacman -Q –help
```
- Pacman使用-S参数来查询远程同步的数据库：
```sh
pacman -S –help
```

## 7.其它用法
**Pacman是个非常广泛的包管理工具，这里只是它的一些其它主要特性**
- 下载包而不安装它：
```sh
pacman -Sw package_name
```
- 安装一个本地包：
```sh
pacman -U /path/to/package/package_name-version.pkg.tar.gz
```
- 安装一个远程包：
```sh
pacman -U http://url/package_name-version.pkg.tar.gz
```
- 清理当前未被安装软件包的缓存(/var/cache/pacman/pkg):
```sh
pacman -Sc
```
- 完全清理包缓存：
```sh
pacman -Scc
```
**关于`pacman -Scc`，仅在确定不需要做任何软件包降级工作时才这样做。`pacman -Scc`会从缓存中删除所有软件包**
- 要删除孤立软件包（递归的，要小心)：
```sh
pacman -Rs $(pacman -Qtdq)
```
- 重新安装你系统中所有的软件包（仓库中已有的）：
```sh
pacman -S $(pacman -Qq | grep -v “$(pacman -Qmq)”)
```
- 获取本地软件包和它们大小的一个已排序清单列表：
```sh
LANG=C pacman -Qi | sed -n ‘/^Name[^:]*: (.*)/{s//1 /;x};/^Installed[^:]*: (.*)/{s//1/;H;x;s/n//;p}’ | sort -nk2
```

## 8.配置
1. 要了解更详细的参数开关可以pacman –help或者man pacman。
2. Pacman的配置文件位于/etc/pacman.conf。关于配置文件的进一步信息可以用man pacman.conf查看。
3. 常用选项都在[options]段。阅读man手册或者查看缺省的pacman.conf可以获得有关信息和用途。
4. 跳过升级软件包,如果由于某种原因，你不希望升级某个软件包，可以加入内容如下：
```sh
IgnorePkg = 软件包名
```
跳过升级软件包组
和软件包一样，也可以象这样跳过升级某个软件包组：
```sh
IgnoreGroup = gnome
```
