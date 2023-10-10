import cv2
import torch
import imutils

def get_imgs():
    ret, img = cam.read()
    imgs = []
    for i in range(0, 91, angle):
        imgs.append(imutils.rotate(img, i))
    return imgs


def get_diff(xmin, ymin, xmax, ymax):
    return (xmax - xmin) - (ymax - ymin)

# Load the model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Set webcam input
cam = cv2.VideoCapture(0)

time = 1
angle = 10

while time > 0:
    imgs_rotate = get_imgs()
    # if (cv2.waitKey(1) & 0xFF == ord("q")) or (cv2.waitKey(1)==27):
    #     break
    time -= 1

results = model(imgs_rotate)
#results.show()
results.save()
print(results.pandas().xyxy[0].xmin)  # img1 predictions (tensor)

# Close the camera
cam.release()
cv2.destroyAllWindows()
