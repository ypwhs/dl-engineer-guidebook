# 常用 CV 数据集

计算机视觉方面常用的数据集。

## 数据集使用方法

### TensorFlow

* [https://www.tensorflow.org/datasets/datasets](https://www.tensorflow.org/datasets/datasets)
* [https://www.tensorflow.org/api\_docs/python/tf/keras/datasets](https://www.tensorflow.org/api_docs/python/tf/keras/datasets)

### PyTorch

* [https://pytorch.org/docs/stable/torchvision/datasets.html](https://pytorch.org/docs/stable/torchvision/datasets.html)

## [MNIST](http://yann.lecun.com/exdb/mnist/)



![MNISTsamples](imgs/image(1).png)

MNIST 是一个手写数字数据集，训练集60000张，测试集 10000张，共有 10 个类别，图像是尺寸为 \(28, 28\) 的黑白图。

## [CIFAR](https://www.cs.toronto.edu/~kriz/cifar.html)



![CIFAR-10samples](imgs/image(15).png)

CIFAR-10 是一个彩色图像数据集，训练集 60000张，测试集 10000张，共有 10 个类别，图像是尺寸为 \(32, 32\) 的彩图。

此外还有 CIFAR-100 数据集，训练集有 60000张，测试集 10000张，共有 100个类别，图像也是 \(32, 32\) 的彩图。

## [ImageNet](http://www.image-net.org/challenges/LSVRC/2012/nonpub-downloads)

![](http://cs231n.github.io/assets/cnnvis/tsne.jpeg)

ImageNet 是一个把深度学习推向一个新的高度的数据集，非常重要。

ImageNet 2012 训练集共有约 120万张图像，验证集有 50000张，图像尺寸各不相同，在使用的时候通常会经过缩放和随机裁剪处理为相同尺寸的正方形图片。

VGG、ResNet 和 DenseNet 的默认图像尺寸为 224，Inception 是 299 ，NASNet 是 331，最新的 EfficientNet 使用了从 224 到 600 的不同尺寸。尺寸越大的同时也会使精度越高。

## [VOC](http://host.robots.ox.ac.uk/pascal/VOC/)

![VOCsamples](imgs/image(45).png)

VOC 的全称是 The PASCAL Visual Object Classes Challenge，该数据集的标注很丰富，可以用于检测和分割等任务。该数据集共有 20个类别。在 YOLOv3 的训练中，使用了 VOC 2007 到 VOC 2012 的所有数据。

VOC 2007 有 9963 张图像，其中训练集 2501 张，验证集2510 张，测试集 4952 张。

## [COCO](http://cocodataset.org)

![](http://cocodataset.org/images/coco-examples.jpg)

COCO 全称是 Common Objects in Context，是一个大规模检测、分割、关键点和看图说话数据集。数据集有 80 个类别。

COCO 2014 训练集有 83k 张图，验证集有 41k，测试集有 41k。  
COCO 2015 测试集有 81k。  
COCO 2017 训练集有 118k ，验证集有 5k，测试集有 41k。

## [CelebA](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html)

![](http://mmlab.ie.cuhk.edu.hk/projects/celeba/overview.png)

CelebA 全称是 Large-scale CelebFaces Attributes \(CelebA\) Dataset，意思是大规模名人面部属性数据集。数据集共有 202599张图，10117位名人，属性有头发、眉毛、眼睛、鼻子、嘴巴、表情和性别等40种属性。此数据集可以用来做人脸识别（分类）、人脸检测、人脸关键点检测、人脸 GAN 等任务。

