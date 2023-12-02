import torch
import sys
sys.path.insert(0, './model/yolov5_obb')
model = torch.load('model/best.pt')
