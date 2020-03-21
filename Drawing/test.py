"""
Created on Tue May 22 15:30:46 2018

@author: zy
"""

'''
利用自编码网络提取图片的特征，并利用特征还原图片
'''

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data




def two_layer_auto_encoder():
    '''
    通过构建一个量程的自编码网络，将MNIST数据集的数据特征提取处来，并通过这些特征重建一个MNIST数据集    
    下面以MNIST数据集为例，将其像素点组成的数据(28x28)从784维降维到256，然后再降到128，最后再以同样的
    方式经过128，再经过256，最终还原到原来的图片。
    '''
    
    '''
    导入MNIST数据集
    '''
    #mnist是一个轻量级的类，它以numpy数组的形式存储着训练，校验，测试数据集  one_hot表示输出二值化后的10维
    mnist = input_data.read_data_sets('MNIST-data',one_hot=True)
    
    print(type(mnist)) #<class 'tensorflow.contrib.learn.python.learn.datasets.base.Datasets'>
    
    print('Training data shape:',mnist.train.images.shape)           #Training data shape: (55000, 784)
    print('Test data shape:',mnist.test.images.shape)                #Test data shape: (10000, 784)
    print('Validation data shape:',mnist.validation.images.shape)    #Validation data shape: (5000, 784)
    print('Training label shape:',mnist.train.labels.shape)          #Training label shape: (55000, 10)

    '''
    定义参数，以及网络结构
    '''
    n_input = 784            #输入节点
    n_hidden_1 = 256         #第一次256个节点  
    n_hidden_2 = 128         #第二层128个节点      
    batch_size = 256         #小批量大小
    training_epochs = 20     #迭代轮数
    display_epoch  = 5       #迭代2轮输出5次信息
    learning_rate = 1e-2     #学习率  
    show_num = 10            #显示的图片个数   
    
    
    #定义占位符    
    input_x = tf.placeholder(dtype=tf.float32,shape=[None,n_input])            #输入
    input_y = input_x                                                          #输出  
    
    #学习参数
    weights = {
            'encoder_h1':tf.Variable(tf.random_normal(shape=[n_input,n_hidden_1])),
            'encoder_h2':tf.Variable(tf.random_normal(shape=[n_hidden_1,n_hidden_2])),
            'decoder_h1':tf.Variable(tf.random_normal(shape=[n_hidden_2,n_hidden_1])),
            'decoder_h2':tf.Variable(tf.random_normal(shape=[n_hidden_1,n_input]))
            }
    
    biases = {
            'encoder_b1':tf.Variable(tf.random_normal(shape=[n_hidden_1])),
            'encoder_b2':tf.Variable(tf.random_normal(shape=[n_hidden_2])),
            'decoder_b1':tf.Variable(tf.random_normal(shape=[n_hidden_1])),
            'decoder_b2':tf.Variable(tf.random_normal(shape=[n_input]))
        }
    
    #编码 当我们对最终提取的特征节点采用sigmoid函数时，就相当于对输入限制或者缩放，使其位于[0,1]范围中
    encoder_h1 = tf.nn.sigmoid(tf.add(tf.matmul(input_x,weights['encoder_h1']),biases['encoder_b1']))    
    encoder_h2 = tf.nn.sigmoid(tf.add(tf.matmul(encoder_h1,weights['encoder_h2']),biases['encoder_b2']))    

    #解码
    decoder_h1 = tf.nn.sigmoid(tf.add(tf.matmul(encoder_h2,weights['decoder_h1']),biases['decoder_b1']))    
    pred = tf.nn.sigmoid(tf.add(tf.matmul(decoder_h1,weights['decoder_h2']),biases['decoder_b2']))    
    
    
    
    '''
    设置代价函数
    '''    
    #对一维的ndarray求平均
    cost = tf.reduce_mean((input_y - pred)**2)    
    
    '''
    求解,开始训练
    '''
    #train = tf.train.RMSPropOptimizer(learning_rate).minimize(cost)
    train = tf.train.AdamOptimizer(learning_rate).minimize(cost)
    
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        
        #计算一轮跌倒多少次
        num_batch = int(np.ceil(mnist.train.num_examples/batch_size))
        
        #迭代
        for epoch in range(training_epochs):
         
            sum_loss = 0.0
            for i in range(num_batch):
                batch_x,batch_y =  mnist.train.next_batch(batch_size)
                                
                _,loss = sess.run([train,cost],feed_dict={input_x:batch_x})
                sum_loss += loss
                
           #打印信息
            if epoch % display_epoch == 0:
                print('Epoch {}  cost = {:.9f}'.format(epoch+1,sum_loss/num_batch))
        print('训练完成')
        
        #输出图像数据最大值和最小值
        print('最大值：',np.max(mnist.train.images[0]),'最小值:',np.min(mnist.train.images[0]))
        
        '''
        可视化结果
        '''
        reconstruction = sess.run(pred,feed_dict = {input_x:mnist.test.images[:show_num]})
        plt.figure(figsize=(1.0*show_num,1*2))        
        for i in range(show_num):
            plt.subplot(2,show_num,i+1)
            plt.imshow(np.reshape(mnist.test.images[i],(28,28)),cmap='gray')            
            plt.axis('off')
            plt.subplot(2,show_num,i+show_num+1)
            plt.imshow(np.reshape(reconstruction[i],(28,28)),cmap='gray')       
            plt.axis('off')
        plt.show()
        
    
