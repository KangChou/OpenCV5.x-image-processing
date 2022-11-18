# -*- coding: utf-8 -*-
import requests
import numpy as np
import json
import cv2

def getTextcv2picture(spoken,url):

    sess = requests.get(url)
    answer = sess.text
    answer = json.loads(answer)

    qss = answer["data"]
    # print(qss)

    resq = answer["cvimg"]

    # 获取字典中内容，转为list
    img_list = resq['content']
    # list转numpy
    img = np.asarray(img_list)
    # 还原为图片文件
    IMAGE_NAME = 'restore.png'
    cv2.imwrite(IMAGE_NAME, img)

    # 可视化 需要将图像转化为uint8
    image = img.astype(np.uint8)
    cv2.imshow('test', image)
    cv2.waitKey(0)

if __name__ == '__main__':
    spoken = "中国"
    url = f"http://127.0.0.1:5000/bot?spoken={spoken}"  # get传送数据
    getTextcv2picture(spoken, url)