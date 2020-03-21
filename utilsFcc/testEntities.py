# encodeing:utf-8
'''
@author:  Ming Cheng  
@Email: fccchengm@zzu.edu.cn
@time: 2018/11/15

@ 计算手术记录数据集中是否每个实体是否均足够，>60
'''
import os
import re
import string
import xml.dom.minidom
from _overlapped import NULL
from _ast import In


# read files
def readfile(filepath):
    file_list = os.listdir(filepath)
    
    ascites = 0     # 腹水 1
    bloodTrans = 0  # 输血 2
    bleeding = 0    # 失血 3
    sizes    = 0    # 大小 4
    position = 0    # 位置 5
    activities = 0  # 活动 6
    touch    = 0    # 肿块是否可触及 7
    nodules  = 0    # 结节 8
    serous   = 0    # 浆膜 9
    invasion = 0    # 侵及 10
    lymphNode = 0   # 肿大淋巴结 11
    gastricWall = 0 # 胃壁 12
    hard = 0        # 质硬
    laparoscopy = 0 # 腹腔镜
    operat = 0      # 手术名称
    metastatic = 0  # 转移
    allEnt = 0      # 包含所有

    
    for j in range(len(file_list)):
        detailPath = filepath+'/'+file_list[j]
#         print('# 遍历第 '+str(j) +'个手术记录：' + detailPath)
        f = open(detailPath, mode='r', encoding='UTF-8')
        content = f.read()       
#         print(content[0:15])
        if '腹水' or '积液' in content:
            ascites = ascites + 1  
#         if '腹水' in content:
#             ascites = ascites + 1       
        if '输血' in content:
            bloodTrans = bloodTrans + 1
#             print (detailPath)
        if '血浆' in content:
            bloodTrans = bloodTrans + 1
#             print (detailPath)        
        if '失血' in content:
            bleeding = bleeding + 1
#             print (detailPath)
        if '出血' in content:
            bleeding = bleeding + 1
#             print (detailPath)
        if '大小' in content:
            sizes = sizes + 1 
        if '活动' in content:
            activities = activities + 1 
        if '触及' in content:
            touch = touch + 1
        if '结节' in content:
            nodules = nodules + 1
        if '侵及' in content:
            invasion = invasion + 1
        if '侵犯' in content:
            invasion = invasion + 1
        if '肿大淋巴结' in content:
            lymphNode = lymphNode + 1
        if '浆膜' in content:
            serous = serous + 1
        if '胃壁' in content:
            gastricWall = gastricWall + 1    
        if '质硬' in content:
            hard = hard + 1   
        if '腹腔镜' in content:
            laparoscopy = laparoscopy + 1   
#         if '术' in content:
#             operat = operat + 1   
        if '转移' in content:
            metastatic = metastatic + 1  
        
        operat = operat + content.count('术' )
        
        f.close
        
        
        allEnt = ascites + bloodTrans + bleeding + sizes + activities + touch + nodules + serous + invasion \
                + lymphNode + serous + gastricWall + hard + laparoscopy +operat+metastatic
         
    print('腹水：' + str(ascites) +'\n'+'输血：' + str(bloodTrans) +'\n'+'失血：' + str(bleeding) +'\n'+'大小：' + str(sizes) +'\n'+'活动：' + str(activities) +'\n'
          +'触及：' + str(touch) +'\n'+'结节：' + str(nodules) +'\n'+'浆膜：' + str(serous) +'\n'+'侵及：' + str(invasion) +'\n'+'淋巴结：' + str(lymphNode) +'\n'
          +'浆膜：' + str(serous) +'\n'+'胃壁：' + str(gastricWall)+'\n'+'质硬：' + str(hard)+'\n'+'腹腔镜：' + str(laparoscopy)+'\n'+'术：' + str(operat)+'\n'
          +'转移：' + str(metastatic)+'\n'+'总计：' + str(allEnt))

def modfile(filepath,writePath):
    file_list = os.listdir(filepath)
    for j in range(len(file_list)):
        detailPath = filepath+'/'+file_list[j]
        writePa = writePath+'/'+file_list[j]
        print('# 遍历：' + detailPath)
        f = open(detailPath, mode='r', encoding='UTF-8')
        lines = f.readlines()#读取全部内容  
        i = 0
        str =''
        for line in lines:         
            if line != '' and i != 0:
                str = str+line
            i = i+1
                       
        newFile = open(writePa,'w', encoding='utf-8')
        newFile.write(str)  
        newFile.close()
        print(file_list[j]+'.txt已生成') 
    
    
    
def modfileNR(filepath,writePath):   
    file_list = os.listdir(filepath)
    for j in range(len(file_list)):
        detailPath = filepath+'/'+file_list[j]
        writePa = writePath+'/'+file_list[j]
#         print('# 遍历：' + detailPath)
        f = open(detailPath, mode='r', encoding='UTF-8')
        lines = f.readlines()#读取全部内容  
        ss = ''.join(lines)
        f.close()
        try:
            nPos  = ss.index('肠粘连松解术')
            ePos = ss.index('水冲洗')            
            str1 = ss[0:nPos]
            str2 = ss[ePos:]
#             eePos  = ss.index('5.')
#             str2 ='3'+ ss[ePos+1:eePos]
#             str3 ='4'+ ss[eePos+1:]

            strr = str1+str2
#             strr = strr + str3
        
            newFile = open(writePa,'w', encoding='utf-8')
            newFile.write(strr)  
            newFile.close()
            os.remove(detailPath)
#             print(file_list[j]+'.txt已生成')         
        except:
            print(detailPath)
       
#             print ("不存在3.温盐水冲洗腹腔")
#             print ("不存在7.温盐水冲洗腹腔")
        
def modfileSM(wsmfilepath,smfilepath,writePath):   
    file_list = os.listdir(wsmfilepath)
    for j in range(len(file_list)):
        detailPath = wsmfilepath+'/'+file_list[j]
        writePa = writePath+'/'+file_list[j]   
        f = open(detailPath, mode='r', encoding='UTF-8')
        lines = f.readlines()#读取全部内容  
        str = ''.join(lines)
        f.close()
#         if '决定行上述术式' in str:
#         detailPath1 = smfilepath+'/'+file_list[j]  
#         f1 = open(detailPath1, mode='r', encoding='UTF-8')
#         line =  f1.readlines()
#         f1.close()
#         ss = line[0]
#         ss = '行'+ss.strip()
        
        str1 = str.replace('38.', '7.')
#         str2 = str1.replace('4.', '8.')
        newFile = open(writePa,'w', encoding='utf-8')
        newFile.write(str1)  
        newFile.close()
        os.remove(detailPath)
        print(detailPath)

if __name__ == '__main__':
    print('2018年11月15日  程铭  测试数据集中每一个实体个数')
    readfile('E:\PythonNew\EMRProject\data\Gastriced_Operation')
    
    # 删除手术名称
#     modfile('E:\PythonNew\EMRProject\data\Gastriced_Operation','E:\PythonNew\EMRProject\data\Gastriced_Operation_1')
#     modfileSM('E:\PythonNew\EMRProject\data\Gastriced_Operation_2','E:\PythonNew\EMRProject\data\Gastriced_Operation','E:\PythonNew\EMRProject\data\Gastriced_Operation_3')


