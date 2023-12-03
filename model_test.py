import torch
import sys
# sys.path.insert(0, './model/yolov5_obb')
model = torch.hub.load('./model/yolov5_obb', 'custom', source='local', path='./model/best.pt')
im = './model/test.jpg'
results = model(im)
results.show()
# results.pandas().xyxy[0]
