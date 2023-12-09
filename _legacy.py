
def mode_validate_algo(): # legacy
  def get_image_t(file_name): # for test
    img = cv2.imread('roboflow/train/images/'+file_name)
    return img
  def get_distance_t(file_name): # for test
    file_name=file_name[:-4]+'.txt'
    with open('roboflow/train/labelTxt/'+file_name,'r') as data_file:
      for line in data_file:
          data = line.split()
    xy_list = []
    for i in range(8):
      xy_list.append(float(data[i]))
      print('get_distance', 640, 640, list(map(int, xy_list)))
    distance = algo.get_distance(640, 640, xy_list)
    # num = 480
    return int(distance)

  file_idx = int(input('Input image idx: ')) # For test
  file_name = os.listdir('roboflow/train/images/')[file_idx]
  print(file_name)
  img = get_image_t(file_name)
  distance = get_distance_t(file_name)
  display(img, distance)
  distance_100 = get_distance_100(distance, img.shape[0])
