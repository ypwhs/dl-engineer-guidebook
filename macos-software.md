# macOS 软件



下面是我安装的与工作有关的软件。

## 终端

* iTerm
* oh my zsh

### iTerm

终端首选 iTerm，官网是 [https://www.iterm2.com/](https://www.iterm2.com/)

最大的好处是可以分屏使用，比如：

![iTerm2](.gitbook/assets/image%20%285%29.png)

### oh my zsh

装好了终端软件以后，我们还需要安装一个好用的 shell 解释器，zsh 和 oh my zsh，官网是 [https://ohmyz.sh](https://ohmyz.sh)

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

## 浏览器

* Chrome
* Chrome 插件

### Chrome

### 常用插件

* [Adblock Plus](https://chrome.google.com/webstore/detail/adblock-plus/cfhdojbkjhnklbpkdaibdccddilifddb)
* [Tampermonkey](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo)
* [Proxy SwitchyOmega](https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif)
* [Octotree](https://chrome.google.com/webstore/detail/octotree/bkhaagjahfmjljalopjnoealnfndnagc)

上面这几个是比较大众化的插件，此外下面还有几个对我个人比较有用的插件：

* [baidu-dl](https://chrome.google.com/webstore/detail/baidu-dl/lflnkcmjnhfedgibjackiibmcdnnoadb)
* [YAAW for Chrome](https://chrome.google.com/webstore/detail/yaaw-for-chrome/dennnbdlpgjgbcjfgaohdahloollfgoc)
* [v2ex plus](https://chrome.google.com/webstore/detail/v2ex-plus/daeclijmnojoemooblcbfeeceopnkolo)
* [1password](https://1password.com/)
* [京价保 - 京东价保助手](https://chrome.google.com/webstore/detail/京价保-京东价保助手/gfgkebiommjpiaomalcbfefimhhanlfd)

可以根据自己的需求对 Chrome 进行配置。

## 编辑器

* [Sublime Text](https://www.sublimetext.com/)
* [MacDown](https://macdown.uranusjr.com/)
* [Hex Fiend](http://ridiculousfish.com/hexfiend/)

### Sublime Text

Sublime Text 是一个非常轻量化的文本编辑器，启动迅速，支持各种语言的代码高亮。当你的同事给你发过来一个没有整个工程结构，只是一个代码片段的文件的时候，你就可以用它来对代码进行高亮。官方网址：[https://www.sublimetext.com/](https://www.sublimetext.com/)

### MacDown

MacDown 是一个 markdown 编辑器，我现在正在用它写文章，官方网址：[https://macdown.uranusjr.com/](https://macdown.uranusjr.com/)

### Hex Fiend

![Hex Fiend](.gitbook/assets/image%20%286%29.png)

Hex Fiend 是一个十六进制编辑器，当你想查看一个二进制文件的内容的时候就可以使用它，比如我会用它来检查我写出的模型权值文件。因为它可以秒开任何大小的文件，有时候我也会用它来查看几百兆的文本文件。官方网址：[http://ridiculousfish.com/hexfiend/](http://ridiculousfish.com/hexfiend/)

## 开发工具

* [Xcode](https://developer.apple.com/xcode/)
* [PyCharm](https://www.jetbrains.com/pycharm/)
* [GitHub Desktop](https://desktop.github.com/)

### Xcode

Xcode 是 macOS 上的 IDE，可以开发 macOS、iPhone、iPad、AppleWatch 等平台上的应用，如果你希望在 iPhone 进行调试，你还需要购买 99$ 的开发者证书。我们一般从 AppStore 上下载 Xcode。官方网址：[https://developer.apple.com/xcode/](https://developer.apple.com/xcode/)

### PyCharm

PyCharm 是我经常使用的 Python IDE，它支持代码高亮、代码提示、调试断点等功能，专业版还支持远程调试，非常适合深度学习从业人员使用。官方网址：[https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/)

因为大多数深度学习工程师都不是直接在八卡机器上写代码，而是使用一个终端机器远程 ssh 进行代码调试。那么如果每次都是上传代码、运行 Python 脚本、看报错，那么就会非常低效，因为有可能你载入了五分钟的数据集以后，报错模型的某个层写错了，然后检查半天，上传一个新的代码，然后陷入上面的循环。

高效一点的方法就是使用 jupyter notebook 进行开发，即使代码报错了也不会直接退出，我们可以在 jupyter notebook 里继续写代码，直到写出正确的代码。那么这仍然不是高效的方法，因为如果我们有一个错误发生在模型内部的 forward 部分，那么我们就需要用 print 大法在出错代码的前后输出矩阵尺寸、数据类型等关键数据，然后根据报错来修 bug。

那么当我们出现这种报错的时候，使用 PyCharm 的远程调试功能就非常方便了，我们可以在出错的代码前面下断点，然后我们可以看到每个矩阵的尺寸，模型的每一层的参数，不需要写许多 print 去实现我们的想法。如果代码报错是一个除0错误，你还可以直接在变量监视器里面增加一个 x.mean\(\) 的条目，然后实时查看 x 的均值，不需要重新运行代码。

### GitHub Desktop

GitHub Desktop 是 GitHub 官方客户端，新手必备。

官方网址：[https://desktop.github.com/](https://desktop.github.com/)

## 实用工具

* Karabiner
* The Unarchiver
* iStat Menus
* Caffeine
* Turbo Boost Switcher
* DaisyDisk
* Netron
* TimeMachineEditor
* Intel® Power Gadget

## 虚拟机

* Parallels Desktop

