import csv
import numpy as np

'''
    血常规各指标 提取
'''

if __name__ == '__main__':
    # 输出文件路径
    xcgoutfile = '../data/COVID-19/Li1-XCG.csv'
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

    xcgtitle = ['patientid', 'data', 'WBC', 'RBC', 'Hb', 'PLT', 'Neut%', 'Lymph%', 'Mono%','Eos%', 'Baso%',
                'Neut#', 'Lymph#', 'Mono#', 'Eos#', 'Baso#', 'Hct', 'MCV', 'MCH',
                'MCHC', 'MPV', 'Pct', 'PDW']
    title_dic = {'patientid': '', 'data': '', 'WBC': '', 'RBC': '', 'Hb': '', 'PLT': '', 'Neut%': '', 'Lymph%': '',
                 'Mono%': '','Eos%': '', 'Baso%': '','Neut#': '', 'Lymph#': '', 'Mono#': '', 'Eos#': '', 'Baso#': '',
                 'Hct': '', 'MCV': '', 'MCH': '','MCHC': '', 'MPV': '', 'Pct': '', 'PDW': ''}
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
            if 'WBC:白细胞计数' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['WBC'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'RBC:红细胞计数' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['RBC'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'Hb:血红蛋白' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['Hb'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'PLT:血小板计数' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['PLT'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'Neut%:中性粒细胞百分数' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['Neut%'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'Lymph%:淋巴细胞百分数' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['Lymph%'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'Mono%:单核细胞百分数' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['Mono%'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'Eos%:嗜酸性粒细胞百分数' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['Eos%'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'Baso%:嗜碱性粒细胞百分数' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['Baso%'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'Neut#:中性粒细胞绝对值' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['Neut#'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'Lymph#:淋巴细胞绝对值' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['Lymph#'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'Mono#:单核细胞绝对值' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['Mono#'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'Eos#:嗜酸性粒细胞绝对值' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['Eos#'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'Baso#:嗜碱性粒细胞绝对值' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['Baso#'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'Hct:红细胞压积' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['Hct'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'MCV:平均红细胞体积' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['MCV'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'MCH:平均红细胞血红蛋白含量' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['MCH'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'MCHC:平均红细胞血红蛋白浓度' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['MCHC'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'MPV:平均血小板体积' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['MPV'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'Pct:血小板压积' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['Pct'] = wbc[2]
            elif 'PCT:血小板压积' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['Pct'] = wbc[2]
        for m in range(len(xuechangguilist)):
            if 'PDW:血小板分布宽度' in xuechangguilist[m]:
                wbc = xuechangguilist[m]
                wbc = wbc.split(":")
                write_flag = True
                title_dic['PDW'] = wbc[2]
        '''
        for m in range(len(xuechangguilist)):
            if 'CRP(C反应蛋白)' in xuechangguilist[m]:
                wbc = xuechangguilist[m].strip().replace("mg/L(0-5)", "")
                wbc = wbc.strip().replace('>100.000','100').replace('mg/L(<5)', '').replace('mg/L(0-10)','')
                xcg.append(wbc[11:])
        for m in range(len(xuechangguilist)):
            if 'PCT(降钙素原)' in xuechangguilist[m]:
                wbc = xuechangguilist[m].strip().replace("ng/mL(0-0.046)", "").\
                    replace('ng/mL(使用抗生素0-0.1不建议0.1-0.25不鼓励0.25-0.5推荐>0.5强烈建议)', '').replace('ng/mL(0-0.5)', '').replace('ng/mL(0-0.06)', '').replace('>100.000','100')
                xcg.append(wbc[10:])
        '''
        if write_flag is True:
            for key, value in title_dic.items():
                file.write(value)
                file.write(',')
            file.write('\n')  # 注意转换后文件最后一行空白需要删除
            write_flag = False

        for key in title_dic.keys():
            title_dic[key] = ''
    print('excel_txt:End')

