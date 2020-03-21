#!/usr/bin/env python
# encodeing:utf-8
'''
@author: GeXiaowei
@contact: xwge@foxmail.com
@time: 2018/10/25
@提取患着 基本信息+病例特点+初步诊断+鉴别诊断+诊疗经过+出院诊断
'''

import os
import re
import xml.dom.minidom


# 入院记录
def xmlParsing_admissionRecord(filepath):
    admissionRecordList = []
    fieldelemTitile = '[1]基本信息'
    admissionRecordList.append(fieldelemTitile)
    dom = xml.dom.minidom.parse(filepath)
    fieldelems = dom.getElementsByTagName("fieldelem")
    for fieldelem in fieldelems:
        if fieldelem.hasAttribute("name"):
            fieldelemName = fieldelem.getAttribute("name")
            if(fieldelemName == '性别'):
                fieldelemText = fieldelemName + fieldelem.childNodes[0].data
                fieldelemText = re.sub('>', ':', fieldelemText)
                admissionRecordList.append(fieldelemText)
            if(fieldelemName == '年龄'):
                fieldelemText = fieldelemName + fieldelem.childNodes[0].data
                fieldelemText = re.sub('>', ':', fieldelemText)
                admissionRecordList.append(fieldelemText)
            if(fieldelemName == '民族'):
                fieldelemText = fieldelemName + fieldelem.childNodes[0].data
                fieldelemText = re.sub('>', ':', fieldelemText)
                admissionRecordList.append(fieldelemText)
            if(fieldelemName == '婚姻状况'):
                fieldelemText = fieldelemName + fieldelem.childNodes[0].data
                fieldelemText = re.sub('>', ':', fieldelemText)
                admissionRecordList.append(fieldelemText)
            if(fieldelemName == '职业'):
                fieldelemText = fieldelemName + fieldelem.childNodes[0].data
                fieldelemText = re.sub('>', ':', fieldelemText)
                admissionRecordList.append(fieldelemText)
    return admissionRecordList


def xmlParsing_courseOfDisease(filepath):
    courseOfDiseaseList = []
    dom = xml.dom.minidom.parse(filepath)
    sections = dom.getElementsByTagName("section")  
    for section in sections:
        if section.hasAttribute("name"):
            sectionName = section.getAttribute("name")
            if(sectionName == '病例特点'):
                courseOfDiseaseList.append('[2]' + sectionName)
                for i in range(len(section.getElementsByTagName('text'))):
                    courseOfDiseaseList.append(section.getElementsByTagName('text')[i].childNodes[0].data)
            if(sectionName == '初步诊断'):
                courseOfDiseaseList.append('[3]' + sectionName)
                for i in range(1, len(section.getElementsByTagName('text'))):
                    courseOfDisease = section.getElementsByTagName('text')[i].childNodes[0].data
                    courseOfDiseaseList.append(courseOfDisease)
            if(sectionName == '鉴别诊断'):
                courseOfDiseaseList.append('[4]' + sectionName)
                for i in range(1, len(section.getElementsByTagName('text'))):
                    courseOfDiseaseList.append(section.getElementsByTagName('text')[i].childNodes[0].data)
    return courseOfDiseaseList

                
def xmlParsing_dischargeRecord_zl(filepath): 
    word1 = '诊疗经过：</fieldelem><text>'
    word2 = '</text><fieldelem name=\"出院诊断\"'
    f = open(filepath, 'r', encoding='UTF-8')
    buff = f.read()
    buff = buff.replace('\n', '')
    pat = re.compile(word1 + '(.*?)' + word2)
    result = pat.findall(buff)
    if len(result):
        results = '[5]诊疗经过\n' + result[0]
        results = re.sub('</text><text>', '', results)
        return results

    
def xmlParsing_dischargeRecord_cy(filepath):
    word1 = '出院诊断：</fieldelem><text>'
    word2 = '</text><fieldelem name=\"出院医嘱\"'
    f = open(filepath, 'r', encoding='UTF-8')
    buff = f.read()
    buff = buff.replace('\n', '')
    pat = re.compile(word1 + '(.*?)' + word2)
    result = pat.findall(buff)
    if len(result):
        results = '[6]出院诊断\n' + result[0]
        results = re.sub('</text><text>', '', results)
        return results
        
    
def xmlParsing_dischargeRecord(filepath):
    dischargeRecordList = []
    if xmlParsing_dischargeRecord_cy(filepath) != None:
        if '</text><fieldelem' not in xmlParsing_dischargeRecord_cy(filepath):
            dischargeRecordList.append(xmlParsing_dischargeRecord_zl(filepath))
            dischargeRecordList.append(xmlParsing_dischargeRecord_cy(filepath))
            return dischargeRecordList


def xmlParsing(file_list, old_dir_list):
    xmlParsing_all = ['a', 'b', 'c']
    for j in range(len(file_list)):
        detailPath = old_dir_list + '/' + file_list[j]
        if '入院记录' in file_list[j]:
            admissionRecordList = xmlParsing_admissionRecord(detailPath)
            xmlParsing_all[0] = admissionRecordList
        elif '病程记录' in file_list[j]:
            courseOfDiseaseList = xmlParsing_courseOfDisease(detailPath)
            xmlParsing_all[1] = courseOfDiseaseList
        elif '其他记录' in file_list[j]:
            dischargeRecordList = xmlParsing_dischargeRecord(detailPath)
            if xmlParsing_dischargeRecord(detailPath) != None:
                xmlParsing_all[2] = dischargeRecordList
    return xmlParsing_all


# 合并某个人的所有病历为一个txt文件
def dofile(filepath, secretKey):
    dir_list = os.listdir(filepath)
    for i in range(len(dir_list)):
        old_dir_list = os.path.join(filepath, dir_list[i])  # 获取某一个的文件路径
        if os.path.isdir(old_dir_list):  # 判断某一个是否为目录
            file_list = os.listdir(old_dir_list)
            xmlparsing_all = xmlParsing(file_list, old_dir_list)
            
            oldFileName = int(re.sub('\D', '', dir_list[i]))
            secretFileName = str(oldFileName * secretKey + secretKey * 2)
            old_dir_list = filepath + 'CG' + secretFileName
            
            newFile = open(old_dir_list + '.txt', 'w')
            
            for j in range(len(xmlparsing_all)):                
                for m in range(len(xmlparsing_all[j])):
                    newFile.write(xmlparsing_all[j][m] + '\n')
            newFile.close()
            print(old_dir_list + '.txt已生成')

                    
if __name__ == '__main__':
    filepath = 'E:/PythonNew/EMRProject/data/Gastric'
    secretKey = 224  # 脱敏密钥
    dofile(filepath, secretKey)
    # xmlParsing(filepath)
