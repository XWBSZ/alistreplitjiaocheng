
## 绕过 Replit 检测部署 AList 网盘教程

**注意：** 本教程参考自大佬Alcex的文章 [链接](https://www.alcex.top/posts/205/)。

### 1. 下载 AList 安装文件

在 [AList Releases 页面](https://github.com/alist-org/alist/releases/) 下载 `alist-linux-amd64.tar.gz` 安装文件。将其重命名为 `xxx.tar.gz`，例如，你可以将其命名为 `XWG.tar.gz`。解压文件得到 `XWG.tar`。

### 2. 在 Replit 上部署

1. 登录或注册 [Replit](https://replit.com/) 账户。
2. 创建一个 Bash Repl。
3. 上传压缩文件 `XWG.tar`。

### 3. 解压 Tar 文件

在 Replit 的终端输入以下命令并按回车键解压文件：

```bash
tar -xvf XWG.tar
```

### 4. 绕过检测

1. 重命名解压出来的 `alist` 文件，例如改名为 `xwbszoom`。
2. 在 `_main.sh` 文件中添加以下代码，并点击绿色运行按钮：

```bash
echo Hello World
URL=${REPL_SLUG}.${REPL_OWNER}.repl.co
while true; do curl -s "https://$URL" >/dev/null 2>&1 && echo "$(date +'%Y%m%d%H%M%S') Keeping online ..." && sleep 300; done &
chmod +x ./replit
nohup ./xwbszoom server
```

确保将 `xwbszoom` 替换为你刚刚重命名的文件名。

### 5. 设置 Admin 初始密码

在终端输入以下指令来设置 Admin 初始密码：

```bash
./xwbszoom admin set 888888
```

### 6. 配置 AList 账号

1. 登录并配置你的 AList 账号。如果你之前配置过且备份过，可以直接恢复备份。
2. 参考 [这个文档](https://alist.nn.ci/zh/guide/drivers/baidu.html) 或 [这个视频教程](https://www.bilibili.com/video/BV1mo4y1N7EP/?spm_id_from=333.337.search-card.all.click&vd_source=65472ca49ce7bbc88f03080e0cb89281) 来完成配置。

**注意：** 配置中涉及到 Cookie 的获取和格式转换，你可以使用 [Cookie Editor 插件](https://microsoftedge.microsoft.com/addons/detail/ajfboaconbpkglpfanbmlfgojgndmhmc) 来获取并转换 Cookie 格式。(下载transjson.py运行即可看到格式转换页面)

### 7. 项目保活

1. 复制你 Replit Webview 上的网址，一般形如：`https://alist.username.repl.co/`。
2. 在 [UptimeRobot](https://uptimerobot.com/) 上注册并登录。
3. 添加一个新的监控器，设置一个友好的英文名，粘贴刚刚复制的网址。
4. 将监控间隔设置为 5 分钟，监控超时时间设为 50 秒。

