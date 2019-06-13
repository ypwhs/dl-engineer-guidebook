# macOS 软件

下面是我安装的与工作有关的软件。

## 终端

### iTerm2

{% embed url="https://www.iterm2.com/" %}

终端首选 iTerm，最大的好处是可以结合 tmux 分屏使用，比如：

![iTerm2](.gitbook/assets/image%20%288%29.png)

### 快捷键配置

开启 ⌘←, ⌘→ 和 ⌥←, ⌥→ 快捷键，可以直接跳到行首，以及跳过单词，在输入很长的命令的时候很有用。

首先打开 iTerm2 的偏好设置（Preferences），然后切换到 Profiles，在右边找到 Keys 快捷键配置：

![iTerm2-&amp;gt;Prefences-&amp;gt;Profiles-&amp;gt;Keys](.gitbook/assets/image%20%2811%29.png)

点击 Key Mappings 下面的加号（+），按下面的表格添加快捷键：

| shortcut | action | send |
| :--- | :--- | :--- |
| ⌘← | SEND ESC SEQ | OH |
| ⌘→ | SEND ESC SEQ | OF |
| ⌥← | SEND ESC SEQ | b |
| ⌥→ | SEND ESC SEQ | f |

如图：

![](.gitbook/assets/image%20%282%29.png)

如果弹出 Warning，直接点确定即可，如果点了确定没反应，退出再打开就行，配置会加进去。

### oh my zsh

{% embed url="https://ohmyz.sh" %}

装好了终端软件以后，我们还需要安装一个好用的 shell 解释器，zsh 和 oh my zsh。

它比默认的 bash 有以下几个优点：

* 当你使用 tab 提示的时候，如果有多个匹配项，你可以用 tab 进行切换
* 当你想使用一个之前输入过的命令的时候，只需要输入首字母，然后按上方向键切换

#### **在 macOS 下安装 oh my zsh**

在 macOS 下，首先需要安装 zsh，然后再安装 oh my zsh。

安装 oh my zsh 的步骤如下：

* 安装 [homebrew](https://brew.sh/index_zh-cn)
* 安装 [zsh](https://github.com/robbyrussell/oh-my-zsh/wiki/Installing-ZSH)
* 安装 [oh my zsh](https://ohmyz.sh/)

完整命令如下：

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install zsh zsh-completions
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

最后需要输入一次密码，记得输入正确，否则下一次启动终端就不会使用 zsh。如果你不小心错过了，可以用下面的命令手动切换默认终端：

```bash
chsh -s /bin/zsh
```

#### **在 Ubuntu 下安装 oh my zsh**

在 Ubuntu 下安装 oh my zsh 直接执行下面的命令即可：

```bash
sudo apt install -y git zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

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

![Hex Fiend](.gitbook/assets/image%20%289%29.png)

{% embed url="http://ridiculousfish.com/hexfiend/" %}

Hex Fiend 是一个十六进制编辑器，当你想查看一个二进制文件的内容的时候就可以使用它，比如我会用它来检查我写出的模型权值文件。因为它可以秒开任何大小的文件，有时候我也会用它来查看几百兆的文本文件。

## 开发工具

### Xcode

{% embed url="https://developer.apple.com/xcode/" %}

Xcode 是 macOS 上的 IDE，可以开发 macOS、iPhone、iPad、AppleWatch 等平台上的应用，如果你希望在 iPhone 进行调试，你还需要购买 99$ 的开发者证书。我们一般从 AppStore 上下载 Xcode。

### PyCharm

{% embed url="https://www.jetbrains.com/pycharm/" %}

PyCharm 是我经常使用的 Python IDE，它支持代码高亮、代码提示、调试断点等功能，专业版还支持远程调试，非常适合深度学习从业人员使用。

因为大多数深度学习工程师都不是直接在八卡机器上写代码，而是使用一个终端机器远程 ssh 进行代码调试。那么如果每次都是上传代码、运行 Python 脚本、看报错，那么就会非常低效，因为有可能你载入了五分钟的数据集以后，报错模型的某个层写错了，然后检查半天，上传一个新的代码，然后陷入上面的循环。

高效一点的方法就是使用 jupyter notebook 进行开发，即使代码报错了也不会直接退出，我们可以在 jupyter notebook 里继续写代码，直到写出正确的代码。那么这仍然不是高效的方法，因为如果我们有一个错误发生在模型内部的 forward 部分，那么我们就需要用 print 大法在出错代码的前后输出矩阵尺寸、数据类型等关键数据，然后根据报错来修 bug。

那么当我们出现这种报错的时候，使用 PyCharm 的远程调试功能就非常方便了，我们可以在出错的代码前面下断点，然后我们可以看到每个矩阵的尺寸，模型的每一层的参数，不需要写许多 print 去实现我们的想法。如果代码报错是一个除0错误，你还可以直接在变量监视器里面增加一个 x.mean\(\) 的条目，然后实时查看 x 的均值，不需要重新运行代码。

### GitHub Desktop

{% embed url="https://desktop.github.com/" %}

GitHub Desktop 是 GitHub 官方客户端，新手必备。

## 浏览器

* Chrome
* Chrome 插件

### Chrome

{% embed url="https://www.google.com/chrome/" %}

目前 Chrome 应该是最受欢迎的浏览器：

![&#x56FE;&#x7247;&#x6765;&#x81EA;&#x7EF4;&#x57FA;&#x767E;&#x79D1;](.gitbook/assets/image%20%2814%29.png)

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

![Octotree](.gitbook/assets/image%20%281%29.png)

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

![Karabiner-Elements](.gitbook/assets/image%20%287%29.png)

我把我的机械键盘的 Command 键和 Option 键替换了，这样就可以像使用原生键盘一样使用我的机械键盘。你还可以把键盘上的 Windows 键和 Alt 键交换位置。

### The Unarchiver

{% embed url="https://theunarchiver.com/" %}

这是一个解压缩软件，可以直接在 App Store 上下载，免费，支持 zip、rar、tar 等格式。

> The Unarchiver 是一款简单易用的小程序，可以解压许多不同类型的存档文件。 它能够打开 Zip、RAR（包括 v5）、7-zip、Tar、Gzip 和 Bzip2 等常见格式。 它还能打开许多旧格式，例如 StuffIt、DiskDoubler、LZH、ARJ 和 ARC。 它还能打开其他各种文件，例如 ISO 和 BIN 磁盘镜像、部分 Windows .EXE 安装程序。 该列表实际上很长 - 有关完整列表，请查看程序主页。

## 虚拟机

* Parallels Desktop

