import csv
import numpy as np

'''
    血常规各指标 提取
'''

if __name__ == '__main__':
    # 输出文件路径
    xcgoutfile = '../data/COVID-19/Li1-BDQT.csv'
    iputfile = '../data/COVID-19/Li1.csv'
    list_file = []
    with open(iputfile, 'r', encoding='GBK') as csv_file:
        all_lines = csv.reader(csv_file)
        for one_line in all_lines:
            list_file.append(one_line)
        arr_file = np.array(list_file)
        print(arr_file.shape)
        patientid = arr_file[:, 0]   # 第1列：病人ID
        patientdata = arr_file[:, 2]
        projectcontent = arr_file[:, 3]
    # 将数据以天为单位写入TXT文件中
    file = open(xcgoutfile, "w", encoding='GBK')

    title = ['patientid', 'data', 'xIgM', 'CVB-IgG',  'CVB-IgM', 'EB-IgG', 'EB-IgM', 'MEV-IgG', 'MEV-IgM','RV-IgM', 'CP-IgM',
                'MP-IgM', 'CMV-IgG', 'CMV-IgM', 'HSV1-IgM', 'HSV2-IgM', 'VZV-IgM', 'ECHO-IgM']
    title_dic = {'patientid': '', 'data': '', 'xIgM': '', 'CVB-IgG': '', 'CVB-IgM': '', 'EB-IgG': '',
                 'EB-IgM': '', 'MEV-IgG': '', 'MEV-IgM': '', 'RV-IgM': '', 'CP-IgM': '', 'MP-IgM': '',
                 'CMV-IgG': '', 'CMV-IgM': '','HSV1-IgM':'', 'HSV2-IgM': '', 'VZV-IgM': '', 'ECHO-IgM': ''}
    write_flag = False

    for y in range(len(title)):
        file.write(title[y])
        file.write(',')
    file.write('\n')   # 注意转换后
    print(len(patientid))
    for n in range(len(patientid)):
        title_dic['patientid'] = patientid[n].strip()
        title_dic['data'] = patientdata[n].strip()
        xuechangguilist = projectcontent[n].split(",")
        for m in range(len(xuechangguilist)):
            if 'xIgM' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['xIgM'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'CVB-IgG' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['CVB-IgG'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'CVB-IgM' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['CVB-IgM'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'EB-IgG' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['EB-IgG'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'EB-IgM' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['EB-IgM'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'MEV-IgG' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['MEV-IgG'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'MEV-IgM' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['MEV-IgM'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'RV-IgM' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['RV-IgM'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'CP-IgM' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['CP-IgM'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'MP-IgM' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['MP-IgM'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'CMV-IgG' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['CMV-IgG'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'CMV-IgM' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['CMV-IgM'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'HSV1-IgM' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['HSV1-IgM'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'HSV2-IgM' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['HSV2-IgM'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'VZV-IgM' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['VZV-IgM'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'ECHO-IgM' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['ECHO-IgM'] = wbc[2]

        if write_flag is True:
            for key, value in title_dic.items():
                file.write(value)
                file.write(',')
            file.write('\n')  # 注意转换后文件最后一行空白需要删除
            write_flag = False

        for key in title_dic.keys():
            title_dic[key] = ''

    print('excel_txt:End')

