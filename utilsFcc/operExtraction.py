#!/usr/bin/env python
# encodeing:utf-8
'''
@ author: GeXiaowei 
@ Email: xwge@foxmail.com
@ Last modified: 2018/11/06 by Ming Cheng 
@ time: 2018/10/25

@提取患者: 基本信息+病例特点+初步诊断+手术记录+诊疗经过+出院诊断
'''

import os
import re
import xml.dom.minidom
from _overlapped import NULL
from _cffi_backend import buffer

# 入院记录
def xmlParsing_admissionRecord(filepath):
    admissionRecordList = []
    patientName = ''
    fieldelemTitile = '[1]基础信息'
#     admissionRecordList.append(fieldelemTitile)
    dom = xml.dom.minidom.parse(filepath)
    fieldelems = dom.getElementsByTagName("fieldelem")
    for fieldelem in fieldelems:
        if fieldelem.hasAttribute("name"):
            fieldelemName = fieldelem.getAttribute("name")
            if(fieldelemName == '姓名'):
                patientName = fieldelem.childNodes[0].data
            if(fieldelemName == '性别'):
                fieldelemText = fieldelemName +'：'+fieldelem.childNodes[0].data
                fieldelemText = fieldelemText.strip('\n')
                admissionRecordList.append(fieldelemText)
            if(fieldelemName == '年龄'):
                fieldelemText = fieldelemName+'：'+fieldelem.childNodes[0].data
                fieldelemText = fieldelemText.strip('\n')
                admissionRecordList.append(fieldelemText)
            if(fieldelemName == '民族'):
                fieldelemText = fieldelemName+'：'+fieldelem.childNodes[0].data
                fieldelemText = fieldelemText.strip('\n')
                admissionRecordList.append(fieldelemText)           
            if(fieldelemName == '婚姻状况'):
                fieldelemText = fieldelemName+'：'+fieldelem.childNodes[0].data
                fieldelemText = fieldelemText.strip('\n')
                admissionRecordList.append(fieldelemText)
            if(fieldelemName == '住址'):
                fieldelemText = fieldelemName+'：'+fieldelem.childNodes[0].data
                fieldelemText = fieldelemText.strip('\n')
                pat1 = re.compile('[^(.+?)]{0,}\县')
                pat2 = re.compile('[^(.+?)]{0,}\区')
                pat3 = re.compile('[^(.+?)]{0,}\市')
                res1 = pat1.findall(fieldelemText)
                res2 = pat2.findall(fieldelemText)
                res3 = pat3.findall(fieldelemText)
                if pat1.findall(fieldelemText):
                    admissionRecordList.append(''.join(res1))
                elif pat2.findall(fieldelemText):
                    admissionRecordList.append(''.join(res2))
                elif pat3.findall(fieldelemText):
                    admissionRecordList.append(''.join(res3))              
            if(fieldelemName == '职业'):
                fieldelemText = fieldelemName+'：'+fieldelem.childNodes[0].data
                fieldelemText = fieldelemText.strip('\n')
                admissionRecordList.append(fieldelemText)
    tempCourses = []
    sections = dom.getElementsByTagName("section")
    for section in sections:
        if section.hasAttribute("name"):
            sectionName = section.getAttribute("name")
            if(sectionName == '主诉'):
                for i in range(len(section.getElementsByTagName('text'))):                   
                    if '主诉：' in section.getElementsByTagName('text')[i].childNodes[0].data:
                        continue
                    else: 
                        tempCourses.append(section.getElementsByTagName('text')[i].childNodes[0].data.replace('\t','').replace('\n','').replace(' ','').replace(',','，').replace(':','：'))                   
                admissionRecordList.append(''.join(tempCourses))                               
    str = '，'.join(admissionRecordList)
    admissionRecordList.clear()
    admissionRecordList.append(fieldelemTitile)
    admissionRecordList.append(str)
    return patientName, admissionRecordList

