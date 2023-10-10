import cv2
import torch
import imutils

def get_imgs(img, angle=10):
    
    imgs = []
    angles = []
    for i in range(0, 180+1, angle):
        imgs.append(imutils.rotate(img, i))
        angles.append(i)
    return imgs, angles

def get_diff(xmin, ymin, xmax, ymax):
    return (xmax - xmin) - (ymax - ymin)

def get_rotated_angle(results, angles):
    max_diff = None
    angle = None

    for i in range(len(angles)):
        xys = results.pandas().xyxy[i]
        if len(xys) == 0:
            continue
        xy = xys.loc[0] # TODO: This code is only for 1 object
        diff = get_diff(xy.xmin, xy.ymin, xy.xmax, xy.ymax)
        if max_diff == None or diff > max_diff :
            max_diff = diff
            angle = angles[i]
            print(xy.confidence)
    return angle
    

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
# cam = cv2.VideoCapture(0)
# ret, img = cam.read()
img = cv2.imread('./img_sample.jpeg')

imgs, angles = get_imgs(img)

results = model(imgs)
results.save()

angle = get_rotated_angle(results, angles)

print(angle)  # img1 predictions (tensor)

# Close the camera
# cam.release()
cv2.destroyAllWindows()
