# Ubuntu 装机步骤

* 安装 Ubuntu
* 配置 ssh

## 如何安装 Ubuntu

* 准备系统 U 盘
* 修改 BIOS 选择 U 盘启动
* 安装 Ubuntu

## 配置 ssh

### openssh-server

刚装好 Ubuntu 以后，为了能够方便地在笔记本上远程连接安装各种软件，我一般会先装openssh-server。

```bash
sudo apt update
sudo apt install openssh-server
```

装好了以后，就可以在终端里通过下面的命令连接服务器。

```bash
ssh 192.168.8.65
```

使用到的命令：[apt](linux-command.md#apt)、[ssh](linux-command.md#ssh)

### 使用 ssh-keygen 生成一个 SSH key

目前使用密码上不如使用 key 安全的，因为 key 的长度通常是 2048 或 4096 位，远超普通的密码。这里建议按照 GitHub 官方网站上的教程[生成新 SSH 密钥并添加到 ssh-agent](https://help.github.com/cn/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)，这样不仅可以用于登录 Linux 机器，也可以用于 git。

使用 `ssh-keygen` 生成了密钥以后，你会得到两个文件：

* `~/.ssh/id_rsa`
* `~/.ssh/id_rsa.pub`

其中 `id_rsa` 是私钥，`id_rsa.pub` 是公钥。

​公钥通常上这样的文本：

> ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDcfQD4nnaQrgC003C0ReAYqrm6XKEchuM6DwkNtHzRs2YhLolH6fEohWAp0mlW9yzQl258lA+FdoH51ONmvGUx/2Y953A6ujHrt7dOIpOkYW5HT6Rmvlwk+3uRmVNQqZTJeRWdblcSHmYY1fi1miawONZiVoLW14xhyH5bOwgwY/GB2yTaffDby451RLT5kQ7LHqiDJtWiRQekR5tKDKZ7mBhKZIKYLOoqAayCHw2scJYsgtw2tPt0/y7BlxO+RuDwuD2WOnthe1ewbwAbbTN17HiLvBd/MIWtVDoGGq6jdNDjNDNbTs8H2VohTc2mNtOOlycN6yzf3ZKZTN6/hNtl ypw@yangpeiendeiMac

### 在 Ubuntu 服务器上配置刚才生成的 SSH key

首先使用密码登录刚才的机器：

```bash
ssh 192.168.8.65
```

然后创建 `~/.ssh` 目录，并且创建 `~/.ssh/authorized_keys` 文件，配置好相应的权限：

```bash
mkdir -p ~/.ssh
touch ~/.ssh/authorized_keys
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

把刚才生成的公钥 `id_rsa.pub` 添加到 `~/.ssh/authorized_keys` 里，如果文件已经有内容，就添加在最后一行。这样以后**每次使用 ssh 登录机器都不需要再输入密码了**。

使用到的命令：[mkdir](linux-command.md#mkdir)、[touch](linux-command.md#touch)、[chmod](linux-command.md#chmod)、[nano](linux-command.md#nano)

### 禁止密码登录

由于密码登录存在不安全因素，比如暴露在公网的 IP 会被扫描，而 key 是绝对安全的，所以我们可以禁止密码登录：

```bash
sudo nano /etc/ssh/sshd_config

PasswordAuthentication no # 添加在最后一行
```

## 配置 sudo 免密码

由于安装驱动等操作需要 sudo 权限，为了避免频繁输入密码，可以配置 sudo 免密码：

```bash
sudo nano /etc/sudoers

ypw ALL=(ALL) NOPASSWD:ALL # 添加在最后一行
```



