# 离线 Python 环境

离线 Python 环境的构建需要：

在有网的机器上：

* 下载服务器对应的 conda 安装包
* 下载 Python 虚拟环境 pkg 文件
* 下载 Python 库的 whl 文件

在离线服务器上：

* 安装 conda
* 安装 Python 虚拟环境
* 安装 Python 库

提示：

* 如果离线服务器已经安装 conda，可以不用重复安装
* 如果离线服务器已经有你需要的 Python 版本对应的虚拟环境，可以使用 `conda create --clone` 克隆旧的虚拟环境


# 下载 conda 安装包

如果你使用 Python 3.7，直接下载最新的 Anaconda 即可，自带许多机器学习环境，只有一些深度学习库没有自带。

如果你使用 Python 3.7 以下的版本，如 Python 3.6，那么你可以只下载 Miniconda。

目前最新的版本：

* https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh
* https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

清华源：

* https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2019.07-Linux-x86_64.sh
* https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh

```sh
mkdir -p ~/Downloads/offline
cd ~/Downloads/offline
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

# 下载 pkg 文件和 whl 文件

## 启动 miniconda 容器

```sh
docker run -it -v ~/Downloads/offline:/data -w /data continuumio/miniconda
```

## 添加 conda 源（可选）

可以加速下载。

```sh
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
```

## 下载 pkg 文件

首先删除已有的 pkg 文件，然后使用 `--download-only` 下载创建新的 python 环境需要的 pkg 文件，最后拷到 `/data`，对应下载文件夹下的 `offline/pkgs` 文件夹。

```sh
rm -rf /opt/conda/pkgs

conda create -n ypw python=3.6
source activate ypw

mkdir -p /data/pkgs
cd /opt/conda/pkgs
cp *.tar.bz2 /data/pkgs
```

## 配置 pip 源（可选）

可以加速下载。

```sh
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

## 下载 whl 文件

```sh
mkdir -p /data/whls
cd /data/whls
pip download jupyter jupyter_contrib_nbextensions numpy pandas scikit-learn matplotlib opencv-python pillow tqdm torch torchvision tensorflow-gpu keras tensorboardx
```

# 在离线机器上进行离线安装

## 将离线包传到离线机器上

```sh
rsync -avP ~/Downloads/offline fat:~/
```

## 安装 conda

```sh
bash ~/offline/Miniconda3-latest-Linux-x86_64.sh
```

## 创建 Python 虚拟环境

```sh
conda create -n ypw --offline
source activate ypw
conda install --offline ~/offline/pkgs/*
```

## 安装 whl 库

```sh
pip install --no-index --find-links=file:///home/richinfo/offline/whls jupyter jupyter_contrib_nbextensions numpy pandas scikit-learn matplotlib opencv-python pillow tqdm torch torchvision tensorflow-gpu keras tensorboardx
```
