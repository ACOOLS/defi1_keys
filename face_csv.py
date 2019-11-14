import os
import cv2

dataset_path="gender_dataset_face"
csv_lines = []
classe= None
for class_name in os.listdir(dataset_path):
    class_path = os.path.join(dataset_path, class_name)
    if (class_name=="man"):
    	classe=1
    else :
    	classe=2
    for path in os.listdir(class_path):
    	image_path=os.path.join(class_path, path)
    	img=cv2.imread(image_path)
    	if (img is not None):
    		height = img.shape[0]
    		width = img.shape[1]
    		csv_lines.append('{} {},{},{},{},{}\n'.format(image_path, 0,0, width, height,classe))
with open(os.path.join('.', 'annotations.csv'), 'a') as f:
	for l in csv_lines:
		f.write(l)
