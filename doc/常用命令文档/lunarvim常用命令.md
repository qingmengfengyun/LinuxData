# lunarvim配置流程

## 安装工具
```sh
yay -S fd # find
yay -S ripgrep # grep
yay -S neovim 
```
* 也可以使用包管理器安装，或者homebrew *

### 快捷方式
- jk          退出编辑模式到命令模式
- zc          折叠
- leader + \  左右分割
- leader + -  上下分割
- ctrl + s    直接保存文件
- shift + h   切换buffer
- shift + l   切换buffer
- leader + h  取消高亮
- leader + h  反转高亮
- leader + W  长代码换行
- leader + S  拼写检查，可以用"z + ="纠正
- leader + n  是否开启相对行号
- leader + o  s,v,h 显示代码结构

- leader + q  退出vim
- leader + c  退出当前buffer
- j           复制下一行到本行,并空一格
- leader + z  全屏当前buffer
- leader + md 在浏览器预览md文件
- leader + c  切换主题
- leader + lf 修正代码格式
- leader + r  执行并显示bash命令
- leader + gg 打开gitui
- sf          打开替换插件-spectre
- leader + r  直接执行脚本
- leader + f  telescope相关功能