def four_layer_auto_encoder():
    '''
    通过构建一个2维的自编码网络，将MNIST数据集的数据特征提取处来，并通过这些特征重建一个MNIST数据集    
    这里使用4层逐渐压缩将785维度分别压缩成256,64,16,2这4个特征向量,最后再还原    
    '''   
     
    '''
    导入MNIST数据集
    '''
    #mnist是一个轻量级的类，它以numpy数组的形式存储着训练，校验，测试数据集  one_hot表示输出二值化后的10维
    mnist = input_data.read_data_sets('MNIST-data',one_hot=True)
    
    print(type(mnist)) #<class 'tensorflow.contrib.learn.python.learn.datasets.base.Datasets'>
    
    print('Training data shape:',mnist.train.images.shape)           #Training data shape: (55000, 784)
    print('Test data shape:',mnist.test.images.shape)                #Test data shape: (10000, 784)
    print('Validation data shape:',mnist.validation.images.shape)    #Validation data shape: (5000, 784)
    print('Training label shape:',mnist.train.labels.shape)          #Training label shape: (55000, 10)

    '''
    定义参数，以及网络结构
    '''
    n_input = 784            #输入节点
    n_hidden_1 = 256        
    n_hidden_2 = 64        
    n_hidden_3 = 16        
    n_hidden_4 = 2        
    batch_size = 256         #小批量大小
    training_epochs = 20     #迭代轮数
    display_epoch  = 5       #迭代1轮输出5次信息
    learning_rate = 1e-2     #学习率  
    show_num = 10            #显示的图片个数   
    
    
    #定义占位符    
    input_x = tf.placeholder(dtype=tf.float32,shape=[None,n_input])            #输入
    input_y = input_x                                                          #输出  
    
    #学习参数
    weights = {
            'encoder_h1':tf.Variable(tf.random_normal(shape=[n_input,n_hidden_1])),            
            'encoder_h2':tf.Variable(tf.random_normal(shape=[n_hidden_1,n_hidden_2])),
            'encoder_h3':tf.Variable(tf.random_normal(shape=[n_hidden_2,n_hidden_3])),
            'encoder_h4':tf.Variable(tf.random_normal(shape=[n_hidden_3,n_hidden_4])),
            'decoder_h1':tf.Variable(tf.random_normal(shape=[n_hidden_4,n_hidden_3])),
            'decoder_h2':tf.Variable(tf.random_normal(shape=[n_hidden_3,n_hidden_2])),
            'decoder_h3':tf.Variable(tf.random_normal(shape=[n_hidden_2,n_hidden_1])),
            'decoder_h4':tf.Variable(tf.random_normal(shape=[n_hidden_1,n_input]))
            }
    
    biases = {
            'encoder_b1':tf.Variable(tf.random_normal(shape=[n_hidden_1])),
            'encoder_b2':tf.Variable(tf.random_normal(shape=[n_hidden_2])),
            'encoder_b3':tf.Variable(tf.random_normal(shape=[n_hidden_3])),
            'encoder_b4':tf.Variable(tf.random_normal(shape=[n_hidden_4])),
            'decoder_b1':tf.Variable(tf.random_normal(shape=[n_hidden_3])),
            'decoder_b2':tf.Variable(tf.random_normal(shape=[n_hidden_2])),            
            'decoder_b3':tf.Variable(tf.random_normal(shape=[n_hidden_1])),
            'decoder_b4':tf.Variable(tf.random_normal(shape=[n_input]))
        }
    
    #编码
    encoder_h1 = tf.nn.sigmoid(tf.add(tf.matmul(input_x,weights['encoder_h1']),biases['encoder_b1']))    
    encoder_h2 = tf.nn.sigmoid(tf.add(tf.matmul(encoder_h1,weights['encoder_h2']),biases['encoder_b2']))    
    encoder_h3 = tf.nn.sigmoid(tf.add(tf.matmul(encoder_h2,weights['encoder_h3']),biases['encoder_b3']))    
    #在编码的最后一层，没有进行sigmoid变化，这是因为生成的二维特征数据其特征已经标的极为主要，所有我们希望让它
    #传到解码器中，少一些变化可以最大化地保存原有的主要特征
    #encoder_h4 = tf.nn.sigmoid(tf.add(tf.matmul(encoder_h3,weights['encoder_h4']),biases['encoder_b4']))
    encoder_h4 = tf.add(tf.matmul(encoder_h3,weights['encoder_h4']),biases['encoder_b4'])

    #解码
    decoder_h1 = tf.nn.sigmoid(tf.add(tf.matmul(encoder_h4,weights['decoder_h1']),biases['decoder_b1']))    
    decoder_h2 = tf.nn.sigmoid(tf.add(tf.matmul(decoder_h1,weights['decoder_h2']),biases['decoder_b2']))    
    decoder_h3 = tf.nn.sigmoid(tf.add(tf.matmul(decoder_h2,weights['decoder_h3']),biases['decoder_b3']))    
    pred = tf.nn.sigmoid(tf.add(tf.matmul(decoder_h3,weights['decoder_h4']),biases['decoder_b4']))    
    
        
    '''
    设置代价函数
    '''    
    #对一维的ndarray求平均
    cost = tf.reduce_mean((input_y - pred)**2)    
    
    '''
    求解,开始训练
    '''
    train = tf.train.AdamOptimizer(learning_rate).minimize(cost)
    
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        
        #计算一轮跌倒多少次
        num_batch = int(np.ceil(mnist.train.num_examples/batch_size))
        
        #迭代
        for epoch in range(training_epochs):
         
            sum_loss = 0.0
            for i in range(num_batch):
                batch_x,batch_y =  mnist.train.next_batch(batch_size)
                                
                _,loss = sess.run([train,cost],feed_dict={input_x:batch_x})
                sum_loss += loss
                
           #打印信息
            if epoch % display_epoch == 0:
                print('Epoch {}  cost = {:.9f}'.format(epoch+1,sum_loss/num_batch))
        print('训练完成')
        
        #输出图像数据最大值和最小值
        print('最大值：',np.max(mnist.train.images[0]),'最小值:',np.min(mnist.train.images[0]))
        
        '''
        可视化结果
        '''
        reconstruction = sess.run(pred,feed_dict = {input_x:mnist.test.images[:show_num]})
        plt.figure(figsize=(1.0*show_num,1*2))        
        for i in range(show_num):
            plt.subplot(2,show_num,i+1)
            plt.imshow(np.reshape(mnist.test.images[i],(28,28)),cmap='gray')            
            plt.axis('off')
            plt.subplot(2,show_num,i+show_num+1)
            plt.imshow(np.reshape(reconstruction[i],(28,28)),cmap='gray')       
            plt.axis('off')
        plt.show()
        
        '''
        显示二维的特征数据  有点聚类的感觉，一般来说通过自编码网络将数据降维之后更有利于进行分类处理
        '''
        plt.figure(figsize=(10,8))
        #将onehot转为一维编码
        labels = [np.argmax(y) for y in mnist.test.labels]              
        encoder_result = sess.run(encoder_h4,feed_dict={input_x:mnist.test.images})
        plt.scatter(encoder_result[:,0],encoder_result[:,1],c=labels)
        plt.colorbar()
        plt.show()
        

