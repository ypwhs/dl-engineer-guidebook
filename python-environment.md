# Python 环境



对于深度学习工程师来说，Python 是必不可少的工具，因为大多数深度学习框架都支持 Python（比如 tensorflow、pytorch、mxnet 等）。在模型开发阶段，使用 Python 非常方便，如果配合 jupyter 使用，还可以进一步提升开发效率。

### Anaconda

Anaconda 是一个 Pyhton 的包管理器，它可以简化 Python 环境的安装。由于 Ubuntu 系统、macOS 系统的局限性，我们尽量不要在系统自带的环境里安装深度学习库，不然可能会出现一些不可预料的问题。

Anaconda 不需要 root 权限，所以可以很方便地安装在用户目录下，只要配置好环境变量即可使用，当你不需要它的时候，只需要直接删除它的目录，然后将对应的环境变量一起删除即可。

还有一个好处就是，你可以直接 scp 整个环境文件夹到其他相同硬件的机器上，它们的环境可以保持绝对的统一，可以极大简化运维的工作。

#### 安装 Anaconda

Anaconda 官方下载页面：[https://www.anaconda.com/downloads](https://www.anaconda.com/downloads)

你只需要下载对应系统的安装包，然后直接运行安装包即可。比如在 macOS 上安装 Anaconda：

```bash
wget https://repo.anaconda.com/archive/Anaconda3-2019.03-MacOSX-x86_64.sh
bash Anaconda3-2019.03-MacOSX-x86_64.sh
```

**提示：**需要使用 brew 安装 wget 命令。

#### 使用 Anaconda 创建其他 Python 环境

如果我们需要其他 Python 环境，可以使用 conda 创建：

```bash
conda create -n python2 python=2.7
source activate python2
```

参考链接：[https://conda.io/docs/user-guide/tasks/manage-environments.html](https://conda.io/docs/user-guide/tasks/manage-environments.html)

#### 把 Conda 的 Python 环境添加到 jupyter 里

当你希望在 jupyter 里面使用你的虚拟环境的时候，你需要执行下面的命令：

```python
conda activate python2
conda install ipykernel
python -m ipykernel install --user --name python2 --display-name "Python 2"
```

其中的 python2 是你的虚拟环境的名字，display-name 可以取一个好听的名字，它会在 jupyter notebook 切换 kernel 的地方显示。

参考链接：[https://ipython.readthedocs.io/en/stable/install/kernel\_install.html](https://ipython.readthedocs.io/en/stable/install/kernel_install.html)

### Python 库

下面就是我安装的几个比较重要的 Python 库：

* jupyter
* `jupyter_contrib_nbextensions`
* numpy
* pandas
* sklearn
* matplotlib
* opencv-python
* pillow
* tqdm
* tensorflow-gpu
* keras
* pytorch
* graphviz
* pydot

