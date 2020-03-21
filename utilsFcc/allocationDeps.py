'''
@author: GeXiaowei
@contact: xwge@foxmail.com
@time: 2018/10/25
'''

import os
import re
import shutil

import pymysql


def getFileName(path):
    # 列出文档
    file_list = os.listdir(path)
    for i in range(len(file_list)):
        old_file_path = os.path.join(path, file_list[i])
        if os.path.isdir(old_file_path):
            # zhuyuanId = re.finditer(r'\d+',file_list[i])[0]   #获取所有的文件名
            # zhuyuanId = int(zhuyuanId)
            zhuyuanId = file_list[i]
            if zhuyuanId[0] == "Z":
                new_file_path = os.path.join(path, '%s' % (getDepartName(zhuyuanId)))  # 要放置的新路径
                shutil.move(old_file_path, new_file_path)
        elif not os.path.exists(old_file_path):
            pass


def getDepartName(zhuyuanId):
    # 打开数据库连接
    db = pymysql.connect("117.158.216.9", "root", "xxc8001@Zdy", "test")
    # 使用 cursor() 方法创建�?个游标对�? cursor
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT * FROM departuser \
           WHERE zhuyuanId = '%s'" % zhuyuanId
    # 执行SQL语句
    cursor.execute(sql)
    # 获取�?有记录列�?
    results = cursor.fetchall()
    for row in results:
        chuyuanks = row[3]
        zhuyuanId = row[1]
        new_folder_path = os.path.join(path, '%s' % chuyuanks)
        print(new_folder_path)
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
    # 关闭数据库连�?
    db.close()
    return chuyuanks


if __name__ == '__main__':
    path = 'E:/JavaNew/workspace/EMRMarking/data/datas'  # 存放病历的目�?
    getFileName(path)

    
