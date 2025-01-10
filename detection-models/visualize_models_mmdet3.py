# Download mmdetection and put this script in the directory.
# git clone https://github.com/open-mmlab/mmdetection

import os.path
from glob import glob

import yaml
import mmcv
from mmdet.apis import inference_detector, init_detector
from mmdet.visualization import DetLocalVisualizer

img_path = 'demo/123.jpg'

img = mmcv.imread(img_path)

model_config_map = {}
for meta_path in glob('configs/*/metafile.yml'):
    meta = yaml.safe_load(open(meta_path))
    if not isinstance(meta, dict):
        continue
    for model in meta['Models']:
        model_config_map[model['Config']] = model

config_path_list = [
    'configs/grounding_dino/grounding_dino_swin-b_finetune_16xb2_1x_coco.py',
    'configs/dino/dino-5scale_swin-l_8xb2-36e_coco.py',
    'configs/detr/detr_r50_8xb2-150e_coco.py',
    'configs/faster_rcnn/faster-rcnn_r50_fpn_2x_coco.py',
    'configs/mask_rcnn/mask-rcnn_r50_fpn_2x_coco.py',
    'configs/yolo/yolov3_d53_8xb8-ms-608-273e_coco.py',
]

visualizer = DetLocalVisualizer(
    bbox_color=(72, 241, 72),
    text_color=(200, 200, 200),
    mask_color='coco',
)

for config_path in config_path_list:
    model_meta = model_config_map[config_path]
    print(model_meta)

    checkpoint_path = model_meta['Weights']
    model_filename = os.path.splitext(os.path.split(checkpoint_path)[1])[0]

    score = model_meta['Results'][0]['Metrics']['box AP']
    model_name = f"{model_meta['Name']}_{score}"

    model = init_detector(config_path, checkpoint_path)
    result = inference_detector(model, img, text_prompt='car')

    visualizer.dataset_meta = model.dataset_meta
    visualizer.add_datasample(
        'new_result',
        mmcv.bgr2rgb(img),
        data_sample=result,
        draw_gt=False,
        out_file=f'demo/{model_name}.jpg',
        pred_score_thr=0.5)

    # model.show_result(
    #     img_path,
    #     result,
    #     score_thr=0.5,
    #     bbox_color=(72, 241, 72),
    #     mask_color='coco',
    #     text_color=(200, 200, 200),
    #     out_file=f'demo/{model_name}.jpg'
    # )
