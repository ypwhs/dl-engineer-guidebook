# Ubuntu 装机步骤

本文分为两个部分，如果你比较熟悉 Linux，可以直接看脚本式装机，速度快，效果好。

## 脚本式装机

```
FILE="/etc/sudoers.d/$USER"
if [ ! -f "$FILE" ]; then
    echo "Create $FILE and add sudo permission"
    echo "$USER ALL=(ALL) NOPASSWD:ALL" | sudo tee "$FILE"
fi
```

```
# 升级系统
sudo apt update
sudo apt upgrade -y
```

```
# 安装常用命令和 oh-my-zsh
sudo apt install -y openssh-server git curl zsh net-tools git curl htop nload tmux screen aria2 graphviz aptitude tree iotop cifs-utils landscape-common p7zip-full
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

```
# 安装 Python 环境
wget https://mirrors.bfsu.edu.cn/anaconda/miniconda/Miniconda3-py310_23.3.1-0-Linux-x86_64.sh
bash Miniconda3-py310_23.3.1-0-Linux-x86_64.sh -b
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```

```
# reboot your terminal
~/miniconda3/bin/conda activate
# pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
# pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

pip config set global.index-url https://mirrors.bfsu.edu.cn/pypi/web/simple
pip install torch==2.1.1+cu118 torchvision==0.16.1+cu118 --index-url https://download.pytorch.org/whl/cu118
pip install jupyter jupyter_contrib_nbextensions numpy pandas flask scikit-image scikit-learn matplotlib opencv-python pillow tqdm openpyxl ninja xtcocotools json_tricks munkres shapely ftfy pytest regex pyyaml yapf cython build twine memory_profiler
pip install openmim
mim install mmpretrain mmdet mmpose mmsegmentation
```

安装 CUDA：

Ubuntu 22.04 [参考链接](https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_network)：

```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb
sudo apt-get update
sudo apt-get -y install cuda-11-8
```

安装指定版本的 cudnn：

```sh
sudo apt install libcudnn8-dev=8.7.0.84-1+cuda11.8
```

添加 CUDA 环境变量：

```
# CUDA 环境变量
if [[ $(grep -L "cuda" ~/.bashrc) ]]; then
  echo "Add CUDA environment to ~/.bashrc"
  echo "export PATH=/usr/local/cuda/bin:\$PATH" | tee -a ~/.bashrc;
  echo "export LD_LIBRARY_PATH=/usr/local/cuda/lib64:\$LD_LIBRARY_PATH" | tee -a ~/.bashrc;
fi

if [[ $(grep -L "cuda" ~/.zshrc) ]]; then
  echo "Add CUDA environment to ~/.zshrc"
  echo "export PATH=/usr/local/cuda/bin:\$PATH" | tee -a ~/.zshrc;
  echo "export LD_LIBRARY_PATH=/usr/local/cuda/lib64:\$LD_LIBRARY_PATH" | tee -a ~/.zshrc;
