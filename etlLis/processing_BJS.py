import csv
import numpy as np

'''
    血常规各指标 提取
'''

if __name__ == '__main__':
    # 输出文件路径
    xcgoutfile = '../data/COVID-19/Li1-BJS.csv'
    iputfile = '../data/COVID-19/Li1.csv'
    list_file = []
    with open(iputfile, 'r', encoding='utf8') as csv_file:
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

    xcgtitle = ['patientid', 'data', '白介素2', '白介素4', '白介素6', '白介素10', '干扰素-γ', '肿瘤坏死因子α']
    title_dic = {'patientid': '', 'data': '', '白介素2': '', '白介素4': '', '白介素6': '', '白介素10': '',
                 '干扰素-γ': '', '肿瘤坏死因子α': ''}
    write_flag = False

    for y in range(len(xcgtitle)):
        file.write(xcgtitle[y])
        file.write(',')
    file.write('\n')   # 注意转换后
    print(len(patientid))
    for n in range(len(patientid)):
        title_dic['patientid'] = patientid[n].strip()
        title_dic['data'] = patientdata[n].strip()
        xuechangguilist = projectcontent[n].split(",")
        for m in range(len(xuechangguilist)):
            if 'IL-2' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['白介素2'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'IL-4' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['白介素4'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'IL-6' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['白介素6'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'IL-10' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['白介素10'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'IFN-γ' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['干扰素-γ'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'TNF-α' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['肿瘤坏死因子α'] = wbc[2]


        if write_flag is True:
            for key, value in title_dic.items():
                file.write(value)
                file.write(',')
            file.write('\n')  # 注意转换后文件最后一行空白需要删除
            write_flag = False

        for key in title_dic.keys():
            title_dic[key] = ''
    print('excel_txt:End')

