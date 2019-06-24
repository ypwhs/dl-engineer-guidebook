---
description: 这里介绍了最常用的 Linux 命令，有一些在工作中是不可或缺的，还有一些能够极大的提高效率。想要熟练地使用多加练习即可！
---

# 常用 Linux 命令

### man

Linux 下的帮助命令。

授人以鱼不如授人以渔，首先应该教会大家查文档，而不是教会大家所有命令的用法。

如：`man ls`可以查看 ls 命令的帮助文档。

提示：按 q 退出帮助页面。

[![asciicast](https://asciinema.org/a/PFF2O1mkmPFMECrkunYHhjHvs.svg)](https://asciinema.org/a/PFF2O1mkmPFMECrkunYHhjHvs)

## 文件查看

### cd

切换工作目录。

`~` 是 home directory 的意思，`.`表示目前所在的目录，`..`表示目前目录位置的上一层目录。

`cd ..` 返回上一层目录。

### ls

`ls` 是 list 的缩写，用来显示目标列表。

`ll` 是`ls -lh` 的别名，列出的信息更加详细。

### pwd

`pwd` 命令以绝对路径的方式显示用户当前工作目录。

### cat

显示文件的内容：`cat file`

当文件较大时，文本会在屏幕上快速滚动，可以使用`Ctrl+S`停止滚动，`Ctrl+Q`恢复滚动，`Ctrl+C`退出当前命令。

### head

显示文件开头的内容，比如：`head -n 5 train.csv` 可以显示训练集 csv 前五行内容。

### tail

显示文件尾部的内容。`tail` 和 `head` 默认显示 10 行。

### find

在指定目录下查找文件。

### grep

筛选命令，比如我想查找许多文件里面的 markdown 文件：

```bash
ls -lh | grep .md
```

```text
➜  pytorch git:(ff608a9) ✗ ls -lh | grep .md
-rw-rw-r--  1 ypw ypw  15K 12月  5  2018 CONTRIBUTING.md
-rw-rw-r--  1 ypw ypw  285 12月  4  2018 mypy-README.md
-rw-rw-r--  1 ypw ypw  14K 12月  5  2018 README.md
```

### whereis

可以查找包含指定关键字的文件，如 `whereis python` 可以查找所有的文件名包含 python 的文件路径：

```text
➜  ~ whereis python
python: /usr/bin/python2.7 /usr/bin/python3.5 /usr/bin/python /usr/bin/python3.5m /usr/lib/python2.7 /usr/lib/python3.5 /etc/python2.7 /etc/python3.5 /etc/python /usr/local/lib/python2.7 /usr/local/lib/python3.5 /usr/include/python3.5m /usr/share/python /home/ypw/anaconda3/bin/python3.6 /home/ypw/anaconda3/bin/python3.6m-config /home/ypw/anaconda3/bin/python3.6-config /home/ypw/anaconda3/bin/python3.6m /home/ypw/anaconda3/bin/python /usr/share/man/man1/python.1.gz
```

### which

可以查找当前使用的命令的绝对路径。

如 `which python` 可以显示 `/home/ypw/anaconda3/bin/python`。

但是当你激活一个新的环境以后，就会得到不一样的结果：

```bash
➜  ~ source activate tensorflow
(tensorflow) ➜  ~ which python
/home/ypw/anaconda3/envs/tensorflow/bin/python
```

### locate

locate 命令会寻找包含关键字的所有文件路径。

## 文件读写

### mkdir

创建文件夹。

### touch

创建空文件。

### rm

移除文件。移除文件夹时需要使用`rm -r`，没有权限时需要`rm -rf` 。

此命令比较危险，注意不要写成这样：`rm -rf / tmp`，这样会删除`/`下的所有文件，属于删库跑路行为。

### cp

复制文件：`cp src dst`

复制文件夹：`cp -r src dst`

### mv

移动命令。

例如：`mv source destination`

[![asciicast](https://asciinema.org/a/hWFuRKiWoggP8xIH7ZKQGmABR.svg)](https://asciinema.org/a/hWFuRKiWoggP8xIH7ZKQGmABR)

### vim

编辑文件的命令，学习曲线比较陡峭，建议搜索相关教程学习。

## 打包压缩

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

## 权限管理

### sudo

以 root 权限执行命令，比如 `sudo reboot` 可以重启机器，普通权限无法重启。

### su

切换用户，比如 `sudo su ypw` 可以将当前用户切换到 ypw 用户。

### chmod

修改权限的命令，比如：`sudo chmod -R 777 data` 可以把 data 文件夹修改为任何人可以读写。

### chown

修改所有者的命令，比如：`sudo chown -R ypw data` 可以把 data 文件夹的所有权改为 ypw。

### passwd

修改密码命令，直接执行 `passwd` 可以修改当前用户密码。

强制修改某个用户的密码：`sudo passwd ypw`

## 进程管理

### ps

`ps aux` 可以列出所有进程的详细信息。

配合 grep 命令用比较好，比如 `ps aux | grep ipython | grep -v grep`

首先使用 `ps aux` 获取所有的进程信息，然后用 `grep ipython` 查找带有 python 的进程，最后使用 `grep -v grep` 过滤 grep 进程本身。

### kill

杀掉执行中的进程，刚才 ps 命令可以得到进程号，你可以根据进程号删除该进程，如 `kill 8339`

[![asciicast](https://asciinema.org/a/LI1QUFDERv148oZZ4qkDOhlIN.svg)](https://asciinema.org/a/LI1QUFDERv148oZZ4qkDOhlIN)

### killall

通过进程名来杀掉进程，请确保你不会影响其他人的情况下使用该命令。

如果同事正在使用 python 跑程序，你也在使用 python 跑程序，在你执行完 `killall python` 以后，你们的 python 进程都会被杀掉。

## 磁盘管理

### df

查看磁盘空间，比如 `df -h` 可以显示下面的内容：

```text
Filesystem      Size  Used Avail Use% Mounted on
udev             32G     0   32G   0% /dev
tmpfs           6.3G  9.5M  6.3G   1% /run
/dev/nvme0n1p2  916G  248G  622G  29% /
tmpfs            32G  679M   31G   3% /dev/shm
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs            32G     0   32G   0% /sys/fs/cgroup
/dev/nvme0n1p1  511M  3.5M  508M   1% /boot/efi
tmpfs           6.3G   32K  6.3G   1% /run/user/1000
```

使用 `df -ih` 可以查看 Inodes 使用情况，如果你的磁盘下存在很多小文件，那么你可以使用这个命令查看文件表是否用完了。

### du

可以查看文件夹大小，比如：`du -h ImageNet` 可以输出下面的内容：

```text
......
163M	ImageNet/train/n12620546
128M	ImageNet/train/n02108551
127M	ImageNet/train/n15075141
140G	ImageNet/train
6.4G	ImageNet/val
146G	ImageNet
```

### mount

挂载磁盘的命令，挂载硬盘：

```bash
sudo mount -t ext4 /dev/nvme0n1p1 /data
```

挂载 samba 网络盘：

```bash
sudo mount -t cifs -o username=ypw,password=**** //192.168.8.57/dataset /home/ypw/dataset
```

注意：此处需要 `sudo apt install cifs-utils` 。

## 系统管理

### apt

Ubuntu 系统的包管理器，用于安装和卸载软件包。

安装：`sudo apt install curl`

卸载：`sudo apt purge curl`

### export

设置环境变量命令，一般写在 `.bashrc` 或 `.zshrc` 文件中，例如：

```bash
export PATH=/usr/local/cuda/bin:$PATH
```

的功能是把 `/usr/local/cuda/bin` 目录添加到 `PATH` 的最前面，这样就可以直接在命令行使用 `/usr/local/cuda/bin` 目录下的 `nvcc` 命令。

### echo

可以输出环境变量。

例如：`echo $PATH`

### service

开启关闭服务的命令，如：

```bash
sudo service network-manager restart
```

### shutdown

关机命令。

例如：`sudo shutdown -t 0`

### reboot

重启命令。

例如：`sudo reboot`

## 系统监测

### uname

显示当前的系统信息。

`uname -a` 显示全部的信息，如内核版本号、硬件架构、主机名称和操作系统类型等。

### top

实时查看系统的运行状态，如 CPU、内存、进程的信息。

### ifconfig

这个命令可以查看当前网卡的 ip 地址。如：

```bash
➜  ~ ifconfig | grep inet
          inet addr:192.168.8.100  Bcast:192.168.8.255  Mask:255.255.255.0
          inet6 addr: fe80::211d:78f6:888a:1/64 Scope:Link
          inet addr:127.0.0.1  Mask:255.0.0.0
```

### free

查看内存使用情况，如：`free -h`

```text
              total        used        free      shared  buff/cache   available
Mem:            62G        404M         61G        9.4M        891M         61G
Swap:          976M          0B        976M
```

## 网络通信

### ping

测试主机之间网络的连通性。

例如：`ping baidu.com`

### ssh 

连接远程服务器：`ssh user@192.168.1.100`

映射远程端口：`ssh -L 本地端口:远程服务器:远程端口 远程服务器`

例如：`ssh -L 8888:localhost:8888 192.168.1.100` 可以把服务器上的 jupyter 监听的 8888 端口映射到本地的 8888 端口，然后只需要在浏览器里输入`http://localhost:8888` 就可以连接远程服务器的 jupyter 了。

### scp

复制文件/文件夹到远程服务器，例如：`scp 文件 用户名@目标主机:目标主机路径`

复制文件：`scp file user@192.168.1.100:/data`

复制文件夹：`scp -r dir user@192.168.1.100:/data`

当你复制大量小文件时，请使用`rsync` 命令。

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

[![asciicast](https://asciinema.org/a/eQjKRxlhu5vOThczbmkcmgbqH.svg)](https://asciinema.org/a/eQjKRxlhu5vOThczbmkcmgbqH)

### wget

从指定的URL下载文件。

下载单个文件：`wget url`

下载并修改文件名：`wget -O filename.zip url`

