# coding=utf-8
import os,os.path,re

path='X:\\图片\\云'

def deal(p):
    for root,dirs,files in os.walk(path):
        #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        """ 
        for eachdir in dirs:
            print('root:'+root)
            print("dir:"+eachdir)
        """
        count=0
        for file in files:
            #print('父目录:'+root)
            #print('文件名:'+file)
            #print(root,os.sep,file)
            print("绝对路径:" + os.path.join(root,file))
            m=p.findall(os.path.join(root,file))
            #print(m)
            if len(m)==2:
                count+=1
                newname=str(m[0])
                print('new:'+str(newname))
                if os.path.exists(newname):
                    os.remove(os.path.join(root,file))
                else:
                    os.rename(os.path.join(root,file),os.path.join(root,newname))
            else:
                pass
                #count_three+=1
                #print("到了快速反击的速度上来看房价")
        return count
    
def main():
  #p4=re.compile('.*(?=\.jpg\.jpg\.jpg\.jpg)')
  # p3=re.compile('.*(?=\.jpg\.jpg\.jpg)')
    p2=re.compile('.*(?=\.jpg\.jpg)')
  # print('4:'+str(deal(p4)))
  #  print('3:'+str(deal(p3)))
    print('2:'+str(deal(p2)))

if __name__=='__main__':
    main()
