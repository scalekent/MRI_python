# MRI: Dicom basic operation by Python

> sys.version: '3.7.6 (default, Jan  8 2020, 20:23:39) [MSC v.1916 64 bit (AMD64)]'
>
> Author: ScaleKent

This project is to integrate and write some reading and calculation operations on MRI Dicom files.



### .py file description

| file name               | description                                                  |
| ----------------------- | ------------------------------------------------------------ |
| DicomViewer.py          | Read the Dicom file and show pixel_array.                    |
| SinPix_T1_TI_Calc.py    | Calculate the single-pixel T1 value of the T1-weight image (based on TI) |
| SinPix_T1_TR_Calc.py    | Calculate the single-pixel T1 value of the T1-weight image (based on TR) |
| SinPix_T2_TE_Calc.py    | Calculate the single-pixel T2 value of the T2-weight image (based on TE) |
| Range_T1_ave_TI_Calc.py | Calculate the average value of T1 within the pixels of the rectangular range of the T2-weight image (based on TI) |

`Range_T1_ave_TI_Calc.py` is a code specially written for calculating the average value of T1 in a certain range. It can also be applied to the calculation of the range average value of `T2(TE)`/`T1(TR)`, but this code cannot customize the selection of pixel coordinates. Of course, you can choose to manually enter all the coordinates you require by yourself (that requires you to modify the code to achieve it). In this code, I only realized the average of all the pixel T1 values in the rectangle.