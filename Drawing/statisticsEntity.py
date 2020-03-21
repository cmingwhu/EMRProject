'''
Created on 2019年4月17日

@author: cmingwhu
统计CCKS2018 实体个数
'''

import os
import re
import string
import xml.dom.minidom
from _overlapped import NULL
from _ast import In
from docutils.nodes import Body
from grpc._cython.cygrpc import Operation

# CCKS2018
def readfile(filepath):
    file_list = os.listdir(filepath)
    
    body = 0     # 解剖部位 1
    operation = 0  # 手术 2
    drug = 0    # 药物 3
    indeSymptom    = 0    # 独立症状 4
    symptom = 0    # 症状描述 5
    allEnt = 0


    
    for j in range(len(file_list)):
        if 'txtoriginal' in file_list[j]:
            continue
        
        detailPath = filepath+'/'+file_list[j]
#         print('# 遍历第 '+str(j) +'入院记录：' + detailPath)
        f = open(detailPath, mode='r', encoding='UTF-8')
        content = f.read()      
        
        
        body = body+ content.count("解剖部位",0,len(content))
        operation = operation + content.count("手术",0,len(content))
        drug = drug+ content.count("药物",0,len(content))
        indeSymptom = indeSymptom + content.count("独立症状",0,len(content))
        symptom = symptom + content.count("症状描述",0,len(content))
         
                        
        f.close
        
        
    allEnt =body + operation + drug + indeSymptom + symptom       
         
    print('解剖部位：' + str(body) +'\n'+'手术：' + str(operation) +'\n'+'药物：' + str(drug) +'\n'+'独立症状：' + str(indeSymptom) +'\n'+'症状描述：' + str(symptom)+'\n'+'实体：' + str(allEnt))
    

# FCC-O
def readfile_FCC(filepath):
    file_list = os.listdir(filepath)
    
    body = 0     # 解剖部位 1
    operation = 0  # 手术 2
    drug = 0    # 药物 3
    tissues    = 0    # 组织结构 4
    pathological = 0  # 病变  5
    feature  = 0   # 症状表现
    allEnt = 0


    
    for j in range(len(file_list)):
        if 'oe' not in file_list[j]:
            continue
        
        detailPath = filepath+'/'+file_list[j]
#         print('# 遍历第 '+str(j) +'入院记录：' + detailPath)
        f = open(detailPath, mode='r', encoding='UTF-8')
        content = f.read()      
        
        
        body = body+ content.count("body",0,len(content))
        operation = operation + content.count("operation",0,len(content))
        drug = drug+ content.count("drug",0,len(content))
        tissues = tissues + content.count("tissues",0,len(content))
        pathological = pathological + content.count("pathological",0,len(content))
        feature = feature + content.count("feature",0,len(content))
        
         
                        
        f.close
        
        
    allEnt =body + operation + drug + tissues + pathological + feature       
         
    print('解剖部位：' + str(body) +'\n'+'手术：' + str(operation) +'\n'+'药物：' + str(drug) +'\n'+'组织结构：' + str(tissues) +'\n'+'病变：' + str(pathological)+'\n'+'特征表现：' + str(feature)+'\n'+'实体：' + str(allEnt))
    
    

if __name__ == '__main__':
    #readfile('E:\PythonNew\EMRProject\data/trainingset')
    readfile_FCC('E:\PythonNew\EMRProject\data/Gastriced_Operation_1_LM')
    