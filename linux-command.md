# 常用 Linux 命令

### cd

切换工作目录。

`~` 是 home directory 的意思，`.`表示目前所在的目录，`..`表示目前目录位置的上一层目录。

`cd ..` 返回上一层目录。

### ssh 

连接远程服务器的命令。

例如： `ssh user@192.168.1.100`

### ls

`ls` 是 list 的缩写，用来显示目标列表。

`ll` 是 `ls -lh` 的别名，列出的信息更加详细。

### apt

Ubuntu 系统的包管理器，用于安装和卸载软件包。

安装：`sudo apt install curl`

卸载：`sudo apt purge curl`

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

复制文件。

### cat

显示文件的内容。

当文件较大时，文本会在屏幕上快速滚动，可以使用`Ctrl+S`停止滚动，`Ctrl+Q`恢复滚动，`Ctrl+C`退出当前命令。

### ping

测试主机之间网络的连通性。

例如：`ping baidu.com`

### zip

压缩命令，通过 `zip file.zip file`可以压缩一个文件，通过`zip files.zip -r dir`可以压缩整个文件夹。

### unzip

解压由 `zip` 命令压缩的 .zip 文件，如 `unzip files.zip`。

### tar

`*.tar` 打包文件：只是把很多小文件拼接在一起，速度快，不占用 CPU，比如 ImageNet 数据集就是一个打包文件，解包的速度非常快。打包后的文件大小和原始文件夹的大小基本一致。

`*.tar.gz` 压缩文件：先打包成一个文件，然后再压缩一遍，就是这个格式。如果文件是未压缩的格式，比如文本文件，使用这个格式可以有很高的压缩比。注意：jpg 和 png 格式是压缩后的格式，只打包就行，如果对 ImageNet 数据集先打包再压缩，就会有很长的耗时，并且文件不会明显变小。

* c：打包
* x：解包
* v：输出详细信息
* f：指定打包文件
* z：使用 gzip 压缩格式

`tar -cvf files.tar dir` 打包文件夹

`tar -xvf files.tar` 解包

`tar -czvf files.tar.gz dir` 压缩文件夹

`tar -xzvf files.tar.gz` 解压

### rsync

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

