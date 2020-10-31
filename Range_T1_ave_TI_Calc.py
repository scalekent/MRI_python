#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: ScaleKent

import os
import pydicom as dicom
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from PIL import Image

file_path = "C:\\Users\\ScaleKent\\Desktop\\MRI\\MRI_python\\dicom_file\\"       # Dicom文件之主路径
pixel_dot = [28,30]                                                              # 数据点坐标 x,y
init_guess = [3000,3000]                                                         # 初始猜测值设定 a,b

fin_mix_T1_map = np.zeros(shape=(128,128), dtype=np.int64)
img = Image.new("L",(128,128))     # 新建相同size的img
pixel_num = 0               # 像素点数量
IN_pixel_sums_T1 = 0        # 在像素点内之 T1 总和
for mix_col in range(53,75,1):                              # x上下限范围
    for mix_row in range(87,107,1):                          # y上下限范围



        # 读取 Dicom 之目录,读取每一个张 dcm
        os.chdir(file_path)
        for root, dirs, files in os.walk(file_path):  
            print('file_path: %s' %(str(root)))
            print(files)

        # 新建矩阵 M_dataset , M_x (乃用于存同像素点上之index值 及 TE\TR\TI等值之存储)
        [i, j] = [pixel_dot[1], pixel_dot[0]]
        M_dataset = np.zeros(shape=(len(files)), dtype=np.int)
        M_x = np.zeros(shape=(len(files)), dtype=np.int)

        # 将目录下文件读出存至 M_ti_dataset , M_x
        print('')
        for fileloop in range(len(files)):
            dataset = dicom.read_file(files[fileloop])
            M_dataset[fileloop] = int(dataset.pixel_array[i,j])
            M_x[fileloop] = int(dataset.InversionTime)

            print('M_dataset: %d' %(dataset.pixel_array[i,j]))
            print('M_x: %d' %(dataset.InversionTime))

        print(M_dataset)
        print(M_x)
        print('')

        # Function
        def func_TI(x, a, b):
            return np.abs(      a * (1 - 2 * np.exp( np.array(x) * (-1) / np.array(b)))        )

        # 转存数据
        x = M_x
        y = M_dataset

        # 使用非线性最小二乘拟合
        popt, pcov = curve_fit(func_TI, x, y, p0 = init_guess)

        # 取得 popt 内之拟合系数
        print(popt)
        a = popt[0] 
        b = popt[1]

        # 拟合 y 之 data
        yvals = func_TI(x,a,b) #拟合y值

        # 打印 拟合后之参数
        print('popt:', popt)
        print('a:', a)
        print('b:', b)
        print('pcov:', pcov)
        print('yvals:', yvals)
        print('')
        print('T1:', b)
        print('')

        pixel_num = pixel_num + 1
        IN_pixel_sums_T1 = IN_pixel_sums_T1 + b

        fin_mix_T1_map[mix_row, mix_col] = int(b)
        img.putpixel([mix_row,mix_col], int(fin_mix_T1_map[i,j]))


print(fin_mix_T1_map)

# np.save("fin_mix_T1_map.npy", fin_mix_T1_map)
# np.savetxt("fin_mix_T1_map.txt",fin_mix_T1_map)

print('\npixel_num & IN_pixel_sums_T1')
print(pixel_num)
print(IN_pixel_sums_T1)

print('\nT1 ave')
print(IN_pixel_sums_T1/pixel_num)