# 病程记录
def xmlParsing_courseOfDisease(filepath):
    courseOfDiseaseList = []
    tempCourses = []
    tempCourses1 = []
    dom = xml.dom.minidom.parse(filepath)
    sections = dom.getElementsByTagName("section")  
    for section in sections:
        if section.hasAttribute("name"):
            sectionName = section.getAttribute("name")
            if(sectionName == '病例特点'):
                courseOfDiseaseList.append('[2]'+sectionName)
                for i in range(len(section.getElementsByTagName('text'))):                   
                    if '本病例特点如下：' in section.getElementsByTagName('text')[i].childNodes[0].data:
                        continue
                    else: 
                        tempCourses.append(section.getElementsByTagName('text')[i].childNodes[0].data.replace('\t','').replace('\n','').replace(' ','').replace(',','，').replace(':','：'))                                                       
                courseOfDiseaseList.append(''.join(tempCourses)) 
            if(sectionName == '初步诊断'):
                courseOfDiseaseList.append('[3]'+sectionName)
                for i in range(1,len(section.getElementsByTagName('text'))):
                    stri = section.getElementsByTagName('text')[i].childNodes[0].data.replace('\t','').replace('\n','').replace(' ','').replace('，','.').replace(':','：')
                    stri = stri.replace('2',' 2').replace('3',' 3').replace('4',' 4').replace('5',' 5').replace('6',' 6').replace('7',' 7').replace('8',' 8').replace('9',' 9')
                    tempCourses1.append(stri)
                courseOfDiseaseList.append(''.join(tempCourses1))
    return courseOfDiseaseList

# 手术记录
def xmlParsing_operationRecord(filepath):
    operationRecordList = []
    word1 = '手术名称：</text><text>'
    word2 = '</text><text>施术者'
    word3 = '</text><text>手术者'
    word11 = '手术经过：</section>'
    word12 = '<section name=\"病程签名\"'  
    f = open(filepath,'r',encoding='UTF-8')
    buff = f.read()
    buff = buff.replace('\n','')
    pat1 = re.compile(word1+'(.*?)'+word2)
    pat2 = re.compile(word1+'(.*?)'+word3)
    pat3 = re.compile(word11+'(.*?)'+word12)
    result3 = pat3.findall(buff)
    result1 = pat1.findall(buff)
    result2 = pat2.findall(buff)    
    # 手术名称
#     if len(result1):
# #         results1 = '[4]手术名称\n'+result1[0]
#         results1 = result1[0]
#         results1 = re.sub('</text><text>','',results1).replace(',','，').replace(':','：')
#         results1.strip()
#         operationRecordList.append(results1); 
#     elif len(result2):
# #         results2 = '[4]手术名称\n'+result2[0]      
#         results2 = result2[0]
#         results2 = re.sub('</text><text>','',results2).replace(',','，').replace(':','：')
#         results2.strip()
#         operationRecordList.append(results2);
    if len(result3):
        result3 = re.sub('</text><text>','',result3[0]).replace(',','，').replace(':','：')
        result3 = re.sub('</text>','',result3)
        result3 = re.sub('<text>','',result3)
        words = result3.split()
        result3 = ''.join(words)  
#         results3 = '[5]手术经过\n'+result3  
        results3 = result3  
        results3 = re.sub('手术医师签名：', '', results3)
        operationRecordList.append(results3);
        return operationRecordList
          

               
def xmlParsing_dischargeRecord_zl(filepath): 
    word1 = '诊疗经过：</fieldelem><text>'
    word2 = '</text><fieldelem name=\"出院诊断\"'
    f = open(filepath,'r',encoding='UTF-8')
    buff = f.read()
    buff = buff.replace('\n','')
    pat = re.compile(word1+'(.*?)'+word2)
    result = pat.findall(buff)
    if len(result):
        results = '[6]诊疗经过\n'+result[0]
        results = re.sub('</text><text>','',results).replace(',','，').replace(':','：')
        results.strip()
        return results
    
    
def xmlParsing_dischargeRecord_cy(filepath):
    word1 = '出院诊断：</fieldelem><text>'
    word2 = '</text><fieldelem name=\"出院医嘱\"'
    f = open(filepath,'r',encoding='UTF-8')
    buff = f.read()
    buff = buff.replace('\n','')
    pat = re.compile(word1+'(.*?)'+word2)
    result = pat.findall(buff)
    if len(result):
        results = '[7]出院诊断\n'+result[0]
        results = re.sub('</text><text>','',results).replace(',','，')
        results.strip()
        return results
        
    
def xmlParsing_dischargeRecord(filepath):
    dischargeRecordList = []
    lstr = xmlParsing_dischargeRecord_cy(filepath)
    if  lstr != None:
        if '</text><fieldelem' not in lstr:
            dischargeRecordList.append(xmlParsing_dischargeRecord_zl(filepath))
            dischargeRecordList.append(xmlParsing_dischargeRecord_cy(filepath))
            return dischargeRecordList

