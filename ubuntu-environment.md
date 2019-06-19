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

## 必备命令

`sudo apt install git htop nload curl tmux screen aria2 graphviz aptitude tree`

git、htop、nload 参考 macOS 环境里的介绍。

### curl

curl 是一个多功能的网络操作命令，你可以使用它来发送 GET、POST 请求。

在开发服务的时候，我们会经常使用这个命令来测试服务是否能返回预期的结果。

GET：

```bash
curl https://dl.ypw.io
```

POST：

```bash
curl -d "param1=value1&param2=value2" -X POST http://localhost:3000/data
```

POST json：

```bash
curl -d '{"key1":"value1", "key2":"value2"}' -H "Content-Type: application/json" -X POST http://localhost:3000/data
```

### tmux

tmux 是一个优秀的终端复用器命令，用户可以通过tmux 在一个终端内管理多个分离的会话，窗口及面板，对于同时使用多个命令行，或多个任务时非常方便。

#### 创建会话

比如你想同时监控 CPU、内存、显卡使用情况，那么你可以在使用 iTerm2 的情况下，执行下面的命令开启一个 tmux 会话\(session\)：

```bash
tmux -CC new -s monitor
```

其中的 monitor 是这个会话的名字，你可以修改为自己喜欢的名字。

#### 修改布局

在弹出的窗口\(window\)中，你可以：

* 使用 ⌘+D `Command + D` 横向分割这个窗口
* 使用 ⌘+⇧+D `Command + Shift + D` 纵向分割这个窗口
* 使用 ⌘+N `Command + N` 创建一个新的窗口

当你调整好布局以后，可以在每个窗格\(panel\)里运行你想运行的命令。

窗口大小可以使用鼠标进行调整，窗格大小也可以使用鼠标拖动修改。

修改好以后，我们可以得到类似下图的效果：

![tmux](.gitbook/assets/image%20%2811%29.png)

#### 脱离会话

如果你想让 python 脚本在后台运行，只需要在刚才创建会话的地方按一下 esc 键，就可以脱离这个会话。

```text
➜  ~ tmux -CC new -s monitor
** tmux mode started **

Command Menu
----------------------------
esc    Detach cleanly.
  X    Force-quit tmux mode.
  L    Toggle logging.
  C    Run tmux command.
```

你也可以直接关闭开启会话的终端的窗口，效果一样。

#### 恢复会话

恢复会话可以使用这个命令：`tmux -CC attach -t monitor`

#### 退出会话

如果你想完全退出所有的终端，只需要在每个窗格里 ⌘+W `Command + W` 即可，关闭最后一个窗口以后，这个会话就结束了。 

