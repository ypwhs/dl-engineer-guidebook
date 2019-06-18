# Ubuntu 环境

## Oh My Zsh

{% embed url="https://ohmyz.sh" caption="Oh My Zsh" %}

在 Ubuntu 下安装 oh my zsh 直接执行下面的命令即可：

```bash
sudo apt install -y git zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

## CUDA

{% embed url="https://developer.nvidia.com/cuda-downloads" caption="CUDA 10.1" %}

CUDA 是英伟达显卡进行各种高性能运算必备的库，不同软件包依赖的 CUDA 版本可能不同，请仔细阅读官方文档。

|  版本 | Windows 10 | Linux |
| :--- | :--- | :--- |
| [CUDA 10.1](https://developer.nvidia.com/cuda-downloads) | [cuda\_10.1.168\_425.25\_win10.exe](https://developer.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda_10.1.168_425.25_win10.exe) | [cuda\_10.1.168\_418.67\_linux.run](https://developer.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda_10.1.168_418.67_linux.run) |
| [CUDA 10.0](https://developer.nvidia.com/cuda-10.0-download-archive) | [cuda\_10.0.130\_411.31\_win10.exe](https://developer.nvidia.com/compute/cuda/10.0/Prod/local_installers/cuda_10.0.130_411.31_win10) | [cuda\_10.0.130\_410.48\_linux.run](https://developer.nvidia.com/compute/cuda/10.0/Prod/local_installers/cuda_10.0.130_410.48_linux) |
| [CUDA 9.0](https://developer.nvidia.com/cuda-90-download-archive) | [cuda\_9.0.176\_win10.exe](https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda_9.0.176_win10-exe) | [cuda\_9.0.176\_384.81\_linux.run](https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda_9.0.176_384.81_linux-run) |

## **cuDNN**

{% embed url="https://developer.nvidia.com/cudnn" caption="cuDNN" %}

最新版 cuDNN 下载需要注册，旧版 cuDNN 无需注册，地址如下：

{% embed url="https://developer.nvidia.com/rdp/cudnn-archive" caption="cuDNN Archive" %}

cuDNN 是英伟达推出的专门用于深度学习加速计算的库，一般来说比使用纯 CUDA 速度要快不少。比如Keras 里有普通的 [LSTM](https://keras.io/layers/recurrent/#lstm) 以及 [CuDNNLSTM](https://keras.io/layers/recurrent/#cudnnlstm)，速度相差最高有十倍。

如果没有设计特殊的结构，cuDNN 应该是你的首选。

## TensorFlow

{% embed url="https://www.tensorflow.org/install/gpu" %}

最新版的 TensorFlow 使用的是 CUDA 10.0 和 cuDNN 7.4.1，NVIDIA 驱动需要 410.x 或更高版本。

建议按照官方文档中的 apt 方法安装 CUDA。

## PyTorch

PyTorch 自带 CUDA 和 cuDNN，只需要安装驱动即可运行。

目前 [PyPI](https://pypi.org/) 安装的 PyTorch 使用的是 CUDA9.0，如果你需要其他版本，请使用官网上的选择器找到你需要的版本，比如 Python 3.6 安装 CUDA10 的 PyTorch 需要使用下面的命令：

```bash
pip3 install https://download.pytorch.org/whl/cu100/torch-1.1.0-cp36-cp36m-linux_x86_64.whl
pip3 install https://download.pytorch.org/whl/cu100/torchvision-0.3.0-cp36-cp36m-linux_x86_64.whl
```