fi
```

安装 mmdet：

```
mim install mmdet
```

## 分步骤安装

以下是分步骤安装的方法，分为以下几个步骤：

* 安装 Ubuntu
* 配置 ssh
* 配置 sudo 免密码 和 apt 源（推荐）
* 安装 oh my zsh 以及常用命令（推荐）
* 安装 NVIDIA 驱动、CUDA 和 cuDNN（分为 apt 和 run 两种安装方式）
* 安装 Anaconda 和 Python 库

这些步骤可能存在滞后性，如果你发现某个步骤已经过时了，可以提 issue 告诉我，或者直接修改这个文档。

## 安装 Ubuntu

以下是 Ubuntu 官方网站上的教程：

* [在 Windows 上制作 Ubuntu 系统盘](https://tutorials.ubuntu.com/tutorial/tutorial-create-a-usb-stick-on-windows)
* [在 macOS 上制作 Ubuntu 系统盘](https://tutorials.ubuntu.com/tutorial/tutorial-create-a-usb-stick-on-macos)
* [安装 Ubuntu](https://tutorials.ubuntu.com/tutorial/tutorial-install-ubuntu-desktop)

目前我安装的版本是 [Ubuntu 18.04](http://releases.ubuntu.com/18.04/)

如果遇到网络问题，可以使用清华大学的镜像：[https://mirror.tuna.tsinghua.edu.cn/ubuntu-releases/18.04.4/ubuntu-18.04.4-desktop-amd64.iso](https://mirror.tuna.tsinghua.edu.cn/ubuntu-releases/18.04.4/ubuntu-18.04.4-desktop-amd64.iso)

如果上面的链接失效了，说明 ubuntu 出新版了，你可以在这里查找新版：[https://mirror.tuna.tsinghua.edu.cn/ubuntu-releases/](https://mirror.tuna.tsinghua.edu.cn/ubuntu-releases/)。

## 配置 ssh

### 安装 openssh-server

装好 Ubuntu 以后，为了能够方便地在其他终端上远程连接，安装各种软件，我一般会先装 openssh-server。

```bash
sudo apt update
sudo apt install openssh-server
```

装好了以后，就可以在终端里通过下面的命令连接服务器。

```bash
ssh 192.168.8.65
```

使用到的命令：[apt](linux-command.md#apt)、[ssh](linux-command.md#ssh)

### 使用 ssh-keygen 生成一个 ssh key

目前使用密码上不如使用 key 安全的，因为 key 的长度通常是 2048 或 4096 位，远超普通的密码。这里建议按照 GitHub 官方网站上的教程[生成新 SSH 密钥并添加到 ssh-agent](https://help.github.com/cn/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)，这样不仅可以用于登录 Linux 机器，也可以用于 git。

使用 `ssh-keygen` 生成了密钥以后，你会得到两个文件：

* `~/.ssh/id_rsa`
* `~/.ssh/id_rsa.pub`

其中 `id_rsa` 是私钥，`id_rsa.pub` 是公钥。不要把私钥发给任何人。

公钥通常上这样的文本：

> ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDcfQD4nnaQrgC003C0ReAYqrm6XKEchuM6DwkNtHzRs2YhLolH6fEohWAp0mlW9yzQl258lA+FdoH51ONmvGUx/2Y953A6ujHrt7dOIpOkYW5HT6Rmvlwk+3uRmVNQqZTJeRWdblcSHmYY1fi1miawONZiVoLW14xhyH5bOwgwY/GB2yTaffDby451RLT5kQ7LHqiDJtWiRQekR5tKDKZ7mBhKZIKYLOoqAayCHw2scJYsgtw2tPt0/y7BlxO+RuDwuD2WOnthe1ewbwAbbTN17HiLvBd/MIWtVDoGGq6jdNDjNDNbTs8H2VohTc2mNtOOlycN6yzf3ZKZTN6/hNtl ypw@yangpeiendeiMac

### 在 Ubuntu 服务器上添加刚才生成的 ssh key

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
nano ~/.ssh/authorized_keys

# 添加你的公钥，如 ssh-rsa AAAA...
```

把刚才生成的公钥 `id_rsa.pub` 添加到 `~/.ssh/authorized_keys` 里，如果文件已经有内容，就添加在最后一行。这样以后**每次使用 ssh 登录机器都不需要再输入密码了**。

