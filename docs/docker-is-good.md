# Docker 是个好东西

* 什么是 Docker
* 安装 Docker
* 安装 nvidia-docker
* 如何编写 Dockerfile
* 如何编译一个 Docker 镜像
* 如何运行 Docker

## 什么是 Docker

[https://docs.docker.com/](https://docs.docker.com/)

Docker 可以让你把整个应用打包成一个文件，它包含你安装的各种依赖环境，比如 CUDA、cuDNN、TensorFlow 等。其他人可以直接使用 Docker 直接运行你打包的这个镜像，不需要进行繁琐的环境配置。

Docker 的优点：

* 灵活，不管你的应用环境有多复杂，都可以打包成一个镜像
* 便携，只需要打包一次，就可以部署到任何地方运行
* 高效，与宿主机共享操作系统内核，效率很高
* 安全，不同的容器之间互不干扰，崩了不影响其他应用

在没有 Docker 之前，运维需要学会配置各种环境、驱动，解决各种库之间的依赖关系，现在只需要装好必要的驱动，然后运行 Docker 就好，非常方便。

## 安装 Docker

[https://docs.docker.com/install/linux/docker-ce/ubuntu/](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

按照官网上的教程安装即可，下面是我运行的命令：

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

为了避免每次使用 docker 命令都要加 sudo，你可以执行下面的命令：

```bash
sudo usermod -aG docker $USER
```

添加以后，你需要重新登录机器才能生效。

你可以运行下面的命令测试 docker：

```bash
docker run hello-world
```

期望输出：

```text
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

如果出现了权限问题，你可以使用下面的命令重新构建 docker 的文件系统：

```bash
sudo service docker stop
sudo rm -rf /var/lib/docker
sudo service docker start
```

