# -*- coding: utf-8 -*
import os
from PIL import Image

in_dir = r"E:\SVN\美术\亚冠棋牌\大厅\切图"
out_dir = r"E:\VineyardValleyImages"

file_list = None
# with open("file_list1.txt", "r", encoding="utf8") as list_file:
#     file_list = list_file.readlines()



# filePath = 'C:\\myLearning\\pythonLearning201712\\carComments\\01\\'
for i,j,k in os.walk(in_dir):
    print(i,j,k)

# for file in file_list:
#     file = file.strip()
#     if not file.endswith(".png"):
#         continue
#     try:
#         image = Image.open(os.path.join(in_dir, file))
#         size_w = image.size[0] - (image.size[0] % 4)
#         size_h = image.size[1] - (image.size[1] % 4)
#         if size_w < 50 or size_h < 50:
#             continue
#         image_size = image.resize((size_w, size_h), Image.ANTIALIAS)
#         out_path = os.path.join(out_dir, file)
#         out_path_dir = os.path.dirname(out_path)
#         if not os.path.exists(out_path_dir):
#             os.makedirs(out_path_dir)
#         image_size.save(out_path)
#     except Exception as exc:
#         pass