使用到的命令：[mkdir](linux-command.md#mkdir)、[touch](linux-command.md#touch)、[chmod](linux-command.md#chmod)、[nano](linux-command.md#nano)

### 禁止密码登录

由于密码登录存在不安全因素，比如暴露在公网的 IP 会被扫描，而 key 是相对安全的，所以我们可以禁止不安全的密码登录：

```bash
sudo nano /etc/ssh/sshd_config

PasswordAuthentication no # 添加在最后一行
```

## 配置 sudo 免密码 和 apt 源

### 配置 sudo 免密码

Ubuntu 22.04 以前：

由于安装驱动等操作需要 sudo 权限，为了避免频繁输入密码，可以配置 sudo 免密码：

```bash
sudo nano /etc/sudoers

ypw ALL=(ALL) NOPASSWD:ALL # 添加在最后一行
```

Ubuntu 22.04 及以后：

`/etc/sudoers` 在 22.04 之后变得不可写： `[ /etc/sudoers is meant to be read-only ]`

因此你需要在 `/etc/sudoers.d/` 文件夹下创建自己的文件：

```
sudo nano /etc/sudoers.d/ypw

ypw ALL=(ALL) NOPASSWD:ALL # 写入到文件中
```

### 配置 apt 源

在使用 apt 的时候有可能因为网络原因导致安装过慢或失败，这时候可以配置一些 apt 源：

* [https://mirror.tuna.tsinghua.edu.cn/help/ubuntu/](https://mirror.tuna.tsinghua.edu.cn/help/ubuntu/)
* [https://opsx.alibaba.com/mirror](https://opsx.alibaba.com/mirror)

下面以清华大学开源软件镜像站为例：

```bash
sudo mv /etc/apt/sources.list /etc/apt/sources_backup.list
sudo nano /etc/apt/sources.list

# 添加下面的内容，保存
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
```

添加好以后，使用下面的命令更新 apt 以后，安装其他软件包的速度就会变快：

```bash
sudo apt update
```

恢复默认源：

```bash
sudo mv /etc/apt/sources_backup.list /etc/apt/sources.list
```

## 安装 oh my zsh 以及常用命令

### 安装 oh my zsh

相比默认的 bash，zsh 有以下几个优点：

* 当你使用 tab 提示的时候，如果有多个匹配项，你可以用 tab 进行切换
* 当你想使用一个之前输入过的命令的时候，只需要输入首字母，然后按上方向键切换

安装 oh my zsh 的步骤如下：

* 安装 [zsh](https://github.com/robbyrussell/oh-my-zsh/wiki/Installing-ZSH)
* 安装 [oh my zsh](https://ohmyz.sh/)

完整命令如下：

```bash
sudo apt install -y git curl zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

### 常用命令

这些是我的[必备命令](ubuntu-environment.md#bi-bei-ming-ling)，你可以按照自己的需要安装：

```bash
sudo apt install -y net-tools git curl htop nload tmux screen aria2 graphviz aptitude tree iotop
```

## 安装 NVIDIA 驱动、CUDA 和 cuDNN（apt）

安装驱动有两种方法，一种是使用apt安装，一种是直接下载驱动安装。我一般会选择直接下载驱动。

### 使用 apt 安装驱动

安装过程可以参考 TensorFlow 的教程：[https://www.tensorflow.org/install/gpu](https://www.tensorflow.org/install/gpu)

下面是我安装的命令：

```bash
# Add NVIDIA package repositories
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
sudo apt update
wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
sudo apt install ./nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
sudo apt update

# Install NVIDIA driver
sudo aptitude install nvidia-driver-410
# Reboot. Check that GPUs are visible using the command: nvidia-smi
```

如果因为网络原因导致下载很慢，可以使用下面的命令让 apt 使用代理：

```bash
sudo nano /etc/apt/apt.conf

# 下面的内容按照实际情况进行修改
Acquire::http::Proxy "http://192.168.8.246:1087";
```

为了避免重启以后鼠标键盘没反应，需要运行下面的命令：

```bash
sudo apt install --reinstall xserver-xorg-input-all
```

### 测试显卡

装好系统以后需要重新启动机器，重启以后运行下面的命令即可测试显卡：

```bash
nvidia-smi
```

如果能看到类似的内容就说明显卡驱动装好了：

```text
Fri Jan 15 21:15:14 2021
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.32.03    Driver Version: 460.32.03    CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce RTX 3080    Off  | 00000000:01:00.0  On |                  N/A |
| 31%   22C    P8     6W / 320W |    183MiB / 10015MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      1151      G   /usr/lib/xorg/Xorg                142MiB |
|    0   N/A  N/A      1454      G   /usr/bin/gnome-shell               38MiB |
+-----------------------------------------------------------------------------+
```

### 安装 CUDA 和 cuDNN

注意：

* 此步骤需下载较大的安装包
* PyTorch 用户可以不安装 CUDA 和 cuDNN

```bash
sudo apt install --no-install-recommends \
    cuda-10-0 \
    libcudnn7=7.6.0.64-1+cuda10.0  \
    libcudnn7-dev=7.6.0.64-1+cuda10.0
```

### 配置环境变量

安装好以后还需要[配置环境变量](linux-command.md#export)，这里我以 `~/.zshrc` 为例：

```bash
nano ~/.zshrc

# 添加下面的内容
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
```

### 安装 TensorRT（可选）

```bash
sudo apt update
sudo apt install -y --no-install-recommends libnvinfer5=5.1.5-1+cuda10.0
sudo apt install -y --no-install-recommends libnvinfer-dev=5.1.5-1+cuda10.0
```

## 安装 NVIDIA 驱动、CUDA 和 cuDNN（run）

### 下载驱动

首先去官网下载驱动：[https://www.nvidia.com/Download/index.aspx?lang=cn](https://www.nvidia.com/Download/index.aspx?lang=cn)

有下面几种方法可以下载：

* 在 Ubuntu 机器上直接使用浏览器下载
* 在自己机器上下载，然后通过 [scp](linux-command.md#scp) 传到 Ubuntu 机器上
* 在自己机器上找到下载地址，然后在 Ubuntu 机器上使用 wget 命令下载

以上方法可以根据实际情况选择，这里我选择第三种方法：

```bash
wget https://cn.download.nvidia.cn/XFree86/Linux-x86_64/450.80.02/NVIDIA-Linux-x86_64-450.80.02.run
```

### 屏蔽 Nouveau

如果你没有屏蔽，就会出现以下提示：

> ERROR: The Nouveau kernel driver is currently in use by your system. This driver is incompatible with the NVIDIA driver, and must be disabled before proceeding. Please consult the NVIDIA driver README and your Linux distribution's documentation for details on how to correctly disable the Nouveau kernel driver.

命令：

```bash
sudo nano /etc/modprobe.d/blacklist-nouveau.conf

# 添加以下内容

blacklist nouveau
options nouveau modeset=0

# 保存

sudo update-initramfs -u
sudo reboot
```

### 安装必要的编译工具

如果没有安装 gcc 等编译工具，就会出现以下提示：

> ERROR: Unable to find the development tool `cc` in your path; please make sure that you have the package 'gcc' installed. If gcc is installed on your system, then please check that `cc` is in your PATH.

命令：

```bash
sudo apt install -y build-essential gcc g++ make binutils linux-headers-`uname -r`
```

### 安装显卡驱动

```bash
sudo bash NVIDIA-Linux-x86_64-450.80.02.run
```

安装步骤很简单，一直下一步就好了。

### 测试显卡

```bash
nvidia-smi
```

如果能看到类似的内容就说明显卡驱动装好了：

```text
Fri Jan 15 21:15:14 2021
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.32.03    Driver Version: 460.32.03    CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce RTX 3080    Off  | 00000000:01:00.0  On |                  N/A |
| 31%   22C    P8     6W / 320W |    183MiB / 10015MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      1151      G   /usr/lib/xorg/Xorg                142MiB |
|    0   N/A  N/A      1454      G   /usr/bin/gnome-shell               38MiB |
+-----------------------------------------------------------------------------+
```

### 安装 CUDA 和 cuDNN

由于不同的深度学习框架的 CUDA 和 cuDNN 版本依赖是不同的，所以请按照你所需要的深度学习框架官网上的说明为准。关于 CUDA 版本、cuDNN版本以及深度学习环境的介绍，请看 [Ubuntu 环境](ubuntu-environment.md)。

提示：PyTorch 用户可以不安装 CUDA 和 cuDNN。

### 安装 CUDA 10.0

由于此安装包比较大，建议使用 aria2c 下载：

```bash
aria2c -x 16 https://developer.nvidia.com/compute/cuda/10.0/Prod/local_installers/cuda_10.0.130_410.48_linux
```

下载好了以后，直接运行安装即可：

```bash
sudo bash cuda_10.0.130_410.48_linux.run

# 按 q 退出 EULA

NVIDIA CUDA Toolkit
Do you accept the previously read EULA?
accept/decline/quit: accept

Install NVIDIA Accelerated Graphics Driver for Linux-x86_64 410.48?
(y)es/(n)o/(q)uit: n

Install the CUDA 10.0 Toolkit?
(y)es/(n)o/(q)uit: y

Enter Toolkit Location
 [ default is /usr/local/cuda-10.0 ]:

Do you want to install a symbolic link at /usr/local/cuda?
(y)es/(n)o/(q)uit: y

Install the CUDA 10.0 Samples?
(y)es/(n)o/(q)uit: n

Installing the CUDA Toolkit in /usr/local/cuda-10.0 ...

===========
= Summary =
===========

Driver:   Not Selected
Toolkit:  Installed in /usr/local/cuda-10.0
Samples:  Not Selected
```

可以按照自己的需要请配置下面的选项，比如你想学习使用 C/C++ 编写 CUDA 程序，可以安装 Samples。

注意：

> Please make sure that
>
> * PATH includes /usr/local/cuda-10.0/bin
> * LD\_LIBRARY\_PATH includes /usr/local/cuda-10.0/lib64, or, add /usr/local/cuda-10.0/lib64 to /etc/ld.so.conf and run ldconfig as root

需要按照上面的指示[配置环境变量](linux-command.md#export)，这里我以 `~/.zshrc` 为例：

```bash
nano ~/.zshrc

# 添加下面的内容
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$PATH
```

### 安装 cuDNN

同样，下载 cudnn-10.0-linux-x64-v7.6.0.64.tgz：

```bash
aria2c -x 16 http://developer.download.nvidia.com/compute/redist/cudnn/v7.6.0/cudnn-10.0-linux-x64-v7.6.0.64.tgz
```

然后安装到 `/usr/local` 目录下：

```bash
sudo tar -xzf cudnn-10.0-linux-x64-v7.6.0.64.tgz -C /usr/local
```

## 安装 Anaconda 和 Python 库

### 安装 Anaconda

安装 Anaconda 和 Python 库的步骤都已经写在了 [Pyhton 环境](python-environment.md)，这里仅仅展示相关命令：

```bash
aria2c -x 16 https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2019.03-Linux-x86_64.sh
bash Anaconda3-2019.03-Linux-x86_64.sh

# 回车，然后按 q 退出 EULA

Do you accept the license terms? [yes|no]
[no] >>> yes

Anaconda3 will now be installed into this location:
/home/ypw/anaconda3

  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below

[/home/ypw/anaconda3] >>>
PREFIX=/home/ypw/anaconda3
installing: python-3.7.3-h0371630_0 ...
Python 3.7.3
installing: conda-env-2.6.0-1 ...
installing: blas-1.0-mkl ...
......
installing: anaconda-2019.03-py37_0 ...
installation finished.
Do you wish the installer to initialize Anaconda3
by running conda init? [yes|no]
[no] >>> yes

......

Thank you for installing Anaconda3!
```

安装完成以后，你可能还需要[配置环境变量](python-environment.md#pei-zhi-huan-jing-bian-liang)。

```bash
~/anaconda3/bin/conda init

# 如果你用的终端是zsh
~/anaconda3/bin/conda init zsh
```

配置好以后，可以重启机器，或者使用 `source ~/.zshrc` [更新环境变量](linux-command.md#source)。

### 配置 pip 源

在使用 pip 的时候有可能因为网络原因导致安装过慢或失败，这时候可以[配置国内的 pip 源](python-environment.md#pip)：

* [https://developer.aliyun.com/mirror/pypi](https://developer.aliyun.com/mirror/pypi)
* [https://mirror.tuna.tsinghua.edu.cn/help/pypi/](https://mirror.tuna.tsinghua.edu.cn/help/pypi/)

下面以阿里云为例：

```bash
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
```

### Python 库

使用下面的命令安装[常用 Python 库](python-environment.md#python-ku)：

```bash
pip install jupyter jupyter_contrib_nbextensions numpy pandas scikit-learn matplotlib opencv-python pillow tqdm torch torchvision tensorflow-gpu keras tensorboardx xlrd openpyxl
```

注意：如果是 30 系列的显卡，比如 3080、3090，需要使用CUDA11或以上的深度学习框架，比如 PyTorch 目前是这样安装的：

```bash
pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
```

### 测试 PyTorch

```python
import torch
dummy = torch.zeros(1, 3, 5, 5).cuda()
conv = torch.nn.Conv2d(in_channels=3, out_channels=1, kernel_size=3).cuda()
print(conv(dummy))
```

期望输出：

```
tensor([[[[0.0443, 0.0443, 0.0443],
          [0.0443, 0.0443, 0.0443],
          [0.0443, 0.0443, 0.0443]]]], device='cuda:0',
       grad_fn=<CudnnConvolutionBackward>)
```

### 测试 TensorFlow

```bash
import tensorflow as tf
mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)
```

期望输出（注意里面的 GeForce GTX 1080 Ti） ：

```text
>>> model.fit(x_train, y_train, epochs=5)
2019-07-21 17:18:16.455944: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2019-07-21 17:18:16.460577: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 3599995000 Hz
2019-07-21 17:18:16.461013: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x5606e83e4f40 executing computations on platform Host. Devices:
2019-07-21 17:18:16.461032: I tensorflow/compiler/xla/service/service.cc:175]   StreamExecutor device (0): <undefined>, <undefined>
2019-07-21 17:18:16.462663: I tensorflow/stream_executor/platform/default/dso_loader.cc:42] Successfully opened dynamic library libcuda.so.1
2019-07-21 17:18:16.915819: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:1005] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2019-07-21 17:18:16.916435: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x5606e78c9a40 executing computations on platform CUDA. Devices:
2019-07-21 17:18:16.916504: I tensorflow/compiler/xla/service/service.cc:175]   StreamExecutor device (0): GeForce GTX 1080 Ti, Compute Capability 6.1
2019-07-21 17:18:16.916782: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:1005] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2019-07-21 17:18:16.918218: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1640] Found device 0 with properties:
name: GeForce GTX 1080 Ti major: 6 minor: 1 memoryClockRate(GHz): 1.683
pciBusID: 0000:0b:00.0
2019-07-21 17:18:16.918581: I tensorflow/stream_executor/platform/default/dso_loader.cc:42] Successfully opened dynamic library libcudart.so.10.0
2019-07-21 17:18:16.920971: I tensorflow/stream_executor/platform/default/dso_loader.cc:42] Successfully opened dynamic library libcublas.so.10.0
2019-07-21 17:18:16.922961: I tensorflow/stream_executor/platform/default/dso_loader.cc:42] Successfully opened dynamic library libcufft.so.10.0
2019-07-21 17:18:16.923461: I tensorflow/stream_executor/platform/default/dso_loader.cc:42] Successfully opened dynamic library libcurand.so.10.0
2019-07-21 17:18:16.926265: I tensorflow/stream_executor/platform/default/dso_loader.cc:42] Successfully opened dynamic library libcusolver.so.10.0
2019-07-21 17:18:16.928450: I tensorflow/stream_executor/platform/default/dso_loader.cc:42] Successfully opened dynamic library libcusparse.so.10.0
2019-07-21 17:18:16.932250: I tensorflow/stream_executor/platform/default/dso_loader.cc:42] Successfully opened dynamic library libcudnn.so.7
2019-07-21 17:18:16.932341: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:1005] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2019-07-21 17:18:16.932899: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:1005] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2019-07-21 17:18:16.933392: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1763] Adding visible gpu devices: 0
2019-07-21 17:18:16.933426: I tensorflow/stream_executor/platform/default/dso_loader.cc:42] Successfully opened dynamic library libcudart.so.10.0
2019-07-21 17:18:16.934335: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1181] Device interconnect StreamExecutor with strength 1 edge matrix:
2019-07-21 17:18:16.934353: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1187]      0
2019-07-21 17:18:16.934363: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1200] 0:   N
2019-07-21 17:18:16.934444: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:1005] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2019-07-21 17:18:16.934988: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:1005] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2019-07-21 17:18:16.935504: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1326] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 10481 MB memory) -> physical GPU (device: 0, name: GeForce GTX 1080 Ti, pci bus id: 0000:0b:00.0, compute capability: 6.1)
Epoch 1/5
2019-07-21 17:18:17.663035: I tensorflow/stream_executor/platform/default/dso_loader.cc:42] Successfully opened dynamic library libcublas.so.10.0
60000/60000 [==============================] - 3s 49us/sample - loss: 0.2209 - acc: 0.9344
Epoch 2/5import torch
x = torch.rand(5, 3)
print(x)
60000/60000 [==============================] - 2s 39us/sample - loss: 0.0968 - acc: 0.9707
Epoch 3/5
60000/60000 [==============================] - 2s 38us/sample - loss: 0.0696 - acc: 0.9779
Epoch 4/5
60000/60000 [==============================] - 2s 38us/sample - loss: 0.0537 - acc: 0.9826
Epoch 5/5
60000/60000 [==============================] - 2s 38us/sample - loss: 0.0428 - acc: 0.9863
<tensorflow.python.keras.callbacks.History object at 0x7f4ece4a2278>
>>> model.evaluate(x_test, y_test)
10000/10000 [==============================] - 0s 24us/sample - loss: 0.0698 - acc: 0.9804
[0.06983174340333789, 0.9804]
```
