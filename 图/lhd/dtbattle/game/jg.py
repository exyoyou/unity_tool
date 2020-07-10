# -*- coding: utf-8 -*
import os
from PIL import Image
import shutil

rootPath = os.getcwd()
in_dir = rootPath
out_dir = rootPath + "/out"

file_list = os.listdir(rootPath)
# with open("file_list1.txt", "r", encoding="utf8") as list_file:
#     file_list = list_file.readlines()

for file in file_list:
    file = file.strip()
    if not file.endswith(".png") and not file.endswith(".jpg"):
        continue
    try:
    	print file
        image = Image.open(os.path.join(in_dir, file))
        size_w = image.size[0] + 4 - (image.size[0] % 4)
        size_h = image.size[1] + 4 - (image.size[1] % 4)
        # if size_w < 50 or size_h < 50:
        # 	shutil.copy(os.path.join(in_dir, file), os.path.join(out_dir, file))
            # continue
        image_size = image.resize((size_w, size_h), Image.ANTIALIAS)
        out_path = os.path.join(out_dir, file)
        out_path_dir = os.path.dirname(out_path)
        if not os.path.exists(out_path_dir):
            os.makedirs(out_path_dir)
        image_size.save(out_path)
    except Exception as exc:
    	# print file
     #    out_path = os.path.join(out_dir, file)
    	# print out_path

		# shutil.copy(file,out_path)
        pass