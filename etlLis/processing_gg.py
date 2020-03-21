import csv
import numpy as np

'''
    血常规各指标 提取
'''

if __name__ == '__main__':
    # 输出文件路径
    xcgoutfile = '../data/COVID-19/Li1-GG.csv'
    iputfile = '../data/COVID-19/Li1.csv'
    list_file = []
    with open(iputfile, 'r', encoding='gbk') as csv_file:
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

    xcgtitle = ['patientid', 'data', '谷丙转氨酶', '谷草转氨酶', '白蛋白', '球蛋白', '总胆红素', '间接胆红素','直接胆红素']
    title_dic = {'patientid': '', 'data': '', '谷丙转氨酶': '', '谷草转氨酶': '', '白蛋白': '', '球蛋白': '',
                 '总胆红素': '', '间接胆红素': '','直接胆红素':''}
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
            if '谷丙转氨酶' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['谷丙转氨酶'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if '谷草转氨酶' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['谷草转氨酶'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'ALB:白蛋白' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['白蛋白'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'GLOB:球蛋白' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['球蛋白'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if '总胆红素' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['总胆红素'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if '间接胆红素' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['间接胆红素'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if '直接胆红素' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['直接胆红素'] = wbc[2]

        if write_flag is True:
            for key, value in title_dic.items():
                file.write(value)
                file.write(',')
            file.write('\n')  # 注意转换后文件最后一行空白需要删除
            write_flag = False

        for key in title_dic.keys():
            title_dic[key] = ''
    print('excel_txt:End')

