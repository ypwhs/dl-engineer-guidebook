---
description: >-
  这篇文章主要介绍的是家用的深度学习工作站，典型的配置有两种，分别是一个 GPU 的机器和 四个 GPU的机器。如果需要更多的 GPU 可以考虑配置两台四个
  GPU 的机器。如果希望一台机器同时具备 6~8 个 GPU 需要联系专门的供应商进行配置，并且有专业的机房存放，放在家里噪声很大并且容易跳闸。
---

# 如何配置一台深度学习工作站

## CPU

由于最近 AMD 和 Intel 频繁更新 CPU，因此大家选择新款的 CPU 比较好。

CPU 瓶颈没有那么大，一般以一个 GPU 对应四个 CPU 核比较好，比如单卡机器买四核 CPU，四卡机器买 16核 CPU。

除了核数，你还需要注意 PCIE 支持情况，一般显卡是 PCI-E 3.0 x16，比如 [i9-9900K](https://www.intel.cn/content/www/cn/zh/products/processors/core/i9-processors/i9-9900k.html) 支持 1x16, 2x8, 1x8+2x4 的配置，也就是说配置四卡的话，有一张卡是全速的，其他卡是半速的，可以插两个 NVMe 固态硬盘。

AMD 的 [2990WX](https://www.amd.com/zh-hans/products/cpu/amd-ryzen-threadripper-2990wx) 支持 64 条 PCI-E 通道，如果不插 NVMe 固态硬盘，可以支持四卡全速。

## 主板

主板需要注意：

* CPU 接口是否能对上
* 显卡是否能插上
* PCI-E 同时可以支持几张卡以什么样的速度运行

## 硬盘

常用硬盘接口有三种：

* SATA3.0，速度 600MB/s
* SAS，速度 1200MB/s
* PCIE 3.0 x4（NVMe\)，速度 3.94GB/s

下面是根据代表产品查询的参数：

| 类型 | 价格\(元/TB\) | 读取速度\(MB/s\) | 写入速度\(MB/s\) | 4K随机读取\(IOPS\) | 4K随机写入\(IOPS\) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| SATA3 机械硬盘 | 200 | 100 | 100 | 100 | 100 |
| SATA3 固态硬盘 | 800 | 550 | 520 | 98000 | 90000 |
| NVMe 固态硬盘 | 1000 | 3230 | 1625 | 340000 | 275000 |

注：

* 4K 随机读写的队列深度为 32
* SATA3 机械硬盘没有太好的数据来源，所以数据是经验值
* SATA3 固态硬盘型号为 [三星（SAMSUNG）1TB SSD固态硬盘 SATA3.0接口 860 EVO](https://item.jd.com/6301071.html)
* NVMe 固态硬盘型号为 [英特尔（Intel）1TB SSD固态硬盘 M.2接口\(NVMe协议\) 760P系](https://item.jd.com/7591647.html)

在面对大量小文件的时候，使用 NVMe 硬盘可以一分钟扫完 1000万文件，如果使用普通硬盘，那么就需要一天时间。为了节省生命，简化代码，硬盘建议选择 NVMe 协议的固态硬盘。

如果你的主板不够新，没有NVMe 插槽，你可以使用 M.2 转接卡将 M.2 接口转为 PCI-E 接口。

## 内存

内存随便买，容量大于显存比较好，比如单卡配 16GB 内存，四卡配 64GB 内存。

## 显卡

首先上显卡性能表：

| 型号 | 架构 | 价格\(元\) | 显存\(GB\) | CUDA核 | Tensor核 | FP32\(TFLOPS\) | FP16 | INT8 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| GTX 1080Ti | Pascal | 5299 | 11 | 3584 | NA | 11.3 | NA | NA |
| RTX 2080 | Turing | 5099 | 8 | 2944 | 368 | 10 | 40.3 | 161.1 |
| RTX 2080Ti | Turing | 8599 | 11 | 4532 | 544 | 13.4 | 53.8 | 215.2 |
| TITAN RTX | Turing | 16499 | 24 | 4608 | 576 | 16.3 | 130 |  |
| Tesla V100 | Volta | 79600 | 32 | 5120 | 640 | 15.7 | 125 | NA |

参考链接：

* [Turing 架构白皮书](https://www.nvidia.com/content/dam/en-zz/Solutions/design-visualization/technologies/turing-architecture/NVIDIA-Turing-Architecture-Whitepaper.pdf)
* [Volta 架构白皮书](https://images.nvidia.com/content/volta-architecture/pdf/volta-architecture-whitepaper.pdf)
* [RTX 2080 Ti Deep Learning Benchmarks with TensorFlow - 2019](https://lambdalabs.com/blog/2080-ti-deep-learning-benchmarks/)

## 电源

先计算功率总和，如单卡 CPU 100W，显卡 250W，加上其他的大概 400W，那么就买 550W 的电源。

双卡最好买 1000W 的电源，四卡最好买 1600W 的电源，我这里实测过 1500W 的电源，跑起来所有的卡以后会因为电源不足而自动关机。

一般墙上的插座只支持 220V 10A，也就是 2200W 的交流电，由于电源要把交流电转直流电，所以会有一些损耗，最高只有 1600W，因此如果想要支持八卡，最好不要在家尝试。八卡一般是双电源，并且需要使用专用的PDU插座，并且使用的是 16A 插口。

## 网卡

一般主板自带千兆网卡。

## 机箱

如果配单卡，可以直接买个普通机箱，注意显卡长度能放下就行。

如果配四卡机器，建议买一个 [Air 540](https://item.jd.com/1024817.html) 机箱，因为我正在用这一款。

## 显示器

深度学习工作站装好系统以后就不需要显示器了，随便接一个显示器就行。

## 键盘鼠标

深度学习工作站装好系统以后就不需要键盘鼠标了，随便接一个键盘鼠标就行。

