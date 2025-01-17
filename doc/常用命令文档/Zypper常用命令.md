# Zypper用法

## 用法
```sh
zypper [--全 局 选 项 ] <命 令 > [--命 令 选 项 ] [参 数 ]
```
## 全局选项
```sh
       --help, -h              帮 助 。 .
       --version, -V           输 出 版 本 号 。
       --quiet, -q             减 少 普 通 输 出 ， 仅 打 印 错 误 信 息 。
       --verbose, -v           增 加 信 息 的 详 细 程 度
       --no-abbrev, -A         表 格 中 不 出 现 缩 写 文 本 。
       --table-style, -s       表 格 样 式 (整 数 )。
       --rug-compatible, -r    开 启 与 rug 的 兼 容 。
       --non-interactive, -n   不 询 问 任 何 问 题 ， 自 动 使 用 默 认 的 回 复 。
       --xmlout, -x            切 换 到 XML 输 出 。
       --reposd-dir, -D <dir> 使 用 其 他 的 安 装 源 定 义 文 件 目 录 。
       --cache-dir, -C <dir>   使 用 其 他 的 元 数 据 缓 存 数 据 库 目 录 。
       --raw-cache-dir <dir>   使 用 其 他 的 原 始 元 数 据 缓 存 目 录 。
```

```sh
       Repository Options:
       --no-gpg-checks         忽 略 GPG 检 查 失 败 并 继 续 。
       --plus-repo, -p <URI>   使 用 额 外 的 安 装 源 。
       --disable-repositories 不 从 安 装 源 读 取 元 数 据 。
       --no-refresh            不 刷 新 安 装 源 。
```

## 目标选项
```sh
       --root, -R <dir>        在 不 同 的 根 目 录 下 操 作 。
       --disable-system-sources、 -D            不 读 取 系 统 安 装 的 可 解 析 项 。
```

## 命令
```sh
       help, ?                 打 印 帮 助 。
       shell, sh               一 次 接 受 多 个 命 令 .
```

```sh
       安 装 源 操 作 ：
       repos, lr               列 出 所 有 定 义 的 安 装 源 。
       addrepo, ar             添 加 一 个 新 的 安 装 源 。具体请看：http://hi.baidu.com/tunaisen/blog/item/4b2af73937ac7ff53b87cec8.html
       removerepo, rr          删 除 指 定 的 安 装 源 。
       renamerepo, nr          重 命 名 指 定 的 安 装 源 。
       modifyrepo, mr          修 改 指 定 的 安 装 源 。
       refresh, ref            刷 新 所 有 安 装 源 。
       clean                   清 除 本 地 缓 存 。
```

```sh
       软 件 管 理 ：
       install, in             安 装 软 件 包 。
       remove, rm              删 除 软 件 包 。
       verify, ve              检 验 软 件 包 的 依 赖 关 系 的 完 整 性 。
       update, up              将 已 经 安 装 的 软 件 包 更 新 到 新 的 版 本 。
       dist-upgrade, dup       执 行 整 个 系 统 的 升 级 。
       source-install, si      安 装 源 代 码 软 件 包 和 它 们 的 编 译 依 赖 。
```

```sh
       查 询 ：
       search, se              查 找 符 合 一 个 模 式 的 软 件 包 。
       info, if                显 示 指 定 软 件 包 的 完 整 信 息 。
       patch-info              显 示 指 定 补 丁 的 完 整 信 息 。
       pattern-info            显 示 指 定 模 式 的 完 整 信 息 。
       product-info            显 示 指 定 产 品 的 完 整 信 息 。
       patch-check, pchk       检 查 补 丁 。
       list-updates, lu        列 出 可 用 的 更 新 。
       patches, pch            列 出 所 有 可 用 的 补 丁 。
       packages, pa            列 出 所 有 可 用 的 软 件 包 。
       patterns, pt            列 出 所 有 可 用 的 模 式 。
       products, pd            列 出 所 有 可 用 的 产 品 。
       what-provides, wp       列 出 能 够 提 供 指 定 功 能 的 软 件 包 。
```

```sh
       软 件 包 锁 定 ：
       addlock, al             添 加 一 个 软 件 包 锁 定 。
       removelock, rl          取 消 一 个 软 件 包 锁 定 。
       locks, ll               列 出 当 前 的 软 件 包 锁 定 。
```
