# encodeing:utf-8
'''

@author: Ming Cheng
@contact: fccchengm@zzu.edu.cn
@time: 2018/11/03

@XML文件归类 归类相同患者XML文件
'''
import os
import re
import shutil


# Create folder 
# Categorization of patients' medical records
def categorXMLtoFolders(inPath, outPath):
    file_list = os.listdir(inPath)
    inpatientNum = set()
    for i in range(len(file_list)):
        if 'ZY' in file_list[i][0:2]:
            continue
        oldFileName = file_list[i][0:10]
        
        index = file_list[i].find('_')  # 第一次出现的位置
        index2 = file_list[i].find('_', index + 1)  # 第二次出现的位置
        tep = file_list[i][11:index2]
        if len(tep) > 1:
            inpatientNum.add("ZY" + tep + oldFileName)
        else:
            inpatientNum.add("ZY0" + tep + oldFileName)
            
    # 创建文件
    for j in inpatientNum:
        isExists = os.path.exists(outPath + '/' + j)
        if not isExists:
            os.makedirs(outPath + '/' + j)
            print (outPath + '/' + j + ' 创建成功')
            
    # 移动文件到指定文件夹
    for i in range(len(file_list)):
        if 'ZY' in file_list[i][0:2]:
            continue
        oldFileName = file_list[i][0:10]
        
        index = file_list[i].find('_')  # 第一次出现的位置
        index2 = file_list[i].find('_', index + 1)  # 第二次出现的位置
        tep = file_list[i][11:index2]
        if len(tep) > 1:
            dirName = "ZY" + tep + oldFileName
        else:
            dirName = "ZY0" + tep + oldFileName
            
        shutil.move(inPath + '/' + file_list[i], outPath + '/' + dirName)
        print ('原始路径:' + inPath + '/' + file_list[i] + '\n目标路径:' + outPath + '/' + dirName + ' 移动成功')
    

if __name__ == '__main__':
    path = ''
    categorXMLtoFolders('E:\PythonNew\EMRProject\data/A', 'E:\PythonNew\EMRProject\data/A_1')
