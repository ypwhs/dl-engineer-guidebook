---
hide:
  - navigation
---

# 检测模型

更新时间：2024 年 5 月

## 模型概览

### 目标检测模型

下面几个模型是比较经典的检测模型：

* 【1】SSD 2015——经典的 OneStage 模型
* 【2】Faster R-CNN 2015——经典的 TwoStage 模型
* 【3】YOLO v3 2018——速度较快的检测模型
* 【4】CenterNet 2019——AnchorFree 模型
* 【5】DETR 2020——使用 Transformer 做检测任务的模型
* 【6】YOLO v5 2020——速度较快的检测模型

它们在 COCO2017 上的分数如下：

![](detection-models/detection-models.png)

### 实例分割模型

下面几个模型是比较经典的实例分割模型：

* 【1】Mask R-CNN 2017——现代化的实例分割模型
* 【2】Cascade Mask R-CNN 2019——级联的 Mask R-CNN
* 【3】QueryInst 2021——目前排行榜第 10 名
* 【4】SwinV2 2021——目前排行榜第 1 名

它们在 COCO2017 上的分数如下：

![](detection-models/instance-segmentation-models.png)

## 具体模型介绍

### SSD 2015

[SSD: Single Shot MultiBox Detector](https://arxiv.org/abs/1512.02325)

SSD 是 OneStage 的模型，因为没有 RPN、ROI 等操作，所以速度会快很多，代价在于精度有所降低。

YOLO 与 SSD 的结构也是类似的，不过一代的 YOLO 没有使用中间层的特征。

模型结构如下：

![](detection-models/ssd.png)

### YOLOv5 2022

* [YOLOv5](https://github.com/ultralytics/yolov5)
* [YOLOv5中文解析](https://zhuanlan.zhihu.com/p/172121380)

YOLOv5 仍然是属于 OneStage 模型，对结构进行了许多优化，降低了计算量。各种数据增强方法也提高了模型的精度。

![](detection-models/yolov5.png)

### Faster R-CNN 2015

[Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks](https://arxiv.org/abs/1506.01497)

Faster R-CNN 是最经典的 TwoStage 模型。 使用 RPN 提取出可能是物体的区域，然后使用 ROI Pooling 抓出局部特征， 再使用分类和回归将类别和框的位置计算出来。

下图就是 FPN 结构的示意：

![](detection-models/faster-rcnn-rpn.png)

下图是检测头的结构：

![](detection-models/faster-rcnn-detection-head.png)

### DETR 2020

[End-to-End Object Detection with Transformers](https://arxiv.org/abs/2005.12872)

DETR 仍然是使用 CNN 提取特征，不过没有使用传统的 RPN 和检测 Head，因此也没有 Anchor，使用了 Transformer 直接检测物体。

DETR 结构：

![](detection-models/detr-structure.png)

Transformer 结构：

![](detection-models/detr-transformer.png)

Multi-Head Attention 结构：

![](detection-models/detr-multi-head-attention.png)

Attention 结构：

![](detection-models/detr-attention.png)

### Mask R-CNN 2017

[Mask R-CNN](https://arxiv.org/abs/1703.06870)

经典的 TwoStage 模型，检测部分和 Faster R-CNN 一样，先提取可能是物体的部分，然后再提取这部分区域的特征计算类别和框，但是多了一个 Mask 分支，用于逐像素分类，计算该物体的 Mask。

![](detection-models/mask-rcnn-1.png)

![](detection-models/mask-rcnn-2.png)

### Cascade Mask R-CNN 2019

[Cascade R-CNN: High Quality Object Detection and Instance Segmentation](https://arxiv.org/abs/1906.09756)

将模型的结果再输入到新的模型里做精调，反复几次，这样可以提升模型的准确率，但是也会增加计算量。

![](detection-models/cascade-mask-rcnn.png)

## 模型可视化对比

为了综合评价各个模型的能力，我们使用各个模型对下图进行了推断和可视化：

| 模型名称                   | 年份   | bbox mAP | 可视化图                                                                                                                                                                                                                                    |
|------------------------|------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SSD Lite MobileNetV2   | 2015 | 21.3     | [![](detection-models/demo/ssdlite_mobilenetv2_scratch_600e_coco_20210629_110627-974d9307.jpg)](detection-models/demo/ssdlite_mobilenetv2_scratch_600e_coco_20210629_110627-974d9307.jpg)                                               |
| YOLOv3                 | 2018 | 33.7     | [![](detection-models/demo/yolov3_d53_fp16_mstrain-608_273e_coco_20210517_213542-4bc34944.jpg)](detection-models/demo/yolov3_d53_fp16_mstrain-608_273e_coco_20210517_213542-4bc34944.jpg)                                               |
| YOLOv5s                | 2022 | 37.4     | [![](detection-models/demo/yolov5s.jpg)](detection-models/demo/yolov5s.jpg)                                                                                                                                                             |
| YOLOv5x6               | 2022 | 55.0     | [![](detection-models/demo/yolov5x6.jpg)](detection-models/demo/yolov5x6.jpg)                                                                                                                                                           |
| Faster R-CNN R50       | 2015 | 38.4     | [![](detection-models/demo/faster-rcnn_r50_fpn_2x_coco_38.4.jpg)](detection-models/demo/faster-rcnn_r50_fpn_2x_coco_38.4.jpg)                                                   |
| Mask R-CNN R50         | 2017 | 39.2     | [![](detection-models/demo/mask-rcnn_r50_fpn_2x_coco_39.2.jpg)](detection-models/demo/mask-rcnn_r50_fpn_2x_coco_39.2.jpg)                                             |
| Cascade Mask R-CNN R50 | 2019 | 44.3     | [![](detection-models/demo/cascade_mask_rcnn_r50_fpn_mstrain_3x_coco_20210628_164719-5bdc3824.jpg)](detection-models/demo/cascade_mask_rcnn_r50_fpn_mstrain_3x_coco_20210628_164719-5bdc3824.jpg)                                       |
| DETR R50               | 2020 | 39.9     | [![](detection-models/demo/detr_r50_8xb2-150e_coco_39.9.jpg)](detection-models/demo/detr_r50_8xb2-150e_coco_39.9.jpg)                                                                             |
| Swin R50               | 2021 | 46.0     | [![](detection-models/demo/mask_rcnn_swin-t-p4-w7_fpn_ms-crop-3x_coco_20210906_131725-bacf6f7b.jpg)](detection-models/demo/mask_rcnn_swin-t-p4-w7_fpn_ms-crop-3x_coco_20210906_131725-bacf6f7b.jpg)                                     |
| QueryInst R50          | 2021 | 47.5     | [![](detection-models/demo/queryinst_r50_fpn_300_proposals_crop_mstrain_480-800_3x_coco_20210904_101802-85cffbd8.jpg)](detection-models/demo/queryinst_r50_fpn_300_proposals_crop_mstrain_480-800_3x_coco_20210904_101802-85cffbd8.jpg) |
| DINO Swin-L | 2022 | 58.4 | [![](detection-models/demo/dino-5scale_swin-l_8xb2-36e_coco_58.4.jpg)](detection-models/demo/dino-5scale_swin-l_8xb2-36e_coco_58.4.jpg) |
| Grounding DINO Swin-L | 2023 | 59.7 | [![](detection-models/demo/grounding_dino_swin-b_finetune_16xb2_1x_coco_59.7.jpg)](detection-models/demo/grounding_dino_swin-b_finetune_16xb2_1x_coco_59.7.jpg) |

本表格的数据可以使用此脚本跑出：[visualize_models_mmdet3.py](detection-models/visualize_models_mmdet3.py)

可以看到，不是 mAP 分数更高的模型就更准，目前基于 Anchor 的模型依然具备极大的优势。
