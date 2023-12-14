# 离线 Python 环境

有时因为限制，我们不能够在目标机器上使用网络安装 Python 环境，那么如何离线构建 Anaconda 虚拟环境，以及如何离线安装各种 Python 库，就是一个必须要思考的问题。我会在这篇文章里介绍我在离线安装 Anaconda 和配置 Python 环境方面的一些经验。

离线构建 Python 环境的构建需要：

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


## 下载 conda 安装包

如果你使用的 Python 版本是 Python 3.7，那么直接下载最新的 Anaconda 即可，自带 Python 3.7 以及许多机器学习环境，只需要离线安装一些深度学习库，这部分内容可以参考下面的下载whl文件。

如果你使用 Python 3.7 以下的版本，如 Python 3.6，那么你可以只下载 Miniconda，然后通过 pkg 里先安装你想要的Python 版本。为什么不下载 Anaconda 呢？因为它很大，而且里面的 Python 版本并不是我们需要的版本。

目前最新的 Anaconda 和 Miniconda 下载链接：

* https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh
* https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

如果你遇到了网络问题，可以使用[清华大学开源软件镜像站的 Anaconda 镜像](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/)：

* https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2019.07-Linux-x86_64.sh
* https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh

可以使用下面的命令来下载：

```sh
mkdir -p ~/Downloads/offline
cd ~/Downloads/offline
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

<script id="asciicast-sI5AYLfu71HaWTJiOLQrcauXJ" src="https://asciinema.org/a/sI5AYLfu71HaWTJiOLQrcauXJ.js" async></script>

## 下载 pkg 文件和 whl 文件

`pip download` 可以下载你所需要和依赖的 Python 库对应的 whl 安装包，但是你必须确保系统内核和 Python 版本一致。如果你使用的是 Mac，而目标机器是 Linux，那么你就不能够使用 `pip download` 命令很方便地下载所有依赖的 whl 文件。为了简化这一问题，我们可以使用 Docker 创建一个 Linux 环境来完成下载任务。

### 启动 miniconda 容器

通过 `-v` 参数，我们可以将 Docker 内部的 `/data` 路径和本地的 `~/Downloads/offline` 路径链接起来，这样当我们下载到 `/data` 时，就可以在本机的 `~/Downloads/offline` 文件夹里看到。

```sh
docker run -it -v ~/Downloads/offline:/data -w /data continuumio/miniconda
```

### 添加 conda 源（可选）

通过添加[清华大学开源软件镜像站的 Anaconda 镜像](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)，我们可以加速下载过程。

```sh
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
```

### 下载 pkg 文件

Anaconda 所有的库都是通过 pkg 安装的，我们只要下载这些 pkg 文件，即可创建我们想要的环境。

首先删除 miniconda docker 里已有的 pkg 文件，因为 miniconda 默认安装了 Python 2.7，我们不希望在安装 Python 3.6 的时候有 Python 2.7 的 pkg 文件。

然后我们创建一个 Python 3.6 环境。如果你希望安装 Python 的其他版本，可以在创建环境的时候自行修改版本号。

创建好环境以后，所有需要的 pkg 文件（后缀名是 `.tar.bz2`）就会下载到 `/opt/conda/pkgs` 目录下，我们只需要把它们拷到 `/data` 目录下，即可在本机的下载文件夹里看见。

```sh
rm -rf /opt/conda/pkgs

conda create -n ypw python=3.6
source activate ypw

mkdir -p /data/pkgs
cd /opt/conda/pkgs
cp *.tar.bz2 /data/pkgs
```

<script id="asciicast-RXDdXjvhHVqbRgFiDbJzHMmN9" src="https://asciinema.org/a/RXDdXjvhHVqbRgFiDbJzHMmN9.js" async></script>

### 配置 pip 源（可选）

通过添加[清华大学开源软件镜像站的 Pypi 镜像](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)，我们可以加速下载过程。

```sh
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### 下载 whl 文件

whl 文件就是我们常说的 Python 库的安装文件，下面是我常用的 Python 库，你可以根据自己的需要进行修改。

```sh
mkdir -p /data/whls
cd /data/whls
pip download jupyter jupyter_contrib_nbextensions numpy pandas scikit-learn matplotlib opencv-python pillow tqdm torch torchvision tensorflow-gpu keras tensorboardx
```

<script id="asciicast-ZjK3RkkKLrTt10mMIrWMaPiLE" src="https://asciinema.org/a/ZjK3RkkKLrTt10mMIrWMaPiLE.js" async></script>

## 在离线机器上进行离线安装

### 将离线包传到离线机器上

下载好所有需要的离线安装包以后，我们就需要将它们传到离线服务器上，然后逐个安装。如果你的机器不支持[rsync](linux-command.md#rsync) 命令，可以使用 [scp](linux-command.md#scp) 命令。

```sh
rsync -avP ~/Downloads/offline fat:~/
```

### 安装 conda

安装 conda 直接使用 bash 运行，然后按照提示进行即可。

```sh
bash ~/offline/Miniconda3-latest-Linux-x86_64.sh
```

<script id="asciicast-oDPnKVGHItMjVZ2RtzSOE916F" src="https://asciinema.org/a/oDPnKVGHItMjVZ2RtzSOE916F.js" async></script>

### 创建 Python 虚拟环境

先创建一个空环境，然后安装已经下载好的 pkg 文件，你就可以离线创建一个 Python 3.6 的环境。

```sh
conda create -n ypw --offline
source activate ypw
conda install --offline ~/offline/pkgs/*
```

### 安装 whl 库

最后，使用 pip 离线安装下载好的 whl 文件。

```sh
pip install --no-index --find-links=file:///home/richinfo/offline/whls jupyter jupyter_contrib_nbextensions numpy pandas scikit-learn matplotlib opencv-python pillow tqdm torch torchvision tensorflow-gpu keras tensorboardx
```

<script id="asciicast-EHRE3XtioqXdTt5VLvRGWxzmQ" src="https://asciinema.org/a/EHRE3XtioqXdTt5VLvRGWxzmQ.js" async></script>
