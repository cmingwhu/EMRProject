import csv
import numpy as np

'''
    血常规各指标 提取
'''

if __name__ == '__main__':
    # 输出文件路径
    xcgoutfile = '../data/COVID-19/Li1-XJBZW.csv'
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

    xcgtitle = ['patientid', 'data', 'N端脑纳肽前体', '肌酸激酶同工酶(质量法)', '肌红蛋白','超敏肌钙蛋白T']

    title_dic = {'patientid': '', 'data': '', 'N端脑纳肽前体': '', '肌酸激酶同工酶(质量法)': '', '肌红蛋白': '', '超敏肌钙蛋白T': ''}
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
            if 'N端脑纳肽前体' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['N端脑纳肽前体'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if '肌酸激酶同工酶' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['肌酸激酶同工酶(质量法)'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if '肌红蛋白' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['肌红蛋白'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if '超敏肌钙蛋白T' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                xwrite_flag = True
                title_dic['超敏肌钙蛋白T'] = wbc[2]

        if write_flag is True:
            for key, value in title_dic.items():
                file.write(value)
                file.write(',')
            file.write('\n')  # 注意转换后文件最后一行空白需要删除
            write_flag = False

        for key in title_dic.keys():
            title_dic[key] = ''
    print('excel_txt:End')

