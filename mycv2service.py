# -*- coding: utf-8 -*-
import flask
import cv2
import json
from json import dumps
from matplotlib import pyplot as plt

app = flask.Flask(__name__)

imgpath = "test.jpeg"  # 图片路径

# 算法导入：sobel边缘检测
def sobelimg(img):
    # 1 读取图像
    img = img #cv2.imread('./horse.jpg',0)
    # 2 计算Sobel卷积结果
    x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
    y = cv2.Sobel(img, cv2.CV_16S, 0, 1)
    # 3 将数据进行转换
    Scale_absX = cv2.convertScaleAbs(x)  # convert 转换  scale 缩放
    Scale_absY = cv2.convertScaleAbs(y)
    # 4 结果合成
    result = cv2.addWeighted(Scale_absX, 0.5, Scale_absY, 0.5, 0)
    # # 5 图像显示
    # plt.figure(figsize=(10,8),dpi=100)
    # plt.subplot(121),plt.imshow(img,cmap=plt.cm.gray),plt.title('原图')
    # plt.xticks([]), plt.yticks([])
    # plt.subplot(122),plt.imshow(result,cmap = plt.cm.gray),plt.title('Sobel滤波后结果')
    # plt.xticks([]), plt.yticks([])
    # plt.show()
    return result


# 图像处理中间操作，可以在下面的过程中添加，然后将结果传输出去
def input_image(imgpath):
    img = cv2.imread(imgpath)
    img = sobelimg(img)
    # # 保存为的json文件
    JSON_NAME = 'myopencv.json'

    # numpy中ndarray文件转为list
    img_list = img.tolist()

    # 字典形式保存数组
    img_dict = {}
    img_dict['name'] = imgpath
    img_dict['content'] = img_list

    # 保存为json格式
    json_data = dumps(img_dict, indent=2)

    # 将数据保存到文件
    with open(JSON_NAME, 'w') as json_file:
        json_file.write(json_data)

    # 读取文件为字典
    with open(JSON_NAME, "rb") as json_file:
        img_dict = json.load(json_file)
        return img_dict

# 访问"http://127.0.0.1:5000/"，可以返回get和post传过来的数据
@app.route('/bot')
def bot():
    # 默认只接收get请求，@app.route('/',methods=["GET","POST"])或者只写"POST",同时接收两种请求
    try:
        # 网页输入文字
        spoken = flask.request.values.get("spoken") if "spoken" in flask.request.values else ""

        # 文字传输过程处理
        qouts =  '我爱你，'+ spoken

        # 图像传输处理
        img_dict = input_image(imgpath)
        x = {'message': 'success',"cvimg": img_dict,'data': {'type': 5000, 'info': {'text':qouts }}}
        print("data:",x)
        return x
    except Exception as err:
        return "输入错误，请重新输入"

if __name__ == '__main__':
    app.run()