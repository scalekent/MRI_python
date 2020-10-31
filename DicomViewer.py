#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: ScaleKent

'''
Some basic packages: 
    pip install pydicom
    pip install matplotlib
    pip install pillow

'''

import pydicom as dicom
from matplotlib import pyplot as plt
from PIL import Image

dicom_dataset = dicom.read_file("C:\\Users\\ScaleKent\\Desktop\\MRI\\MRI_python\\dicom_file\\003-001.dcm")
                                # 目标 .dcm 文件的所在目录
print(dicom_dataset)

# Dicom pixel show
plt.imshow(dicom_dataset.pixel_array, cmap= 'bone')          # cmap: color
plt.show()
