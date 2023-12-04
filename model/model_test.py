# import torch
# import sys
# # sys.path.insert(0, './model/yolov5_obb')
# model = torch.hub.load('./model/yolov5_obb', 'custom', source='local', path='./model/best.pt')
# im = './model/test2.jpg'
# results = model(im)
# # results.show()
# print(results.pandas().xyxy[0])

import os
import yolov5_obb.detect as detect

current_dir=os.path.dirname(os.path.realpath(__file__))

weights=os.path.join(current_dir, 'best.pt')
source=os.path.join(current_dir, 'test.jpg')

# !python detect.py --weights "runs/train/exp/weights/best.pt" --source "D:/Code/conveyor-alignment-robot/model/test.jpg" --conf-thres 0.01 --img 416 --device 0 --agnostic
result = detect.run(
 weights=weights,
 source=source,
 conf_thres=0.01,
 imgsz=(416,416),
 device=0,
 agnostic_nms=True,
 return_result=True,
 classes=0
 )

print(result)
