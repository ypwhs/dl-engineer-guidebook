# macOS 环境

这篇文章会介绍我在 macOS 的终端里安装的命令和软件。

## [Homebrew](https://brew.sh/index_zh-cn)

Homebrew 是 macOS 上的一个包管理器，你可以使用 Homebrew 安装 Apple 没有预装但[你需要的东西](https://formulae.brew.sh/formula/)。

安装 Homebrew 只需要一行命令：

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

使用 Homebrew 安装一个 wget 吧：

```bash
brew install wget
```

当你需要更新的时候，可以使用下面的命令完成：

```bash
brew update && brew upgrade && brew cleanup
```

### 切换源

如果你觉得使用brew安装和更新软件的时候非常慢，可以使用其他的镜像，如[清华大学](https://mirrors.tuna.tsinghua.edu.cn/help/homebrew/)：

使用下面的命令可以加速 `brew update` ：

```bash
git -C "$(brew --repo)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git
git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git
git -C "$(brew --repo homebrew/cask)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask.git
brew update
```

设置下面的环境变量可以加速 `brew install` ：

```bash
export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles
```

## [Oh My Zsh](https://ohmyz.sh/)

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

## 必备软件

使用 [homebrew-cask](https://github.com/Homebrew/homebrew-cask) 可以轻松安装各种 macOS 软件，下面的命令可以安装一些必备软件：

### 终端

```bash
brew cask install iTerm2
```

### 编辑器

```bash
brew cask install Sublime-Text MacDown Typora Hex-Fiend 
```

### 浏览器

```bash
brew cask install Google-Chrome
```

### 开发软件

```bash
brew cask install PyCharm Anaconda GitHub Postman
```

### 实用工具

```bash
brew cask install Netron Karabiner-Elements The-Unarchiver Caffeine
```

### 日常应用

```bash
brew cask install WeChat QQ IINA BaiduNetdisk
```

## 必备命令

```bash
brew install git htop nload wget
```

### git

git 是代码管理工具。

### htop

htop 是一个系统监控与进程管理软件， 如：

<script id="asciicast-eWBQp36f4KWmhMX1FAoQ8SQl4" src="https://asciinema.org/a/eWBQp36f4KWmhMX1FAoQ8SQl4.js" async></script>

### nload

nload 是一个网速监控命令，你可以用它查看比如打包 docker 的时候的网速如何，是否在下载依赖的软件包。

下面是运行 [https://www.speedtest.net](https://www.speedtest.net) 的时候监控 nload 的过程：

<script id="asciicast-o2IpTuWi93dRo2E1SHP2rILKZ" src="https://asciinema.org/a/o2IpTuWi93dRo2E1SHP2rILKZ.js" async></script>

### wget

很方便的命令行下载工具，比如：

```bash
wget https://repo.anaconda.com/archive/Anaconda3-2019.03-MacOSX-x86_64.sh
bash Anaconda3-2019.03-MacOSX-x86_64.sh
```

通过上面的命令，你可以下载 Anaconda 安装包，然后安装 Anaconda。

通过 `-c` 参数，可以接着上次的进度继续下载。

如：

<script id="asciicast-5iHU0tVcLZxUGUubbPG7U8AoY" src="https://asciinema.org/a/5iHU0tVcLZxUGUubbPG7U8AoY.js" async></script>

