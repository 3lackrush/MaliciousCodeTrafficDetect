#!/usr/bin/env python
#coing:utf-8

#__Author__ == 'Kios'

import requests
import os
from datetime import datetime
import csv
import time
import sys

def OpenCsv():
    ListTry = []
    with open('export.csv','rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            ListTry.append(row)
    return ListTry


def GetTraffic():
    
    proxies = {
        "http":"socks5://127.0.0.1:1080",
        "https":"socks5://127.0.0.1:1080"
    }
    
    ListGet = OpenCsv()
    length = 0
    ListUrl = []
    #print("length is %d",len(ListGet))
    print("Engine Start...Proceed!")
    while(length < (len(ListGet)-1)):
        url = ListGet[length][1]
        if (url != '-'):
            realUrl = url
        else:
            realUrl = ListGet[length][2]
        #print("The url is %s",realUrl)
        #print("\n")
        try:
            r = requests.get("http://"+realUrl,proxies=proxies,timeout=5)
            status_code = r.status_code

            if status_code == 200:
                #os.system('wget http://'+realUrl)
                fp = open("data.txt","a")
                fp.write(realUrl+"\n")
                fp.close()
            else:
                print(realUrl +" is out of date! " +"HTTP Code:"+str(status_code))
            #time.sleep(5)
        except requests.exceptions.RequestException:
            print"LOG NO."+str(length)+":TimeOut! Can not Connect to "+"http://"+realUrl
        length += 1
    
    

if __name__ == '__main__':
    GetTraffic()
