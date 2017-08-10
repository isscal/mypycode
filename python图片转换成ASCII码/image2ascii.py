# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 03:31:31 2017

@author: dc
"""

from PIL import Image
import numpy as np
import argparse

ascii_char = list('''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ''')

#命令行输入参数处理
parser = argparse.ArgumentParser()
    
parser.add_argument('file')

parser.add_argument('height', type = int)

parser.add_argument('width', type = int)

#获取参数
args = parser.parse_args()

filepath = args.file

hh = args.height

ww = args.width

def RGB2char(r,g,b):
    
    #RGB值变为灰度图像
    gray = round(0.2126*r+0.7152*g+0.0722*b)
    #由一下映射关系得到字符对应下标
    label = np.int(gray/(256.0+1)*len(ascii_char))
    #返回字符
    return ascii_char[label]


def DrawAsciiImage(image, height=150, width=150):
    #输入参数为处理图像，输出高度，输出宽度
    
    #将图像按照输出高度宽度来设置
    ima = image.resize((height,width), Image.NEAREST)
    
    #txt_image存放输出的字符图像，以字符串的形式
    txt_image = ""
      
    #遍历每个像素点，进行映射变换
    for i in range(height):
        
        for j in range(width):
            
            r, g, b = ima.getpixel((j,i))
            
            point = RGB2char(r,g,b)
        
            txt_image += point
    
        txt_image += '\n'
    
    return txt_image    


if __name__ == '__main__':
    
    #读入图像，用PIL库的读入函数
    image = Image.open(filepath)
    
    #读入的图像每个像素有4维，这里变为rgb三维
    rgb_im = image.convert('RGB')
    
    #rgb图像变为字符图像
    txt_image = DrawAsciiImage(rgb_im,hh,ww)

    print(txt_image)
    
    #写入文件，注意用'wb'方式会出现TypeError
    with open('ascii_image.txt', 'w') as f:
        f.write(txt_image)
    
    #a = input("press any key to quit")

    