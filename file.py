# coding=utf-8
import os,os.path

path='X:\图片\切克闹'
for root,dirs,files in os.walk(path):
    ##三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for eachdir in dirs:
        print('root:'+root)
        print("dir:"+eachdir)
        
    for file in files:
        print('父目录:'+root)
        print('文件名:'+file)
        #print(root,os.sep,file)
        print("绝对路径:" + os.path.join(root,file))
        newname= os.path.join(root,file)+'.jpg'
        print(newname)
        os.rename(os.path.join(root,file),os.path.join(root,newname))
