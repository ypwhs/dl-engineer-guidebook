---
description: >-
  对于深度学习工程师来说，Python 是必不可少的工具，因为大多数深度学习框架都支持 Python（比如 tensorflow、pytorch、mxnet
  等）。在模型开发阶段，使用 Python 非常方便，如果配合 jupyter 使用，还可以进一步提升开发效率。
---

# Python 环境

## Anaconda

{% embed url="https://www.anaconda.com/" %}

Anaconda 是一个 Pyhton 的包管理器，它可以简化 Python 环境的安装。由于 Ubuntu 系统、macOS 系统的局限性，我们尽量不要在系统自带的环境里安装深度学习库，不然可能会出现一些不可预料的问题。

Anaconda 不需要 root 权限，所以可以很方便地安装在用户目录下，只要配置好环境变量即可使用，当你不需要它的时候，只需要直接删除它的目录，然后将对应的环境变量一起删除即可。

还有一个好处就是，你可以直接 scp 整个环境文件夹到其他相同硬件的机器上，它们的环境可以保持绝对的统一，可以极大简化运维的工作。

### 安装 Anaconda

Anaconda 官方下载页面：[https://www.anaconda.com/downloads](https://www.anaconda.com/downloads)

你只需要下载对应系统的安装包，然后直接运行安装包即可。比如在 macOS 上安装 Anaconda：

```bash
wget https://repo.anaconda.com/archive/Anaconda3-2019.03-MacOSX-x86_64.sh
bash Anaconda3-2019.03-MacOSX-x86_64.sh
```

**提示：**需要使用 brew 安装 wget 命令。

当然，macOS 上还可以[使用 brew cask 安装](macos-environment.md#kai-fa-ruan-jian)。

### 配置环境变量

安装好以后，有可能需要手动[配置环境变量](linux-command.md#export)，比如我安装在 `/usr/local/anaconda3` 目录下，所以我在 `~/.zshrc` 里添加里下面这句：

```bash
export PATH="/usr/local/anaconda3/bin:$PATH"
```

### 使用 Anaconda 创建其他 Python 环境

如果我们需要其他 Python 环境，可以使用 conda 创建：

```bash
conda create -n python2 python=2.7
source activate python2
```

参考链接：[https://conda.io/docs/user-guide/tasks/manage-environments.html](https://conda.io/docs/user-guide/tasks/manage-environments.html)

### 把 Conda 的 Python 环境添加到 jupyter 里

当你希望在 jupyter 里使用你的虚拟环境的时候，你需要执行下面的命令：

```python
conda activate python2
conda install ipykernel
python -m ipykernel install --user --name python2 --display-name "Python 2"
```

其中的 python2 是你的虚拟环境的名字，display-name 可以取一个好听的名字，它会在 jupyter notebook 切换 kernel 的地方显示。

参考链接：[https://ipython.readthedocs.io/en/stable/install/kernel\_install.html](https://ipython.readthedocs.io/en/stable/install/kernel_install.html)

### 切换 pip 源

如果你使用 pip 安装的时候网速较慢，可以使用[清华大学的镜像](https://mirror.tuna.tsinghua.edu.cn/help/pypi/)：

```bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

## Python 库

下面是我认为比较重要的 Python 库：

* jupyter
* `jupyter_contrib_nbextensions`
* numpy
* pandas
* sklearn
* matplotlib
* opencv-python
* pillow
* tqdm
* torch
* torchvision
* tensorflow-gpu
* keras
* tensorboard
* tensorboardx

### jupyter

{% embed url="https://jupyter.org/" %}

在实验阶段，强烈建议你使用 jupyter notebook 编写实验代码，因为它与写 Python 脚本的逻辑完全不同。

官方介绍：

> Jupyter Notebook是一个开源Web应用程序，允许您创建和共享包含实时代码，公式，可视化和叙述文本的文档。用途包括：数据清理和转换，数值模拟，统计建模，数据可视化，机器学习等。

特点：

* web页面交互，在各个平台甚至是手机上都有同样的界面
* 运行过的代码产生的变量、函数、类不会消失，除非你重启内核
* 不仅支持写代码，显示函数输出的文字，还支持显示图片，甚至实现简单的交互功能
* 支持 Markdown 编写注释，还支持 latex 公式

### jupyter\_contrib\_nbextensions

{% embed url="https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html" %}

Jupyter Notebook 插件。

> 该`jupyter_contrib_nbextensions`软件包包含一系列社区贡献的非官方扩展，可为Jupyter笔记本添加功能。这些扩展大多是用Javascript编写的，将在您的浏览器中本地加载。

我使用了[代码执行时间插件](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/execute_time/readme.html)和[函数折叠插件](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/codefolding/readme.html)。

### numpy

{% embed url="https://www.numpy.org/" %}



科学计算必备库。

> NumPy是Python语言的一个扩展程序库。支持高端大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。

### pandas

{% embed url="https://pandas.pydata.org/" %}

操作 csv 非常方便，python 里的 excel。

> _pandas_是一个开源的，BSD许可的库，为Python编程语言提供高性能，易于使用的数据结构和数据分析工具。

### sklearn

{% embed url="https://scikit-learn.org/" %}

机器学习模型大全。

> Python中的机器学习
>
> * 简单有效的数据挖掘和数据分析工具
> * 可供所有人访问，并可在各种环境中重复使用
> * 基于NumPy，SciPy和matplotlib构建
> * 开源，商业上可用 - BSD许可证

### matplotlib

{% embed url="https://matplotlib.org/" %}

画图工具。

> Matplotlib是一个Python 2D绘图库，可以生成各种硬拷贝格式和跨平台的交互式环境的出版物质量数据。Matplotlib可用于Python脚本、IPython shell、Jupyter Notebook 和 Web应用程序服务器和四个图形用户界面工具包。

### opencv-python

{% embed url="https://opencv.org/" %}

OpenCV 的 Python 库，图像处理必备。

> OpenCV的全称是Open Source Computer Vision Library，是一个跨平台的计算机视觉库。

### pillow

{% embed url="https://pillow.readthedocs.io/en/stable/" %}

PIL，另一个图像处理库，PyTorch 里的 torchvision 有很多写好的数据增强类，它们的输入类型是 PIL.Image。

> 该库提供广泛的文件格式支持，高效的内部表示和相当强大的图像处理功能。
>
> 核心图像库旨在快速访问以几种基本像素格式存储的数据。它应该为一般的图像处理工具提供坚实的基础。

### tqdm

{% embed url="https://github.com/tqdm/tqdm" %}

进度条库，耗时长的任务可以使用 tqdm 直观地展示任务的进度，避免焦虑。

> `tqdm`在阿拉伯语中是“进步”（_taqadum_，تقدم）的意思，在西班牙语中是“我太爱你了”（_te quiero demasiado_）的缩写。
>
> 只需在任何迭代器外包一个 tqdm：`tqdm(iterable)`，就能立刻让你的循环显示一个聪明的进度条！

![tqdm](https://raw.githubusercontent.com/tqdm/tqdm/master/images/tqdm.gif)

### torch

{% embed url="https://pytorch.org/" %}

深度学习库，推荐使用。

> 一个开源深度学习平台，提供从研究原型到生产部署的无缝路径。

### torchvision

{% embed url="https://pytorch.org/docs/stable/torchvision/index.html" %}

和 PyTorch 配套使用。

> [`torchvision`](https://pytorch.org/docs/stable/torchvision/index.html#module-torchvision)包含了流行的数据集，预训练模型和计算机视觉的常见的图像变换。

### tensorflow

{% embed url="https://www.tensorflow.org/" %}

深度学习库，大而全。配备显卡的机器请按照 [Ubuntu 环境](ubuntu-environment.md) 进行配置。

> TensorFlow是一个用于机器学习的端到端开源平台。 它拥有全面、灵活的工具、库和社区资源生态系统，可让研究人员推动ML的最新技术，开发人员可轻松构建和部署ML驱动的应用程序。

### keras

{% embed url="https://keras.io/" %}

更高级的 API，和 tensorflow 联合使用很方便。最新的 TensorFlow 2.0 非常推荐使用 Keras 作为模型搭建的高级 API，你不必直接安装 Keras，直接使用 tf.keras 即可。

> Keras是一个高级神经网络API，用Python编写，能够在TensorFlow，CNTK或Theano之上运行。它的开发重点是实现快速实验。能够以最小的延迟从理念到结果是进行良好研究的关键。

绘制模型结构需要 graphviz 和 pydot。 

### tensorboard

{% embed url="https://www.tensorflow.org/tensorboard" %}

TensorBoard 是一个可视化工具，你可以使用它可视化：

* loss、acc 曲线
* 模型结构
* 权重分布
* 生成的图像
* 生成的文字

### tensorboardx

{% embed url="https://github.com/lanpa/tensorboardX" %}

tensorboardx 是一个框架无关的 tensorboard writer，支持 numpy 矩阵、pytorch 的 tensor 等格式。

目前 pytorch 1.1 也有[官方支持](https://pytorch.org/docs/stable/tensorboard.html)，但是功能有限，所以目前我仍然在使用 tensorboardx。





