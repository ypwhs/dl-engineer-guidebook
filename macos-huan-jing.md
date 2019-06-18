# macOS 环境

## Homebrew

{% embed url="https://brew.sh/index\_zh-cn" caption="Homebrew" %}

Homebrew 是 macOS 上的一个包管理器，使用 Homebrew 安装 Apple 没有预装但 [你需要的东西](https://formulae.brew.sh/formula/)。

安装 Homebrew 只需要一行命令：

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

使用 Homebrew 安装一个 curl 吧：

```bash
brew install curl
```

## Oh My Zsh

{% embed url="https://ohmyz.sh" caption="Oh My Zsh" %}

装好了终端软件以后，我们还需要安装一个好用的 shell 解释器，zsh 和 oh my zsh。

它比默认的 bash 有以下几个优点：

* 当你使用 tab 提示的时候，如果有多个匹配项，你可以用 tab 进行切换
* 当你想使用一个之前输入过的命令的时候，只需要输入首字母，然后按上方向键切换

#### **在 macOS 下安装 oh my zsh**

在 macOS 下，首先需要安装 zsh，然后再安装 oh my zsh。

安装 oh my zsh 的步骤如下：

* 安装 [zsh](https://github.com/robbyrussell/oh-my-zsh/wiki/Installing-ZSH)
* 安装 [oh my zsh](https://ohmyz.sh/)

完整命令如下：

```bash
brew install zsh zsh-completions
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

最后需要输入一次密码，记得输入正确，否则下一次启动终端就不会使用 zsh。如果你不小心错过了，可以用下面的命令手动切换默认终端：

```bash
chsh -s /bin/zsh
```

