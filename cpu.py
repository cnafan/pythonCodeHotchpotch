#coding=utf-8
"""查看cpu利用率
"""
import time
import win32com.client
com=win32com.client.Dispatch("WbemScripting.SWbemRefresher")
obj=win32com.client.GetObject("winmgmts:\\root\cimv2")
processorItems=com.AddEnum(obj,"Win32_PerfFormattedData_PerfOS_Processor").objectSet
while(1):
    com.Refresh()
    for item in processorItems:
        print(item.Name+" ")
        print(item.PercentProcessorTime+"%")
    time.sleep(5)
