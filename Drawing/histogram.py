'''
Created on 2019年3月23日

@author: lenovo
'''
import numpy as np
from matplotlib import pyplot as plt
from statisticsEntity import readfile_FCC

# histogram
def histogramRoutine():
    plt.figure(figsize=(9,6))
    labels =["Q1","Q2","Q3","Q4","Q5","Q6","Q7","Q8","Q9","Q10","Q11","Q12","Q13"]
    n = 13
    X = np.arange(n)+1 #X是1,2,3,4,5,6,7,8,柱的个数
    #uniform均匀分布的随机数，normal是正态分布的随机数，0.5-1均匀分布的数，一共有n个
    Y1 = [0.86,0.76,0.68,0.69,0.91,0.90,0.64,1,0.54,0.83,0.81,0.73,0.75] # precision
    Y2 = [0.81,0.85,0.75,0.76,0.93,0.83,0.51,0.89,0.68,0.91,0.89,0.91,0.63] # recall
    Y3 = [0.83,0.80,0.71,0.73,0.91,0.86,0.56,0.94,0.6,0.87,0.84,0.81,0.68] # F-score
    plt.xticks(X+0.2,labels)
    plt.bar(X, Y1, alpha=0.9, width = 0.2, facecolor = 'dimgrey', label='Precision', lw=1)
    plt.bar(X+0.2, Y2, alpha=0.9, width = 0.2, facecolor = 'silver', label='Recall', lw=1)
    plt.bar(X+0.4, Y3, alpha=0.9, width = 0.2, facecolor = 'k', label='F-measure', lw=1)
    plt.legend(loc="upper left") # label的位置在左上，没有这句会找不到label去哪了
    
    plt.ylim(0,+1.1)
    plt.show()
    

# histogram transverse
def histogramTransverse():
    plt.rcdefaults()
    fig,ax = plt.subplots()     #   ax为子图
     
    #   数据生成
    labels =["Q1","Q2","Q3","Q4","Q5","Q6","Q7"]
    y_pos = np.arange(len(labels))  #   根据人数生成的数据组y_post=[0,1,2,3,4]

    X1 = [0.64,0.54,0.69,0.68,0.83,0.75,0.91,]   # Precision
    X2 = [0.51,0.68,0.76,0.75,0.91,0.63,0.93]   # Recall
    X3 = [0.56,0.6,0.73,0.71,0.87, 0.68,0.91]   # F-score #   生成5个元素的随机数组
   # error = np.random.rand(len(labels)) #   生成5个元素的随机数组0-1之间
     
    #   数据显示
    ax.barh(y_pos, X1,0.3,color='steelblue',label='Precision')
    ax.barh(y_pos+0.3, X2,0.3,color='silver', label='Recall')
    ax.barh(y_pos+0.6, X3,0.3,color='slategrey', label='F-score')
    
#     ax.barh(y_pos+0.1, X2, color='k', ecolor='black')
    #   y_pos   横坐标，    performance 纵坐标，xerr=error  误差图显示，
    #   align='center'数据标签显示在柱子中心，color='green'柱子颜色， ecolor='black'柱子边缘颜色
     
    ax.set_yticks(y_pos+0.3)    #   设置纵坐标的刻度
    ax.set_yticklabels(labels)  #   设置纵坐标的标签（人名）
    ax.invert_yaxis()  #    把Y反转，取消这一行运行一下就明白了
   #ax.set_xlabel('Performance')    #   显示X轴标签
#     ax.set_title('F-score')   #   设置图头
    plt.xlim(0.0,+1)
    
    plt.legend(loc='upper right')
#     plt.legend(loc="upper right")
    plt.show()  #   显示图片

# histogram CCKSs
def hisCCK2017():
    plt.figure(figsize=(12,6))
     
    #第一行第一列图形
    ax1 = plt.subplot(1,2,1)
    #第一行第二列图形
    ax2 = plt.subplot(1,2,2)
    
    
    
    CCKS2017labels =["Body","Disease","SymDes","Test","Treament"]
    FCClabels =["Body","Operation","Drug","Lesion","Feature"]
    n = 5
    X = np.arange(n)+1 #X是1,2,3,4,5,6,7,8,柱的个数
    #uniform均匀分布的随机数，normal是正态分布的随机数，0.5-1均匀分布的数，一共有n个
    Y1 = [0.8515,0.7619,0.9628,0.9326,0.7636] # F
    Y2 = [0.8626,0.7892,0.9527,0.9366,0.7865] # F
    Y3 = [0.8706,0.8068,0.9489,0.9403,0.8235] # F
    Y4 = [0.8884,0.8268,0.9549,0.9423,0.8835] # F
    
    Z1 = [0.8026,0.7536,0.8653,0.8836,0.8164] # F81.56
    Z2 = [0.7916,0.8621,0.8631,0.8736,0.8506] # F84.38
    Z3 = [0.8336,0.8436,0.8824,0.8935,0.8735] # F87.79
    Z4 = [0.8515,0.8402,0.9023,0.9034,0.8624] # F88.56
    
    plt.sca(ax1)
    
    ax1.set_title('CCKS2017')
    
    plt.xticks(X+0.2,CCKS2017labels)
    plt.bar(X, Y1, alpha=0.9, width = 0.2, facecolor = 'silver', label='CRF', lw=1)
    plt.bar(X+0.2, Y2, alpha=0.9, width = 0.2, facecolor = 'dimgray', label='BiLSTM-CRF', lw=1)
    plt.bar(X+0.4, Y3, alpha=0.9, width = 0.2, facecolor = 'cadetblue', label='CNN-BiLSTM-CRF', lw=1)
    plt.bar(X+0.6, Y4, alpha=0.9, width = 0.2, facecolor = 'k', label='Our model', lw=1)
    plt.legend(loc="upper left") # label的位置在左上，没有这句会找不到label去哪了
    
    plt.ylim(0.7,+1)
    
    plt.sca(ax2)
    ax2.set_title('FCC-Ope')
    
    plt.xticks(X+0.2,FCClabels)
    plt.bar(X, Z1, alpha=0.9, width = 0.2, facecolor = 'silver', label='CRF', lw=1)
    plt.bar(X+0.2, Z2, alpha=0.9, width = 0.2, facecolor = 'dimgray', label='BiLSTM-CRF', lw=1)
    plt.bar(X+0.4, Z3, alpha=0.9, width = 0.2, facecolor = 'cadetblue', label='CNN-BiLSTM-CRF', lw=1)
    plt.bar(X+0.6, Z4, alpha=0.9, width = 0.2, facecolor = 'k', label='Our model', lw=1)
    plt.legend(loc="upper left") # label的位置在左上，没有这句会找不到label去哪了
    
    plt.ylim(0.7,+1)
    
    plt.show()



if __name__ == '__main__':
#    histogramRoutine()
   histogramTransverse()