def max_pool_with_argmax(net,stride):
    '''
    重定义一个最大池化函数，返回最大池化结果以及每个最大值的位置(是个索引，形状和池化结果一致)
    
    args:
        net:输入数据 形状为[batch,in_height,in_width,in_channels]
        stride：步长，是一个int32类型，注意在最大池化操作中我们设置窗口大小和步长大小是一样的
    '''
    #使用mask保存每个最大值的位置 这个函数只支持GPU操作
    _, mask = tf.nn.max_pool_with_argmax( net,ksize=[1, stride, stride, 1], strides=[1, stride, stride, 1],padding='SAME')
    #将反向传播的mask梯度计算停止
    mask = tf.stop_gradient(mask)
    #计算最大池化操作
    net = tf.nn.max_pool(net, ksize=[1, stride, stride, 1],strides=[1, stride, stride, 1], padding='SAME') 
    #将池化结果和mask返回
    return net,mask



def un_max_pool(net,mask,stride):
    '''
    定义一个反最大池化的函数，找到mask最大的索引，将max的值填到指定位置
    args:
        net:最大池化后的输出，形状为[batch, height, width, in_channels]
        mask：位置索引组数组，形状和net一样
        stride:步长，是一个int32类型，这里就是max_pool_with_argmax传入的stride参数
    '''
    ksize = [1, stride, stride, 1]
    input_shape = net.get_shape().as_list()
    #  calculation new shape
    output_shape = (input_shape[0], input_shape[1] * ksize[1], input_shape[2] * ksize[2], input_shape[3])
    # calculation indices for batch, height, width and feature maps
    one_like_mask = tf.ones_like(mask)
    batch_range = tf.reshape(tf.range(output_shape[0], dtype=tf.int64), shape=[input_shape[0], 1, 1, 1])
    b = one_like_mask * batch_range
    y = mask // (output_shape[2] * output_shape[3])
    x = mask % (output_shape[2] * output_shape[3]) // output_shape[3]
    feature_range = tf.range(output_shape[3], dtype=tf.int64)
    f = one_like_mask * feature_range
    # transpose indices & reshape update values to one dimension
    updates_size = tf.size(net)
    indices = tf.transpose(tf.reshape(tf.stack([b, y, x, f]), [4, updates_size]))
    values = tf.reshape(net, [updates_size])
    ret = tf.scatter_nd(indices, values, output_shape)
    return ret



