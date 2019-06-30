# macOS 软件

下面是我安装的与工作有关的软件。

## 终端

### iTerm2

{% embed url="https://www.iterm2.com/" %}

终端首选 iTerm，最大的好处是可以结合 tmux 分屏使用，比如：

![iTerm2](.gitbook/assets/image%20%2844%29.png)

### 快捷键配置

开启 ⌘←, ⌘→ 和 ⌥←, ⌥→ 快捷键，可以直接跳到行首，以及跳过单词，在输入很长的命令的时候很有用。

首先打开 iTerm2 的偏好设置（Preferences），然后切换到 Profiles，在右边找到 Keys 快捷键配置：

![iTerm2-&amp;gt;Prefences-&amp;gt;Profiles-&amp;gt;Keys](.gitbook/assets/image%20%2848%29.png)

点击 Key Mappings 下面的加号（+），按下面的表格添加快捷键：

| shortcut | action | send |
| :--- | :--- | :--- |
| ⌘← | SEND ESC SEQ | OH |
| ⌘→ | SEND ESC SEQ | OF |
| ⌥← | SEND ESC SEQ | b |
| ⌥→ | SEND ESC SEQ | f |

如图：

![](.gitbook/assets/image%20%2812%29.png)

如果弹出 Warning，直接点确定即可，如果点了确定没反应，退出再打开就行，配置会加进去。

#### **关闭默认非活跃窗口变灰的选项**

取消勾选`Preferences -> Appearance -> Dim inactive split panes`即可。

## 编辑器

### Sublime Text

{% embed url="https://www.sublimetext.com/" caption="" %}

Sublime Text 是一个非常轻量化的文本编辑器，启动迅速，支持各种语言的代码高亮。

当你只想打开庞大工程里的一个文件的时候，你就可以用它来阅读和修改代码。

