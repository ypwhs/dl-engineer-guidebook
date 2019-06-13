# 常用 Linux 命令

### cd

切换工作目录。

`~` 是 home directory的意思，`.`表示目前所在的目录，`..`表示目前目录位置的上一层目录。

`cd ..` 返回上一层目录。

### ssh 

连接远程服务器的命令。

例如： `ssh user@192.168.1.100`

### ls

`ls` 是 list 的缩写，用来显示目标列表。

`ll` 是 `ls -lh` 的别名，列出的信息更加详细。

### apt

### pwd

`pwd` 命令以绝对路径的方式显示用户当前工作目录。

### mkdir

创建文件夹。

### rm

移除文件。移除文件夹时需要使用 `rm -r`，没有权限时需要`rm -rf` 。

此命令比较危险，注意不要写成这样：`rm -rf / tmp`，这样会删除`/`下的所有文件，属于删库跑路行为。

### mv

移动命令，如`mv source destination`。

### cp

### cat

### ping

测试主机之间网络的连通性。

例如：`ping baidu.com`

### zip

压缩命令，通过 `zip file.zip file`可以压缩一个文件，通过`zip files.zip -r dir`可以压缩整个文件夹

### unzip

解压由 `zip` 命令压缩的 .zip 文件，如 `unzip files.zip`。

### tar

### 

### export

### echo

### shutdown

### crontab

### service

### ps

### top

### htop

### kill



### **screen**

使得可以同时连接多个本地或远程的命令行会话，并在其间自由切换。

### tmux



### sudo

### su



### grep

### find

### sed

### awk

### diff

### vim

### sort

### args

### ftp

### free

### df

### du

### ifconfig

### mount

### chmod

### chown

### passwd

### uname

### whereis

### whatis

### locate

### man

### head

### tail

### wget

