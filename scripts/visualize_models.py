# Download mmdetection and put this script in the directory.
# git clone https://github.com/open-mmlab/mmdetection

import os.path
from glob import glob

import yaml

from mmdet.apis import inference_detector, init_detector

img_path = 'demo/1.jpg'

model_config_map = {}
for meta_path in glob('configs/*/metafile.yml'):
    meta = yaml.safe_load(open(meta_path))
    for model in meta['Models']:
        model_config_map[model['Config']] = model

config_path_list = [
    'configs/mask_rcnn/mask_rcnn_r50_fpn_2x_coco.py',
    'configs/cascade_rcnn/cascade_mask_rcnn_r50_fpn_mstrain_3x_coco.py',
    'configs/ssd/ssdlite_mobilenetv2_scratch_600e_coco.py',
    'configs/yolo/yolov3_d53_fp16_mstrain-608_273e_coco.py',
    'configs/swin/mask_rcnn_swin-t-p4-w7_fpn_ms-crop-3x_coco.py',
    'configs/queryinst/queryinst_r50_fpn_300_proposals_crop_mstrain_480-800_3x_coco.py',
    'configs/detr/detr_r50_8x2_150e_coco.py'
]


for config_path in config_path_list:
    model = model_config_map[config_path]
    print(model)

    checkpoint_path = model['Weights']
    model_name = os.path.splitext(os.path.split(checkpoint_path)[1])[0]

    model = init_detector(config_path, checkpoint_path)
    result = inference_detector(model, img_path)

    model.show_result(
        img_path,
        result,
        score_thr=0.3,
        bbox_color=(72, 241, 72),
        mask_color='coco',
        text_color=(200, 200, 200),
        out_file=f'demo/{model_name}.jpg'
    )
