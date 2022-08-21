import os
from glob import glob
#
# path = 'meta-data/images/' #이동복사
# copy_path = './images_copy'
#
# if os.path.exists(path) :
#     # 복사해서 넣을 디렉토리 생성
#     if not os.path.exists(copy_path):
#         os.mkdir(copy_path)
#
#     img_list = glob(path + '*.png')
#     print(img_list)

#퍼일 복사
f = open('meta-data/images/102.png', 'rb')
img = f.read()

#파일 이동
f = open('./102.png', 'wb')
f.write(img)