def cnn_auto_encoder():
    tf.reset_default_graph()
    '''
    通过构建一个卷积网络的自编码，将MNIST数据集的数据特征提取处来，并通过这些特征重建一个MNIST数据集    
    '''
    
    '''
    导入MNIST数据集
    '''
    #mnist是一个轻量级的类，它以numpy数组的形式存储着训练，校验，测试数据集  one_hot表示输出二值化后的10维
    mnist = input_data.read_data_sets('MNIST-data',one_hot=True)
    
    print(type(mnist)) #<class 'tensorflow.contrib.learn.python.learn.datasets.base.Datasets'>
    
    print('Training data shape:',mnist.train.images.shape)           #Training data shape: (55000, 784)
    print('Test data shape:',mnist.test.images.shape)                #Test data shape: (10000, 784)
    print('Validation data shape:',mnist.validation.images.shape)    #Validation data shape: (5000, 784)
    print('Training label shape:',mnist.train.labels.shape)          #Training label shape: (55000, 10)

    '''
    定义参数，以及网络结构
    '''
    n_input = 784
    batch_size = 256         #小批量大小
    n_conv_1 = 16            #第一层16个ch
    n_conv_2 = 32            #第二层32个ch
    training_epochs = 8      #迭代轮数
    display_epoch  = 5       #迭代2轮输出5次信息
    learning_rate = 1e-2     #学习率  
    show_num = 10            #显示的图片个数   
    
    
    #定义占位符     使用反卷积的时候，这个形状中不能带有None，不然会报错
    input_x = tf.placeholder(dtype=tf.float32,shape=[batch_size,n_input])      #输入
    #input_y = input_x                                                          #输出  
    
    #学习参数    
    weights = {
        'encoder_conv1': tf.Variable(tf.truncated_normal([5, 5, 1, n_conv_1],stddev=0.1)),
        'encoder_conv2': tf.Variable(tf.random_normal([3, 3, n_conv_1, n_conv_2],stddev=0.1)),
        'decoder_conv1': tf.Variable(tf.random_normal([5, 5, 1, n_conv_1],stddev=0.1)),
        'decoder_conv2': tf.Variable(tf.random_normal([3, 3, n_conv_1, n_conv_2],stddev=0.1))
    }
    biases = {
        'encoder_conv1': tf.Variable(tf.zeros([n_conv_1])),
        'encoder_conv2': tf.Variable(tf.zeros([n_conv_2])),
        'decoder_conv1': tf.Variable(tf.zeros([n_conv_1])),
        'decoder_conv2': tf.Variable(tf.zeros([n_conv_2])),
    }
    
    
    image_x = tf.reshape(input_x,[-1,28,28,1])    
    #编码 当我们对最终提取的特征节点采用sigmoid函数时，就相当于对输入限制或者缩放，使其位于[0,1]范围中
    encoder_conv1 = tf.nn.relu(tf.nn.conv2d(image_x, weights['encoder_conv1'],strides=[1,1,1,1],padding = 'SAME') + biases['encoder_conv1'])      
    print('encoder_conv1:',encoder_conv1.shape)
    encoder_conv2 = tf.nn.relu(tf.nn.conv2d(encoder_conv1, weights['encoder_conv2'],strides=[1,1,1,1],padding = 'SAME') + biases['encoder_conv2'])   
    print('encoder_conv2:',encoder_conv2.shape)
    encoder_pool2, mask = max_pool_with_argmax(encoder_conv2, 2)    #池化
    print('encoder_pool2:',encoder_pool2.shape)
    

    #解码
    decoder_upool = un_max_pool(encoder_pool2,mask,2)     #反池化
    decoder_conv1 = tf.nn.conv2d_transpose(decoder_upool - biases['decoder_conv2'], weights['decoder_conv2'],encoder_conv1.shape,strides=[1,1,1,1],padding='SAME')    
    pred = tf.nn.conv2d_transpose(decoder_conv1 - biases['decoder_conv1'], weights['decoder_conv1'], image_x.shape,strides=[1,1,1,1],padding='SAME')
    print('pred:',pred.shape)
    

    '''
    设置代价函数
    '''    
    #对一维的ndarray求平均
    cost = tf.reduce_mean((image_x - pred)**2)    
    
    '''
    求解,开始训练
    '''
    #train = tf.train.RMSPropOptimizer(learning_rate).minimize(cost)
    train = tf.train.AdamOptimizer(learning_rate).minimize(cost)
    
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        
        #计算一轮跌倒多少次
        num_batch = int(np.ceil(mnist.train.num_examples/batch_size))
        
        #迭代
        for epoch in range(training_epochs):
         
            sum_loss = 0.0
            for i in range(num_batch):
                batch_x,batch_y =  mnist.train.next_batch(batch_size)
                                
                _,loss = sess.run([train,cost],feed_dict={input_x:batch_x})
                sum_loss += loss
                
           #打印信息
            if epoch % display_epoch == 0:
                print('Epoch {}  cost = {:.9f}'.format(epoch+1,sum_loss/num_batch))
        print('训练完成')
        
        #输出图像数据最大值和最小值
        print('最大值：',np.max(mnist.train.images[0]),'最小值:',np.min(mnist.train.images[0]))
        
        '''
        可视化结果
        '''
        reconstruction = sess.run(pred,feed_dict = {input_x:batch_x})
        plt.figure(figsize=(1.0*show_num,1*2))        
        for i in range(show_num):
            plt.subplot(2,show_num,i+1)
            plt.imshow(np.reshape(batch_x[i],(28,28)),cmap='gray')            
            plt.axis('off')
            plt.subplot(2,show_num,i+show_num+1)
            plt.imshow(np.reshape(reconstruction[i],(28,28)),cmap='gray')       
            plt.axis('off')
        plt.show()
        
        
        
if  __name__ == '__main__':
    #two_layer_auto_encoder()
    four_layer_auto_encoder()
    #cnn_auto_encoder()