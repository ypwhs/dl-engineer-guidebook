# 常用 Linux 命令

### cd

切换工作目录。

`~` 是 home directory 的意思，`.`表示目前所在的目录，`..`表示目前目录位置的上一层目录。

`cd ..` 返回上一层目录。

### ssh 

连接远程服务器：`ssh user@192.168.1.100`

映射远程端口：`ssh -L 本地端口:远程服务器:远程端口 远程服务器`

例如：`ssh -L 8888:localhost:8888 192.168.1.100` 可以把服务器上的 jupyter 监听的 8888 端口映射到本地的 8888 端口，然后只需要在浏览器里输入`http://localhost:8888` 就可以连接远程服务器的 jupyter 了。

### scp

复制文件/文件夹到远程服务器，例如：`scp 文件 用户名@目标主机:目标主机路径`

复制文件：`scp file user@192.168.1.100:/data`

复制文件夹：`scp -r dir user@192.168.1.100:/data`

当你复制大量小文件时，请使用`rsync` 命令。

### ls

`ls` 是 list 的缩写，用来显示目标列表。

`ll` 是`ls -lh` 的别名，列出的信息更加详细。

### apt

Ubuntu 系统的包管理器，用于安装和卸载软件包。

安装：`sudo apt install curl`

卸载：`sudo apt purge curl`

### pwd

`pwd` 命令以绝对路径的方式显示用户当前工作目录。

### mkdir

创建文件夹。

### rm

移除文件。移除文件夹时需要使用`rm -r`，没有权限时需要`rm -rf` 。

此命令比较危险，注意不要写成这样：`rm -rf / tmp`，这样会删除`/`下的所有文件，属于删库跑路行为。

### mv

移动命令。

例如：`mv source destination`

### cp

复制文件：`cp src dst`

复制文件夹：`cp -r src dst`

### cat

显示文件的内容：`cat file`

当文件较大时，文本会在屏幕上快速滚动，可以使用`Ctrl+S`停止滚动，`Ctrl+Q`恢复滚动，`Ctrl+C`退出当前命令。

### ping

测试主机之间网络的连通性。

例如：`ping baidu.com`

### zip

压缩命令，通过`zip file.zip file`可以压缩一个文件，通过`zip files.zip -r dir`可以压缩整个文件夹。

### unzip

解压由`zip` 命令压缩的 .zip 文件。

例如：`unzip files.zip`

### tar

`*.tar` 打包文件：只是把很多小文件拼接在一起，速度快，不占用 CPU，比如 ImageNet 数据集就是一个打包文件，解包的速度非常快。打包后的文件大小和原始文件夹的大小基本一致。

`*.tar.gz` 压缩文件：先打包成一个文件，然后再压缩一遍，就是这个格式。如果文件是未压缩的格式，比如文本文件，使用这个格式可以有很高的压缩比。注意：jpg 和 png 格式是压缩后的格式，只打包就行，如果对 ImageNet 数据集先打包再压缩，就会有很长的耗时，并且文件不会明显变小。

* c：打包
* x：解包
* v：输出详细信息
* f：指定打包文件
* z：使用 gzip 压缩格式

打包文件夹：`tar -cvf files.tar dir` 

解包：`tar -xvf files.tar` 

压缩文件夹：`tar -czvf files.tar.gz dir` 

解压：`tar -xzvf files.tar.gz` 

### rsync

同步文件/文件夹命令，带有增量备份功能，速度很快。

参数：

* -a，--archive 归档模式，表示以递归方式传输文件，并保持所有文件属性，等于-rlptgoD。
* -v，--verbose 详细模式输出。
* -z，--compress 在传输时压缩数据，如果你传输的文件没有压缩过，并且带宽不够大，就可以开启压缩。如果你传输的是图像文件，那么压缩会拖慢传输速度。
* --delete，在同步的时候删除多余的文件，这可以确保两个文件夹的一致性。
* --exclude，排除文件，可以使用通配符
* -P，等同于 --partial --progress，显示备份过程。

同步文件夹：`rsync -avP 本地文件夹 用户名@远程服务器:远程地址`

### export

设置环境变量命令，一般写在 `.bashrc` 或 `.zshrc` 文件中，例如：

```bash
export PATH=/usr/local/cuda/bin:$PATH
```

的功能是把 `/usr/local/cuda/bin` 目录添加到 `PATH` 的最前面，这样就可以直接在命令行使用 `/usr/local/cuda/bin` 目录下的 `nvcc` 命令。

### echo

可以输出环境变量。

例如：`echo $PATH`

### shutdown

关机命令。

例如：`sudo shutdown -t 0`

### wget

从指定的URL下载文件。

### ps

### top

### htop

### kill

### **screen**

### tmux

### sudo

### su

### crontab

### service

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

### 

