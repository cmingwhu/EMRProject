import csv
import datetime

import numpy as np
from pandas import read_csv

if __name__ == '__main__':
    # 输出文件路径
    xcgoutfile = '../data/COVID-19/Li1.csv'
    iputfile = '../data/COVID-19/Lis.csv'
    list_file = []
    with open(iputfile, 'r', encoding='GBK') as csv_file:
        all_lines = csv.reader(csv_file)
        for one_line in all_lines:
            list_file.append(one_line)
        list_file.remove(list_file[0])
        arr_file = np.array(list_file)
    print(arr_file.shape)
    patientid = arr_file[:, 0]   # 第1列：病人ID
    projectOnlyNum = arr_file[:, 2]   # 第3列：检验唯一号
    projectname = arr_file[:, 7]    # 检验目的名称
    projectdate = arr_file[:, 8]    # 日期
    projectcontent = arr_file[:, 10]
    # 处理文件中null情况
    for i in range(len(projectname)):
        if projectname[i] == 'NULL':
            projectname[i] = projectname[i - 1]

    # 数据预处理
    NEW_projectcontent = []
    file = open(xcgoutfile, "w", encoding='UTF-8')
    for m in range(len(projectname)):
        if '血常规' in projectname[m]:
            NEW_projectcontent.append(patientid[m] + ',' + projectOnlyNum[m] + ',' + projectdate[m] + ',"'
                                      + projectcontent[m] + '"\n')
        if '血气' in projectname[m]:
            NEW_projectcontent.append(patientid[m] + ',' + projectOnlyNum[m] + ',' + projectdate[m] + ',"'
                                      + projectcontent[m] + '"\n')
        if '肾功' in projectname[m]:
            NEW_projectcontent.append(patientid[m] + ',' + projectOnlyNum[m] + ',' + projectdate[m] + ',"'
                                      + projectcontent[m] + '"\n')
        if '肝功' in projectname[m]:
            NEW_projectcontent.append(patientid[m] + ',' + projectOnlyNum[m] + ',' + projectdate[m] + ',"'
                                      + projectcontent[m] + '"\n')
        if '心肌标志物'in projectname[m]:
            NEW_projectcontent.append(patientid[m] + ',' + projectOnlyNum[m] + ',' + projectdate[m] + ',"'
                                      + projectcontent[m] + '"\n')
        if '血凝' in projectname[m]:
            NEW_projectcontent.append(patientid[m] + ',' + projectOnlyNum[m] + ',' + projectdate[m] + ',"'
                                      + projectcontent[m] + '"\n')
        if '病毒全套' in projectname[m]:
            NEW_projectcontent.append(patientid[m] + ',' + projectOnlyNum[m] + ',' + projectdate[m] + ',"'
                                      + projectcontent[m] + '"\n')
        if len(projectname[m]) == 0:
            NEW_projectcontent.append(patientid[m] + ',' + projectOnlyNum[m] + ',' + projectdate[m] + ',"'
                                      + projectcontent[m] + '"\n')
    NEW_projectcontent = list(set(NEW_projectcontent))
    for yy in range(len(NEW_projectcontent)):
        file.write(NEW_projectcontent[yy])
        print('------------------------>')
    print('excel_txt:End')
