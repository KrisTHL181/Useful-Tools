import cv2
import numpy as np
import sys
import os
def convert(src,dst):
    # 读取图片
    image = cv2.imread(src)
    # 将图片转换为 RGBA 格式
    rgba_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
    # 提取图片的 alpha 通道
    alpha_channel = rgba_image[:, :, 3]
    # 创建一个全透明的 mask
    mask = np.zeros_like(alpha_channel)
    # 将黑色区域的 mask 设置为不透明
    mask[alpha_channel == 0] = 255
    # 通过 mask 将图片的背景改为透明
    rgba_image[:, :, 3] = mask
    # 将图片保存为新的文件
    cv2.imwrite(dst, rgba_image)

files=os.listdir(sys.argv[1])
for file in files:
    convert(sys.argv[1]+file,sys.argv[2]+file)