def xmlParsing(file_list,old_dir_list):
    xmlParsing_all = ['a','b','c','d']
    for j in range(len(file_list)):
        detailPath = old_dir_list+'/'+file_list[j]
        if '入院记录' in file_list[j]:
            patientName, admissionRecordList = xmlParsing_admissionRecord(detailPath)
            xmlParsing_all[0] = admissionRecordList
        elif '病程记录' in file_list[j]:
            courseOfDiseaseList = xmlParsing_courseOfDisease(detailPath)
            xmlParsing_all[1] = courseOfDiseaseList
        elif '手术记录' in file_list[j]:
            operationRecordList = xmlParsing_operationRecord(detailPath)     
            if operationRecordList  != None:         
                xmlParsing_all[2] = operationRecordList
        elif '其他记录' in file_list[j]:
            dischargeRecordList = xmlParsing_dischargeRecord(detailPath)
            if dischargeRecordList != None:
                xmlParsing_all[3] = dischargeRecordList
    # 数据修订
    for i in range(len(xmlParsing_all)):
        for m in range(len(xmlParsing_all[2])):
            strr = xmlParsing_all[2][m]
            xmlParsing_all[2][m] = xmlParsing_all[2][m].replace(patientName,'').replace('CA','癌') # 'ca' 替换成 ‘癌’
        
    return xmlParsing_all

#合并某个人的所有病历为一个txt文件
def dofile(filepath,refilepath,secretKey):
    dir_list = os.listdir(filepath)
    for i in range(len(dir_list)):
        old_dir_list = os.path.join(filepath,dir_list[i]) #获取某一个的文件路径
        if os.path.isdir(old_dir_list):    #判断某一个是否为目录
            file_list = os.listdir(old_dir_list)
            xmlparsing_all = xmlParsing(file_list,old_dir_list)           
            oldFileName = int(re.sub('\D','',dir_list[i]))
#             secretFileName = str(oldFileName*secretKey+secretKey*2)

            secretFileName = str(oldFileName)
            old_dir_list = refilepath + '\CG' +secretFileName    
            if secretFileName == '10002459377' :
                print(' ')                
            newFile = open(old_dir_list+'.txt','w', encoding='utf-8')  
            
            # 存所有数据         
#             for j in range(len(xmlparsing_all)):                
#                 for m in range(len(xmlparsing_all[j])):
#                     newFile.write(xmlparsing_all[j][m]+'\n')
            
            # 只存手术数据
            for m in range(len(xmlparsing_all[2])):
                newFile.write(xmlparsing_all[2][m]+'\n')
            
            newFile.close()
            print(old_dir_list+'.txt已生成')
    print ('##########病历数据预处理结束，共处理病历：'+str(len(dir_list))+'份！##########')     
               
 # 检测患者病历均包含手术记录                   
def find_Operative_record(filepath): 
    dir_list = os.listdir(filepath)
    for i in range(len(dir_list)):
        old_dir_list = os.path.join(filepath,dir_list[i]) #获取某一个的文件路径
        if os.path.isdir(old_dir_list): 
            file_list = os.listdir(old_dir_list)
            k = 0
            for j in range(len(file_list)):
                k += 1
                if '手术记录' in file_list[j]:
                    break
            if k == len(file_list):
                print(old_dir_list)
 
 
def find_(filepath):
    dir_list = os.listdir(filepath)
    for i in range(len(dir_list)):
        old_dir_list = os.path.join(filepath,dir_list[i]) #获取某一个的文件路径
        f = open(old_dir_list,'r',encoding='UTF-8')
        buff = f.read()
        if '早期' in buff:
            print (old_dir_list)
 
 
if __name__=='__main__':
    print('2018年10月27日  葛晓伟  病历信息抽取')
    orfilepath = 'E:/PythonNew/EMRProject/data/A_1'
    refilepath = 'E:/PythonNew/EMRProject/data/A_2'
    secretKey = 224 #脱敏密钥
    dofile(orfilepath,refilepath,secretKey)
    
#     find_('E:\PythonNew\EMRProject\data\Gastriced')
    
    

#     xmlParsing_admissionRecord('E:\PythonNew\EMRProject\data\orGastric\ZY010002533136/0002533136_1_0002533136_入院记录00010001.xml')




