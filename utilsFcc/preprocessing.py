#!/usr/bin/env python
# encodeing:utf-8
'''
@author: GeXiaowei
@contact: xwge@foxmail.com
@time: 2018/10/25
@数据修订 
'''

import os
import re
import codecs
import linecache

from tempfile import _candidate_tempdir_list
from idlelib.iomenu import encoding


# 修正入院记录XML文件中的BUG，补'>'
def reviseBugs(filepath):
    # 列出文档
    dir_list = os.listdir(filepath)
    for i in range(len(dir_list)):
        old_dir_list = os.path.join(filepath, dir_list[i])  # 获取某一个的文件路径
        if os.path.isdir(old_dir_list):
            file_list = os.listdir(old_dir_list)
            for j in range(len(file_list)):
                if '入院记录' in file_list[j]:
                    detailPath = old_dir_list + '/' + file_list[j]
                    print('#修正入院记录XML文件中的BUG ' + detailPath)
                    f = open(detailPath, mode='r', encoding='UTF-8')
                    content = f.read()
                    # 文本方式读入
                    content = re.sub("code-system=\"\"", "code-system=\"\">", content)
                    content = re.sub("code-system=\"\">>", "code-system=\"\">", content)
                    # 替换encoding头        f.close()
                    f = open(detailPath, 'w')
                    # 写入       
                    f.write(content)
                    f.close()
                    f = codecs.open(detailPath, 'rb', 'mbcs')
                    # 二进制方式读入
                    text = f.read().encode("utf-8")
                    # 使用utf-8方式编码
                    f.close
                    f = open(detailPath, 'wb')
                    # 二进制方式写入
                    f.write(text)
                    f.close()
                
                                   

# 替换fieldelem为section（病程记录）                  
def conver_fieldelem_to_section(filepath):
    # 列出文档
    dir_list = os.listdir(filepath)
    for i in range(len(dir_list)):
        old_dir_list = os.path.join(filepath, dir_list[i])  # 获取某一个的文件路径
        if os.path.isdir(old_dir_list):
            file_list = os.listdir(old_dir_list)
            for j in range(len(file_list)):
                if '病程记录' in file_list[j]:
                    detailPath = old_dir_list + '/' + file_list[j]
                    print('将“病程记录XML”文件中的fieldelem转换为section ' + detailPath)
                    f = open(detailPath, mode='r', encoding='UTF-8')
                    content = f.read()
                    content = re.sub("fieldelem", "section", content)
                    f = open(detailPath, 'w')
                    # 写入       
                    f.write(content)
                    f.close()
                    f = codecs.open(detailPath, 'rb', 'mbcs')
                    # 二进制方式读入
                    text = f.read().encode("utf-8")
                    # 使用utf-8方式编码
                    f.close
                    f = open(detailPath, 'wb')
                    # 二进制方式写入
                    f.write(text)
                    f.close()
    print("'病程记录' 格式标准化结束！")
                
# “手术记录” 标准化描述(手术记录 -> 手术经过)
def operationStandardization(filepath):
    # 列出文档
    dir_list = os.listdir(filepath)
    for i in range(len(dir_list)):
        old_dir_list = os.path.join(filepath, dir_list[i])  # 获取某一个的文件路径
        if os.path.isdir(old_dir_list):
            file_list = os.listdir(old_dir_list)
            for j in range(len(file_list)):
                if '手术记录' in file_list[j]:
                    detailPath = old_dir_list + '/' + file_list[j]
                    print('将“手术记录”格式标准化: ' + detailPath)
                    f = open(detailPath, mode='r', encoding='UTF-8')
                    content = f.read()
                    content = re.sub("fieldelem", "section", content)
                    content = re.sub("手术记录：</section>", "手术经过：</section>", content)
                    f = open(detailPath, 'w')
                    # 写入       
                    f.write(content)
                    f.close()
                    f = codecs.open(detailPath, 'rb', 'mbcs')
                    # 二进制方式读入
                    text = f.read().encode("utf-8")
                    # 使用utf-8方式编码
                    f.close
                    f = open(detailPath, 'wb')
                    # 二进制方式写入
                    f.write(text)
                    f.close()              
    print("“手术记录” 格式标准化结束！")

      
# 转换一个人所有的病历文件为utf-8            
def convert_file_to_utf8(filepath):
    # 列出文档
    dir_list = os.listdir(filepath)
    for i in range(len(dir_list)):
        old_dir_list = os.path.join(filepath, dir_list[i])  # 获取某一个的文件路径
        if os.path.isdir(old_dir_list):  # 判断某一个是否为目录
            file_list = os.listdir(old_dir_list)
            for j in range(len(file_list)):
                detailPath = old_dir_list + '/' + file_list[j]
                print('#转换所有的病历文件为utf-8 ' + detailPath)                    
                try:
                    f = open(detailPath, 'r',encoding='utf-8')
                    content = f.read()  #文本方式读入                  
                    #替换encoding头
                    content = re.sub("GB2312", "UTF-8", content)
                    f.close()
                    f = open(detailPath, 'w')
                    #写入       
                    f.write(content)
                    f.close()
                    f = codecs.open(detailPath, 'rb', 'mbcs')
                    #二进制方式读入
                    text = f.read().encode("utf-8")
                    #使用utf-8方式编码
                    f.close
                    f = open(detailPath, 'wb')
                    #二进制方式写入
                    f.write(text)
                    f.close()
                except Exception as e:
                    f = open(detailPath, 'r',encoding='GB18030')
                    content = f.read()  #文本方式读入                    
                    #替换encoding头
                    content = re.sub("GB2312", "UTF-8", content)
                    f.close()
                    f = open(detailPath, 'w')
                    #写入       
                    f.write(content)
                    f.close()
                    f = codecs.open(detailPath, 'rb', 'mbcs')
                    #二进制方式读入
                    text = f.read().encode("utf-8")
                    #使用utf-8方式编码
                    f.close
                    f = open(detailPath, 'wb')
                    #二进制方式写入
                    f.write(text)
                    f.close()
    print("XML编码格式转换结束！")


def ReadFile_(filePath,encoding=""):
    with codecs.open(filePath,"r",encoding) as f:
        return f.read()

def WriteFile_(filePath,u,encoding=""):
    with codecs.open(filePath,"w",encoding) as f:
        #f.write(u.encode(encoding,errors="ignore"))
        f.write(u)

def UTF8_2_GBK(src,dst):
    content = ReadFile(src,encoding="utf-8")
    WriteFile(dst,content,encoding="gb2312")

def GBK_2_UTF8(src,dst):
    content = ReadFile_(src,encoding="gb2312")
    WriteFile_(dst,content,encoding="utf-8")

                
                
if __name__ == '__main__':
    print('2018年10月27日  葛晓伟  病历信息xml文件格式转换')
    filepath = 'E:\PythonNew\EMRProject\data\A_1'
       

    convert_file_to_utf8(filepath)
    conver_fieldelem_to_section(filepath)
    operationStandardization(filepath)
    reviseBugs(filepath)

    print('标准化结果！')
