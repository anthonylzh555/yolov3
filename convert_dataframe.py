import xml.etree.ElementTree as ET
from os import getcwd, walk, listdir
from os.path import join, isfile, isdir, join
"""
Convert the dataframe
from PascalVOC to YOLO
"""

# define your own classes
#classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
classes=["lauggage"]

def convert_annotation(image_id, list_file):
    in_file = open('dataset/xml/%s.xml'%(image_id),encoding='utf-8')
    tree = ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text),
                                            int(xmlbox.find('xmax').text),
                                            int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

        
wd = getcwd()
own_data_name=[]
mypath = "dataset/img"
files = listdir(mypath)

for f in files:
    fullpath = join(mypath, f)
    if isfile(fullpath):
        print("document：", f)
        own_data_name.append(f)
print(own_data_name)
          
list_file = open('own_datapath.txt', 'w',encoding='utf-8')
for image_id in own_data_name:
    list_file.write('dataset/img/%s.jpg'%(image_id.split('.')[0]))
    if "Thumbs" not in image_id:
        convert_annotation(image_id.split('.')[0], list_file)
        list_file.write('\n')
list_file.close()

