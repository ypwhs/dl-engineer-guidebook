# 选 Windows、Linux 还是 macOS？

这三个系统都是有必要的，我在工作中大部分情况下都会使用 macOS 作为终端，仅仅在使用 office 软件、百度云的时候会用到 Windows。虽然我直接使用的机器是 macOS 的操作系统，但是实际上跑程序的机器是 Ubuntu（Linux）操作系统。

## macOS

使用 macOS 的原因有很多，下面我们逐一分析。

从硬件上来说：

* 好看，苹果的工业设计是非常棒的
* 流畅，触控板的滚动和缩放效果舒适
* 屏幕好，颜色的还原以及亮度和色温的控制都很恰当，60帧的屏幕很舒服
* 笔记本续航时间长
* iMac 5K 屏很大，可以显示很多终端

从软件上来说：

* 好看，从系统 UI 上来说，苹果的审美是有保障的，甚至在 macOS 上开发的软件都会注重审美
* 环境与 Linux 接近，终端命令基本是通用的，在使用上无缝切换
* 更安全，全盘加密，不用担心被偷以后被窃取文件，并且由于占有率低，少有为 macOS 开发的病毒软件
* 与其他苹果设备合作很紧密，比如桌面的文件可以在每台设备上同步，甚至可以直接在 iPhone 上查看

## Windows

这个操作系统通常是大家最为熟悉的操作系统，所以这里就不再介绍它的优点，这里只提几个缺点：

* 深度学习框架的官方支持不够及时，tensorflow 于 2015年11月发布，但是首次支持 Windows 间隔了一年：[TensorFlow now builds and runs on Microsoft Windows](https://github.com/tensorflow/tensorflow/releases/tag/0.12.0-rc0)
* 其他学者开发的新模型的代码通常需要进行修改才能在 Windows 上运行，如果他们的代码涉及 CUDA 编程，这种修改会很困难
* 路径的斜杠与其他操作系统不同，Windows 使用的是 `\`，容易作为转义字符解析成其他字符导致 bug
* 换行符与其他操作系统不同，Windows 使用的不是 `\n`，而是 `\r\n`
* 命令行与其他操作系统不同，许多命令功能一样，但是名字不同，比如 ifconfig 与 ipconfig，rm 与 del 等

为了能够使用大多数深度学习工程师开源的代码，我们建议使用 Ubuntu 作为跑代码的机器。

## Ubuntu

不管是做深度学习还是做其他的 Linux 学习，Ubuntu 都应该是首选的操作系统，原因如下：

* 易用性强
* 使用人数多，教程多，生态好
* 各个深度学习框架的官方支持，比如 [TensorFlow GPU](https://www.tensorflow.org/install/gpu) 只介绍了在 Ubuntu 下的安装方法



