#!/usr/bin/env python
# encodeing:utf-8
'''
@ author:  Ming Cheng  
@ Email: fccchengm@zzu.edu.cn
@ time: 2018/11/15

@ 计算手术记录数据集中是否每个实体是否均足够，>60
'''
import os
import re
import string
import xml.dom.minidom
from _overlapped import NULL
from _ast import In


# 住院号处理
def modfile(filepath,writePath):

    detailPath = filepath
    writePa = writePath
    
    print('# 遍历：' + detailPath)
    f = open(detailPath, mode='r', encoding='UTF-8')
    lines = f.readlines()#读取全部内容  
    i = 0
    str =''
    for line in lines: 

        line =  line.strip()
        line = ',\''+line+'\''
        str = str +line

                    
    newFile = open(writePa,'w', encoding='utf-8')
    newFile.write(str)  
    newFile.close()
    print(writePath+'已生成') 
 
    

if __name__ == '__main__':
    print('2018年11月15日  程铭  测试数据集中每一个实体个数')
    modfile('E:\PythonNew\EMRProject\data/1.txt','E:\PythonNew\EMRProject\data/1-.txt')
    
    # 删除手术名称
#     modfile('E:\PythonNew\EMRProject\data\Gastriced_Operation','E:\PythonNew\EMRProject\data\Gastriced_Operation_1')
#     modfileSM('E:\PythonNew\EMRProject\data\Gastriced_Operation_2','E:\PythonNew\EMRProject\data\Gastriced_Operation','E:\PythonNew\EMRProject\data\Gastriced_Operation_3')
#!/usr/bin/env python