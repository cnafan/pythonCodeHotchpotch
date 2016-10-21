import os
from os.path import basename, isdir
from os import listdir
import cmd
import sys
import time

def dirs(path):
    if path == None:
        path='C:\\0f655bfe00ac9114d4e74ced4691c4da\\vodcache\\'
            #path =os.getcwd() #current path
    for i in os.walk(path):
        if os.path.exists(i[0]):
             cmd(str(i[0]))

def cmd(command):
    #os.system('ipconfig')
    os.system('cd '+str(command)+' &&copy/b *.tdl 1.mp4')
if __name__=='__main__':
    dirs('C:\\0f655bfe00ac9114d4e74ced4691c4da\\vodcache\\')
    