![Sublime Text 3](https://www.sublimetext.com/screenshots/3.0/osx@2x.png)

### MacDown

{% embed url="https://macdown.uranusjr.com/" caption="" %}

![MacDown](https://macdown.uranusjr.com/static/images/macdown-demo.png)

MacDown 是一个 markdown 编辑器，支持 Markdown 以及 LaTeX，写文章必备。

### Typora

{% embed url="https://typora.io/" %}

另一个 Markdown 编辑器，与 MacDown 不同在于，MacDown 是分栏编辑，左边 Markdown，右边实时渲染，而 Typora 只有一个编辑界面，实时写实时渲染。

![Typora](https://typora.io/img/new/toc.png)



### Hex Fiend

![Hex Fiend](.gitbook/assets/image%20%2847%29.png)

{% embed url="http://ridiculousfish.com/hexfiend/" %}

Hex Fiend 是一个十六进制编辑器，当你想查看一个二进制文件的内容的时候就可以使用它，比如我会用它来检查我写出的模型权值文件。因为它可以秒开任何大小的文件，有时候我也会用它来查看几百兆的文本文件。

## 开发工具

### Xcode

{% embed url="https://developer.apple.com/xcode/" %}

Xcode 是 macOS 上的 IDE，可以开发 macOS、iPhone、iPad、AppleWatch 等平台上的应用，如果你希望在 iPhone 进行调试，你还需要购买 99$ 的开发者证书。我们一般从 AppStore 上下载 Xcode。

### PyCharm

{% embed url="https://www.jetbrains.com/pycharm/" %}

PyCharm 是我经常使用的 Python IDE，它支持代码高亮、代码提示、调试断点等功能，专业版还支持远程调试，非常适合深度学习从业人员使用。

因为大多数深度学习工程师都不是直接在训练机器上写代码，而是使用一个终端机器远程 ssh 进行代码调试。那么如果每次都是上传代码、运行 Python 脚本、看报错，那么就会非常低效，因为有可能你载入了五分钟的数据集以后，报错模型的某个层写错了，然后检查半天，上传一个新的代码，然后陷入上面的循环。

高效一点的方法就是使用 jupyter notebook 进行开发，即使代码报错了也不会直接退出，我们可以在 jupyter notebook 里继续写代码，直到写出正确的代码。那么这仍然不是高效的方法，因为如果我们有一个错误发生在模型内部的 forward 部分，那么我们就需要用 print 大法在出错代码的前后输出矩阵尺寸、数据类型等关键数据，然后根据报错来修 bug。

那么当我们出现这种报错的时候，使用 PyCharm 的远程调试功能就非常方便了，我们可以在出错的代码前面下断点，然后我们可以看到每个矩阵的尺寸，模型的每一层的参数，不需要写许多 print 去实现我们的想法。如果代码报错是一个除0错误，你还可以直接在变量监视器里面增加一个 `x.mean()` 的条目，然后实时查看 x 的均值，不需要重新运行代码。

### GitHub Desktop

{% embed url="https://desktop.github.com/" %}

GitHub Desktop 是 GitHub 官方客户端，新手必备。

## 浏览器

* Chrome
* Chrome 插件

### Chrome

{% embed url="https://www.google.com/chrome/" %}

目前 Chrome 应该是最受欢迎的浏览器：

![&#x56FE;&#x7247;&#x6765;&#x81EA;&#x7EF4;&#x57FA;&#x767E;&#x79D1;](.gitbook/assets/image%20%2853%29.png)

这里建议使用 Chrome 作为主力浏览器，原因如下：

* 简洁
* 插件强大且免费（Safari 的某些插件是收费的）

### 常用插件

#### Adblock Plus

{% embed url="https://chrome.google.com/webstore/detail/adblock-plus-free-ad-bloc/cfhdojbkjhnklbpkdaibdccddilifddb" %}

拦截广告的好工具。

#### Tampermonkey

{% embed url="https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo" %}

脚本管理器，你可以找到支持各种功能的脚本，比如：

* 去广告
* 下载视频
* 你可以自己写 js 脚本以实现一切功能

#### Proxy SwitchyOmega

{% embed url="https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif" %}

可以很方便地切换代理服务器。

#### Octotree

{% embed url="https://chrome.google.com/webstore/detail/octotree/bkhaagjahfmjljalopjnoealnfndnagc" %}

可以在 GitHub 页面展示代码文件结构，非常方便，如图：

![Octotree](.gitbook/assets/image%20%2811%29.png)

## 实用工具

* Netron
* Karabiner-Elements
* The Unarchiver
* iStat Menus
* Caffeine
* DaisyDisk
* TimeMachineEditor
* Turbo Boost Switcher
* Intel® Power Gadget

### Netron

{% embed url="https://github.com/lutzroeder/netron" %}

它是一个可视化模型结构的软件，支持的模型文件格式有：**ONNX** \(`.onnx`, `.pb`, `.pbtxt`\), **Keras** \(`.h5`, `.keras`\), **Core ML** \(`.mlmodel`\), **Caffe2**\(`predict_net.pb`, `predict_net.pbtxt`\), **MXNet** \(`.model`, `-symbol.json`\) and **TensorFlow Lite** \(`.tflite`\). Netron has experimental support for **Caffe** \(`.caffemodel`, `.prototxt`\), **PyTorch** \(`.pth`\), **Torch** \(`.t7`\), **CNTK** \(`.model`, `.cntk`\), **PaddlePaddle** \(`__model__`\), **Darknet** \(`.cfg`\), **scikit-learn** \(`.pkl`\), **TensorFlow.js** \(`model.json`, `.pb`\) and **TensorFlow**\(`.pb`, `.meta`, `.pbtxt`\).

![Netron](https://raw.githubusercontent.com/lutzroeder/netron/master/media/screenshot.png)

### Karabiner-Elements

{% embed url="https://pqrs.org/osx/karabiner/" %}

Karabiner-Elements 是一个改键工具，机械键盘必备软件。

> 适用于macOS的功能强大且稳定的键盘定制器。

![Karabiner-Elements](.gitbook/assets/image%20%2838%29.png)

我把我的机械键盘的 Command 键和 Option 键替换了，这样就可以像使用原生键盘一样使用我的机械键盘。你还可以把键盘上的 Windows 键和 Alt 键交换位置。

### The Unarchiver

{% embed url="https://theunarchiver.com/" %}

这是一个解压缩软件，可以直接在 App Store 上下载，免费，支持 zip、rar、tar 等格式。

> The Unarchiver 是一款简单易用的小程序，可以解压许多不同类型的存档文件。 它能够打开 Zip、RAR（包括 v5）、7-zip、Tar、Gzip 和 Bzip2 等常见格式。 它还能打开许多旧格式，例如 StuffIt、DiskDoubler、LZH、ARJ 和 ARC。 它还能打开其他各种文件，例如 ISO 和 BIN 磁盘镜像、部分 Windows .EXE 安装程序。 该列表实际上很长 - 有关完整列表，请查看程序主页。

### iStat Menus

{% embed url="https://bjango.com/mac/istatmenus/" %}

这个软件可以监控 Mac 的 CPU、内存、网速等信息。

通过这个软件，我可以直观地查看我跑程序的时候 CPU 有没有全部用上，它在状态栏并不会占用太多空间，下载东西的时候也可以监控网速。

### Caffeine

{% embed url="http://lightheadsw.com/caffeine/" %}

它可以防止你的电脑进入睡眠，你只需要在状态栏点一下就可以打开和关闭，比在设置里面操作方便不少。

### DaisyDisk

{% embed url="https://daisydiskapp.com/" %}

这是一个非常好用的磁盘空间整理工具，你可以检查你的 Mac 上占用空间较大的文件都在哪里，收费。

![DaisyDisk](.gitbook/assets/image%20%2843%29.png)

### TimeMachineEditor

{% embed url="https://tclementdev.com/timemachineeditor/" %}

这个软件可以控制你的 TimeMachine 在什么时候备份，比如我会设置每小时在本地备份一次，但是我工作的时候不要备份，因为如果备份在硬盘里会占用磁盘速度，如果你备份在 NAS 上会占用网速。

![](https://tclementdev.com/timemachineeditor/interval.png)



### Turbo Boost Switcher

{% embed url="http://tbswitcher.rugarciap.com/" %}

这个软件可以关闭 Intel CPU 的睿频，这样可以减少功耗，如果你在旅行的时候没有电源，你只想尽可能保持续航，那么你可以使用这个软件手动关闭睿频。下面的软件可以可视化关闭睿频的过程。

### Intel® Power Gadget

{% embed url="https://software.intel.com/en-us/articles/intel-power-gadget" %}

![Intel&#xAE; Power Gadget](.gitbook/assets/image%20%2820%29.png)

如图所示，一开始我是关闭睿频的，CPU 频率始终压着灰色的线，4.2GHz，开启睿频以后 CPU 频率上升到了 4.4GHz，并且 CPU 温度上升到了 93 度，相应的功耗也上升了不少。因此在没有足够的电量，或者只是想减少发热以降低风扇噪音的情况下，可以使用上面的 Turbo Boost Switcher 关闭手动关闭睿频。

## 虚拟机

### Parallels Desktop

{% embed url="https://www.parallels.com/products/desktop/" %}

这是一款非常优秀的虚拟机软件，收费。

它创新的融合模式可以让你在 Mac 桌面下，在使用 Windows 软件的时候感觉像在使用 Mac 原生的软件，比如：

![Coherence View mode](.gitbook/assets/image%20%2815%29.png)

后面的窗口是 Finder，前面的窗口是一个 Windows 应用，使用 Parallels Desktop 可以让你无缝使用 Mac 和 Windows 的应用。

