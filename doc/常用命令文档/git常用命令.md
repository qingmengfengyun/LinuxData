# git 常用命令
- git 三个区 工作区 暂存区 本地库
## 修改本地git用户信息
`git config --global user.name "username"` 
## 修改本地Git的邮箱信息
`git config --global user.email "xxxx@xxx.com"`
## 查看本地config信息
`git config --global --list`
## 从服务器地址上将项目代码拷贝到当前目录,可以加空格指定路径和文件夹名称
`git clone <url>` 
## 初始化仓库,可以在后面加空格指定仓库的路径
`git init`
## 添加文件到暂存区
`git add <file>`
## 添加当前目录中的所有文件
`git add .`
## 提交更改
`git commit -m "<message>"`
## 添加对跟踪文件所做的所有更改并提交
`git commit -am "<message>"`
## 从暂存区删除一个文件
`git reset <file>`
## 移动或重命名文件
`git mv <current path> <new path>`
## 从存储库中删除文件
`git rm <file>`
## 从暂存区中删除
`git rm --cached <file>`
## 显示分支
`git branch`
- `-a` 显示所有分支（本地和远程）
- `-r` 显示远程分支
- `-v` 显示最后一次提交的分支
## 创建一个分支
`git branch <branch>`
## 创建一个分支并使用 checkout 命令切换到它
`git checkout -b <branch>`
## 切换到一个分支
`git switch <branch>`
## 删除一个分支
`git branch -d <branch>`
- 加`-D`强行删除分支
## 合并分支
`git merge <branch to merge into HEAD>`
- `--no-ff` 即使合并解析为快进，也创建合并提交
- `--squash` 将指定分支中的所有提交压缩为单个提交 
## 变基分支
`git rebase <branch to rebase from>`
- **变基是将一系列提交移动或组合到新的基本提交的过程**
## 查看之前的提交
`git checkout <commit id>`
## 恢复提交
`git revert <commit id>`
## 重置提交
`git reset <commit id>`
- 可以添加三个参数，默认是`--mixed`
- `--mixed` 重置HEAD和暂存区，默认参数，保留工作区
- `--soft` 重置 HEAD，保留暂存区和工作区，让仓库恢复到执行git commit之前的状态
- `--hard` 重置HEAD、暂存区和工作区
## 查看存储库的状态
`git status`
- `-s` "--short" 以短格式输出输出
- `-b` "--branch" 以短格式显示分支和跟踪信息
- `--show-stash` 显示当前隐藏的条目数量
- `--long` 以长格式输出输出,这是默认设置
- `-v` "--verbose" 除了已更改的文件名称之外，还会显示将要提交的文本更改
## 显示提交历史
`git log`
- `-p` 按补丁格式显示每个更新的差异，比下一条--stat命令信息更全。
- `--stat` 显示每次提交修改文件的统计信息，每个提交都列出了修改过的文件，以及其中添加和移除的行数，并在最后列出所有增减行数小计。
- `--shortstat` 只显示`--stat`中最后的行数添加、修改、删除的统计。
- `--name-only` 仅在提交信息后，显示已修改的文件清单。
- `--name-status` 显示新增、修改、删除的文件清单。
- `--abbrev-commit` 仅显示SHA-1校验和的前几个字符，而非所有的40个字符。
- `--relative-date` 使用较短的相对时间，而不是完整格式显示日期（比如“2 weeks ago”）。
- `--graph` 在日志旁以 ASCII 图形显示分支与合并历史。
- `--online` 列表的形式查看历史版本记录
## 显示对未暂存文件的更改
`git diff\`
- `git diff --staged` 标志来显示对暂存文件的更改
- `git diff <commit id 01> <commit id 02>` 显示两次提交之间的变化
## 存储更改，允许在不提交更改的情况下临时存储更
`git stash`
- `git stash save "<message>"` 将消息添加到存储中  
- `git stash list` 列出存储
- `git stash apply <stash id>` 申请一个藏匿处，应用存储不会将其从存储列表中删除，如果不指定，将应用最新的 stash
- `git stash apply stash@{0}` 使用格式 stash@{} 应用存储
- `git stash drop <stash id>` 删除一个藏匿处
- `git stash clear` 删除所有藏匿处
- `git stash pop <stash id>` 应用和删除存储
- `git stash show <stash id>`  显示存储中的更改
## 添加远程仓库
`git remote add <remote name> <url>`
## 显示远程仓库
`git remote`
- `git remote -v` 标志以显示远程存储库的URL
## 删除远程仓库
`git remote remove <remote name>`
## 重命名远程存储库
`git remote rename <old name> <new name>`
## 从远程存储库中获取更改
`git fetch <remote name>`
## 从特定分支获取更改
`git fetch <remote name> <branch>`
## 从远程存储库中拉取更改
`git pull <remote name> <branch>`
## 将更改推送到远程存储库
`git push <remote name>`
## 将更改推送到特定分支
`git push <remote name> <branch>`

## git删除子模块
### 编辑.gitmodules文件，删除子模块相关配置
`git config -f .gitmodules --remove-section submodule.[submodule_path]`
### 编辑.git/config文件，删除子模块相关配置
`git config --remove-section submodule.[submodule_path]`
### 删除子模块文件夹
`rm -rf [submodule_path]`
### 从Git中删除子模块的跟踪记录
`git rm --cached [submodule_path]`
### 提交更改
`git commit -m "Removed submodule [submodule_path]"`

