# Ubuntu 环境

## CUDA

* [https://developer.nvidia.com/cuda-downloads](https://developer.nvidia.com/cuda-downloads)
* [https://developer.nvidia.com/cuda-10.0-download-archive](https://developer.nvidia.com/cuda-10.0-download-archive)
* [https://developer.nvidia.com/cuda-toolkit-archive](https://developer.nvidia.com/cuda-toolkit-archive)

CUDA 是英伟达显卡进行各种高性能运算必备的库，不同软件包依赖的 CUDA 版本可能不同，请仔细阅读你所使用的深度学习框架的官方文档。

|  版本 | Windows 10 | Linux |
| :--- | :--- | :--- |
| [CUDA 10.1](https://developer.nvidia.com/cuda-downloads) | [cuda\_10.1.168\_425.25\_win10.exe](https://developer.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda_10.1.168_425.25_win10.exe) | [cuda\_10.1.168\_418.67\_linux.run](https://developer.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda_10.1.168_418.67_linux.run) |
| [CUDA 10.0](https://developer.nvidia.com/cuda-10.0-download-archive) | [cuda\_10.0.130\_411.31\_win10.exe](https://developer.nvidia.com/compute/cuda/10.0/Prod/local_installers/cuda_10.0.130_411.31_win10) | [cuda\_10.0.130\_410.48\_linux.run](https://developer.nvidia.com/compute/cuda/10.0/Prod/local_installers/cuda_10.0.130_410.48_linux) |
| [CUDA 9.2](https://developer.nvidia.com/cuda-92-download-archive) | [cuda\_9.2.148\_win10.exe](https://developer.nvidia.com/compute/cuda/9.2/Prod2/local_installers2/cuda_9.2.148_win10) | [cuda\_9.2.148\_396.37\_linux.run](https://developer.nvidia.com/compute/cuda/9.2/Prod2/local_installers/cuda_9.2.148_396.37_linux) |
| [CUDA 9.1](https://developer.nvidia.com/cuda-91-download-archive) | [cuda\_9.1.85\_win10.exe](https://developer.nvidia.com/compute/cuda/9.1/Prod/local_installers/cuda_9.1.85_win10) | [cuda\_9.1.85\_387.26\_linux.run](https://developer.nvidia.com/compute/cuda/9.1/Prod/local_installers/cuda_9.1.85_387.26_linux) |
| [CUDA 9.0](https://developer.nvidia.com/cuda-90-download-archive) | [cuda\_9.0.176\_win10.exe](https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda_9.0.176_win10-exe) | [cuda\_9.0.176\_384.81\_linux.run](https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda_9.0.176_384.81_linux-run) |
|  | 以下版本较低，推荐使用上面的版本。 |  |
| [CUDA 8.0 GA2](https://developer.nvidia.com/cuda-80-ga2-download-archive) | [cuda\_8.0.61\_win10.exe](https://developer.nvidia.com/compute/cuda/8.0/Prod2/local_installers/cuda_8.0.61_win10-exe) | [cuda\_8.0.61\_375.26\_linux.run](https://developer.nvidia.com/compute/cuda/8.0/Prod2/local_installers/cuda_8.0.61_375.26_linux-run) |
| [CUDA 8.0 GA1](https://developer.nvidia.com/cuda-80-download-archive) | [cuda\_8.0.44\_win10.exe](https://developer.nvidia.com/compute/cuda/8.0/prod/local_installers/cuda_8.0.44_win10-exe) | [cuda\_8.0.44\_linux.run](https://developer.nvidia.com/compute/cuda/8.0/prod/local_installers/cuda_8.0.44_linux-run) |
| [CUDA 7.5](https://developer.nvidia.com/cuda-75-downloads-archive) | [cuda\_7.5.18\_win10.exe](http://developer.download.nvidia.com/compute/cuda/7.5/Prod/local_installers/cuda_7.5.18_win10.exe) | [cuda\_7.5.18\_linux.run](http://developer.download.nvidia.com/compute/cuda/7.5/Prod/local_installers/cuda_7.5.18_linux.run) |
| [CUDA 7.0](https://developer.nvidia.com/cuda-toolkit-70) | [cuda\_7.0.28\_windows.exe](http://developer.download.nvidia.com/compute/cuda/7_0/Prod/local_installers/cuda_7.0.28_windows.exe) | [cuda\_7.0.28\_linux.run](http://developer.download.nvidia.com/compute/cuda/7_0/Prod/local_installers/cuda_7.0.28_linux.run) |
| [CUDA 6.5](https://developer.nvidia.com/cuda-toolkit-65) | [cuda\_6.5.14\_windows\_general\_64.exe](http://developer.download.nvidia.com/compute/cuda/6_5/rel/installers/cuda_6.5.14_windows_general_64.exe) | [cuda\_6.5.14\_linux\_64.run](http://developer.download.nvidia.com/compute/cuda/6_5/rel/installers/cuda_6.5.14_linux_64.run) |

## **cuDNN**

cuDNN 下载需要注册，地址如下：

* [https://developer.nvidia.com/cudnn](https://developer.nvidia.com/cudnn)
* [https://developer.nvidia.com/rdp/cudnn-archive](https://developer.nvidia.com/rdp/cudnn-archive)

cuDNN 是英伟达推出的专门用于深度学习加速计算的库，一般来说比使用纯 CUDA 速度要快不少。比如Keras 里有普通的 [LSTM](https://keras.io/layers/recurrent/#lstm) 以及 [CuDNNLSTM](https://keras.io/layers/recurrent/#cudnnlstm)，速度相差最高有十倍。如果没有设计特殊的结构，cuDNN 应该是你的首选。

| cuDNN | CUDA9.0 | CUDA9.2 | CUDA10.0 | CUDA10.1 |
| :--- | :--- | :--- | :--- | :--- |
| 7.6.1 | [cudnn-9.0-linux-x64-v7.6.1.34.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.1/cudnn-9.0-linux-x64-v7.6.1.34.tgz) \(392.82MB\) | [cudnn-9.2-linux-x64-v7.6.1.34.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.1/cudnn-9.2-linux-x64-v7.6.1.34.tgz) \(396.89MB\) | [cudnn-10.0-linux-x64-v7.6.1.34.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.1/cudnn-10.0-linux-x64-v7.6.1.34.tgz) \(460.88MB\) | [cudnn-10.1-linux-x64-v7.6.1.34.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.1/cudnn-10.1-linux-x64-v7.6.1.34.tgz) \(497.63MB\) |
| 7.6.0 | [cudnn-9.0-linux-x64-v7.6.0.64.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.0/cudnn-9.0-linux-x64-v7.6.0.64.tgz) \(374.59MB\) | [cudnn-9.2-linux-x64-v7.6.0.64.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.0/cudnn-9.2-linux-x64-v7.6.0.64.tgz) \(378.84MB\) | [cudnn-10.0-linux-x64-v7.6.0.64.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.0/cudnn-10.0-linux-x64-v7.6.0.64.tgz) \(440.90MB\) | [cudnn-10.1-linux-x64-v7.6.0.64.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.0/cudnn-10.1-linux-x64-v7.6.0.64.tgz) \(477.61MB\) |
| 7.5.1 | [cudnn-9.0-linux-x64-v7.5.1.10.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.5.1/cudnn-9.0-linux-x64-v7.5.1.10.tgz) \(357.13MB\) | [cudnn-9.2-linux-x64-v7.5.1.10.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.5.1/cudnn-9.2-linux-x64-v7.5.1.10.tgz) \(361.63MB\) | [cudnn-10.0-linux-x64-v7.5.1.10.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.5.1/cudnn-10.0-linux-x64-v7.5.1.10.tgz) \(412.76MB\) | [cudnn-10.1-linux-x64-v7.5.1.10.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.5.1/cudnn-10.1-linux-x64-v7.5.1.10.tgz) \(449.47MB\) |
| 7.5.0 | [cudnn-9.0-linux-x64-v7.5.0.56.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.5.0/cudnn-9.0-linux-x64-v7.5.0.56.tgz) \(357.11MB\) | [cudnn-9.2-linux-x64-v7.5.0.56.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.5.0/cudnn-9.2-linux-x64-v7.5.0.56.tgz) \(361.61MB\) | [cudnn-10.0-linux-x64-v7.5.0.56.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.5.0/cudnn-10.0-linux-x64-v7.5.0.56.tgz) \(412.76MB\) | [cudnn-10.1-linux-x64-v7.5.0.56.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.5.0/cudnn-10.1-linux-x64-v7.5.0.56.tgz) \(449.46MB\) |
| 7.4.2 | [cudnn-9.0-linux-x64-v7.4.2.24.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.4.2/cudnn-9.0-linux-x64-v7.4.2.24.tgz) \(349.00MB\) | [cudnn-9.2-linux-x64-v7.4.2.24.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.4.2/cudnn-9.2-linux-x64-v7.4.2.24.tgz) \(353.84MB\) | [cudnn-10.0-linux-x64-v7.4.2.24.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.4.2/cudnn-10.0-linux-x64-v7.4.2.24.tgz) \(404.82MB\) | - |
| 7.4.1 | [cudnn-9.0-linux-x64-v7.4.1.5.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.4.1/cudnn-9.0-linux-x64-v7.4.1.5.tgz) \(347.17MB\) | [cudnn-9.2-linux-x64-v7.4.1.5.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.4.1/cudnn-9.2-linux-x64-v7.4.1.5.tgz) \(352.02MB\) | [cudnn-10.0-linux-x64-v7.4.1.5.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.4.1/cudnn-10.0-linux-x64-v7.4.1.5.tgz) \(403.12MB\) | - |
| 7.3.1 | [cudnn-9.0-linux-x64-v7.3.1.20.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.3.1/cudnn-9.0-linux-x64-v7.3.1.20.tgz) \(344.85MB\) | [cudnn-9.2-linux-x64-v7.3.1.20.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.3.1/cudnn-9.2-linux-x64-v7.3.1.20.tgz) \(351.05MB\) | [cudnn-10.0-linux-x64-v7.3.1.20.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.3.1/cudnn-10.0-linux-x64-v7.3.1.20.tgz) \(400.58MB\) | - |
| 7.3.0 | [cudnn-9.0-linux-x64-v7.3.0.29.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.3.0/cudnn-9.0-linux-x64-v7.3.0.29.tgz) \(340.43MB\) | - | [cudnn-10.0-linux-x64-v7.3.0.29.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.3.0/cudnn-10.0-linux-x64-v7.3.0.29.tgz) \(396.06MB\) | - |
| 7.2.1 | [cudnn-9.0-linux-x64-v7.2.1.38.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.2.1/cudnn-9.0-linux-x64-v7.2.1.38.tgz) \(331.19MB\) | [cudnn-9.2-linux-x64-v7.2.1.38.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.2.1/cudnn-9.2-linux-x64-v7.2.1.38.tgz) \(337.08MB\) | - | - |
| 7.1.4 | [cudnn-9.0-linux-x64-v7.1.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.1.4/cudnn-9.0-linux-x64-v7.1.tgz) \(390.26MB\) | [cudnn-9.2-linux-x64-v7.1.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.1.4/cudnn-9.2-linux-x64-v7.1.tgz) \(401.58MB\) | - | - |

以下版本较低，推荐使用上面的版本。

| cuDNN | CUDA6.5 | CUDA7.0 | CUDA7.5 | CUDA8.0 | CUDA9.0 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 7.2.1 | - | - | - | [cudnn-8.0-linux-x64-v7.2.1.38.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.2.1/cudnn-8.0-linux-x64-v7.2.1.38.tgz) \(189.78MB\) | [cudnn-9.0-linux-x64-v7.2.1.38.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.2.1/cudnn-9.0-linux-x64-v7.2.1.38.tgz) \(331.19MB\) |
| 7.1.4 | - | - | - | - | [cudnn-9.0-linux-x64-v7.1.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.1.4/cudnn-9.0-linux-x64-v7.1.tgz) \(390.26MB\) |
| 7.1.3 | - | - | - | [cudnn-8.0-linux-x64-v7.1.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.1.3/cudnn-8.0-linux-x64-v7.1.tgz) \(245.96MB\) | [cudnn-9.0-linux-x64-v7.1.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.1.3/cudnn-9.0-linux-x64-v7.1.tgz) \(387.77MB\) |
| 7.1.2 | - | - | - | [cudnn-8.0-linux-x64-v7.1.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.1.2/cudnn-8.0-linux-x64-v7.1.tgz) \(246.13MB\) | [cudnn-9.0-linux-x64-v7.1.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.1.2/cudnn-9.0-linux-x64-v7.1.tgz) \(387.42MB\) |
| 7.0.5 | - | - | - | [cudnn-8.0-linux-x64-v7.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.0.5/cudnn-8.0-linux-x64-v7.tgz) \(267.98MB\) | [cudnn-9.0-linux-x64-v7.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.0.5/cudnn-9.0-linux-x64-v7.tgz) \(332.66MB\) |
| 7.0.4 | - | - | - | [cudnn-8.0-linux-x64-v7.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.0.4/cudnn-8.0-linux-x64-v7.tgz) \(267.98MB\) | [cudnn-9.0-linux-x64-v7.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.0.4/cudnn-9.0-linux-x64-v7.tgz) \(332.67MB\) |
| 6.0 | - | - | [cudnn-7.5-linux-x64-v6.0.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v6.0/cudnn-7.5-linux-x64-v6.0.tgz) \(109.43MB\) | [cudnn-8.0-linux-x64-v6.0.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v6.0/cudnn-8.0-linux-x64-v6.0.tgz) \(191.82MB\) | - |
| 5.1 | - | - | [cudnn-7.5-linux-x64-v5.1.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v5.1/cudnn-7.5-linux-x64-v5.1.tgz) \(77.18MB\) | [cudnn-8.0-linux-x64-v5.1.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v5.1/cudnn-8.0-linux-x64-v5.1.tgz) \(98.39MB\) | - |
| 5 | - | - | [cudnn-7.5-linux-x64-v5.0-ga.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v5/cudnn-7.5-linux-x64-v5.0-ga.tgz) \(75.66MB\) | [cudnn-8.0-linux-x64-v5.0-ga.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v5/cudnn-8.0-linux-x64-v5.0-ga.tgz) \(94.58MB\) | - |
| 4 | - | [cudnn-7.0-linux-x64-v4.0-prod.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v4/cudnn-7.0-linux-x64-v4.0-prod.tgz) \(81.73MB\) | - | - | - |
| 3 | - | [cudnn-7.0-linux-x64-v3.0-prod.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v3/cudnn-7.0-linux-x64-v3.0-prod.tgz) \(63.81MB\) | - | - | - |
| 2 | [cudnn-6.5-linux-x64-v2.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v2/cudnn-6.5-linux-x64-v2.tgz) \(15.18MB\) | - | - | - | - |

## [TensorRT](https://developer.nvidia.com/tensorrt)

TensorRT 是英伟达推出的推断库（Inference），通常用于模型部署。

使用 TensorRT 可以进行半精度推断，甚至对模型进行 int8 量化，从而得到数倍的性能提升，并且尽可能保证精度。由于此项目还在开发阶段，不同的版本可能不通用，请参考你所使用的深度学习框架的文档，找到你所需要安装的 TensorRT 版本。

## TensorFlow

* [https://www.tensorflow.org](https://www.tensorflow.org)
* [https://www.tensorflow.org/install/gpu](https://www.tensorflow.org/install/gpu)

最新版的 TensorFlow 使用的是 CUDA 10.0 和 cuDNN 7.4.1，NVIDIA 驱动需要 410.x 或更高版本。

建议按照官方文档中的 apt 方法安装 CUDA。

### 历史版本依赖环境

| **TensorFlow** | **CUDA** | **cuDNN** | **NVIDIA Driver** | **NCCL** | **TensorRT** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1.14 | 10.0 | 7.4.1 | 410 | 2.2 | 5.0 |
| [1.13](https://github.com/tensorflow/docs/blob/r1.13/site/en/install/gpu.md#software-requirements) | 10.0 | 7.4.1 | 410 | 2.2 | 5.0 |
| [1.12](https://github.com/tensorflow/docs/blob/r1.12/site/en/install/gpu.md#software-requirements) | 9.0 | 7.2 | 384 | 2.2 | 4.0 |
| [1.11](https://github.com/tensorflow/docs/blob/r1.11/site/en/install/gpu.md#software-requirements) | 9.0 | 7.2 | 384 | 2.2 | 4.0 |
| [1.10](https://github.com/tensorflow/docs/blob/r1.10/site/en/install/install_linux.md#tensorflow-gpu-support) | 9.0 | 7.1 | 384 | 2.2 | 4.0 |
| [1.9](https://github.com/tensorflow/docs/blob/r1.9/site/en/install/install_linux.md#tensorflow-gpu-support) | 9.0 | 7.0 |  |  | 3.0 |
| [1.8](https://github.com/tensorflow/docs/blob/r1.8/site/en/install/install_linux.md#nvidia-requirements-to-run-tensorflow-with-gpu-support) | 9.0 | 7.0 |  |  | 3.0 |
| [1.7](https://github.com/tensorflow/docs/blob/r1.7/site/en/install/install_linux.md#nvidia-requirements-to-run-tensorflow-with-gpu-support) | 9.0 | 7.0 |  |  | 3.0 |
| [1.6](https://github.com/tensorflow/docs/blob/r1.6/site/en/install/install_linux.md#nvidia-requirements-to-run-tensorflow-with-gpu-support) | 9.0 | 7.0 |  |  |  |
| [1.5](https://github.com/tensorflow/docs/blob/r1.5/site/en/install/install_linux.md#nvidia-requirements-to-run-tensorflow-with-gpu-support) | 9.0 | 7.0 |  |  |  |
| [1.4](https://github.com/tensorflow/docs/blob/r1.4/site/en/install/install_linux.md#nvidia-requirements-to-run-tensorflow-with-gpu-support) | 8.0 | 6.0 |  |  |  |
| [1.3](https://github.com/tensorflow/docs/blob/r1.3/site/en/install/install_linux.md#nvidia-requirements-to-run-tensorflow-with-gpu-support) | 8.0 | 6.0 |  |  |  |
| [1.2](https://github.com/tensorflow/docs/blob/r1.2/site/en/install/install_linux.md#nvidia-requirements-to-run-tensorflow-with-gpu-support) | 8.0 | 5.1 |  |  |  |
| [1.1](https://github.com/tensorflow/docs/blob/r1.1/site/en/install/install_linux.md#nvidia-requirements-to-run-tensorflow-with-gpu-support) | 8.0 | 5.1 |  |  |  |
| [1.0](%20https://github.com/tensorflow/docs/blob/r1.0/site/en/install/install_linux.md#nvidia-requirements-to-run-tensorflow-with-gpu-support) | 8.0 | 5.1 |  |  |  |

提示：

* NVIDIA Driver 为空，官方文档说的是只要安装满足 CUDA 版本的驱动即可
* NCCL 和 TensorRT 为空，表示不需要安装

## [PyTorch](https://pytorch.org/)

PyTorch 自带 CUDA 和 cuDNN，只需要安装 NVIDIA 驱动即可运行。

目前 [PyPI](https://pypi.org/) 安装的 PyTorch 使用的是 CUDA9.0，如果你需要其他版本，请使用官网上的选择器找到你需要的版本，比如 Python 3.7 安装 CUDA10 的 PyTorch 需要使用下面的命令：

```bash
pip3 install https://download.pytorch.org/whl/cu100/torch-1.1.0-cp37-cp37m-linux_x86_64.whl
pip3 install https://download.pytorch.org/whl/cu100/torchvision-0.3.0-cp37-cp37m-linux_x86_64.whl
```

## 必备命令

```bash
sudo apt install git curl htop nload tmux screen aria2 graphviz aptitude tree
```

常见的 git、htop、nload 等命令在 [macOS 环境](macos-environment.md#bi-bei-ming-ling) 里已经介绍过了。其实大部分命令在没有安装的时候，如果你使用它们，会自动提示需要安装，所以不用担心没有安装全：

```bash
ypw@ypw-ubuntu:~$ screen

Command 'screen' not found, but can be installed with:

sudo apt install screen
```

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

tmux 最大的好处是可以让你的命令在后台运行，不会因为终端关闭而退出。比如在后台运行 jupyter、python 数据预处理脚本和训练脚本等。

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

![tmux](.gitbook/assets/image%20%2829%29.png)

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

### screen

screen 和 tmux 一样都是在后台运行命令的工具。

#### 新建窗口

```bash
screen -S jupyter
```

其中 -S 后面跟的是 screen 的名字。

#### 恢复窗口

```bash
screen -r jupyter
```

其中 -r 后面跟的是 screen 的名字。

#### 退出窗口

你可以在窗口中使用 exit 命令退出窗口，也可以使用下面的命令：

```bash
screen -X -S jupyter quit
```

其中 -S 后面跟的是 screen 的名字。

#### 在 screen 里支持滚轮

新建一个 `~/.screenrc` 文件，在里面添加一行 `termcapinfo xterm* ti@:te@` 并保存，重新连接 screen 就可以使用滚轮了。

#### 进入拷贝模式

输入快捷键 `Ctrl + a + [` 进入拷贝模式，然后你就可以使用方向键、翻页键进行翻页。

下面是拷贝模式下的常用快捷键：

```text
h -    Move the cursor left by one character
j -    Move the cursor down by one line
k -    Move the cursor up by one line
l -    Move the cursor right by one character
0 -    Move to the beginning of the current line
$ -    Move to the end of the current line.
G -    Moves to the specified line
       (defaults to the end of the buffer).
C-u -  Scrolls a half page up.
C-b -  Scrolls a full page up.
C-d -  Scrolls a half page down.
C-f -  Scrolls the full page down.
```

如果你记不得这么多快捷键，推荐 iTerm2 + tmux 的组合。

