#!/usr/bin/env python
#coding:utf-8

import sys
import requests
import datetime
import threading

url = sys.argv[1]
 
 
def Handler(start, end, url, filename):
    
    headers = {'Range': 'bytes=%d-%d' % (start, end)}
    r = requests.get(url, headers=headers, stream=True)
    
    # 写入文件对应位置
    with open(filename, "r+b") as fp:
        fp.seek(start)
        var = fp.tell()
        fp.write(r.content)


def download_file(url, num_thread = 5):

    r = requests.head(url)

    try:
        file_name = url.split('.')[-1]
        file_size = int(r.headers['content-length'])
    except:
        print("Check your URL, may be it is not support threading download!")
        return 

    fp = open(file_name,"wb")
    fp.truncate(file_size)
    fp.close()

    part = file_size // num_thread

    for i in range(num_thread):
        start = part * i
        if i == num_thread - 1:
            end = file_size
        else:
            end = start + part

        t = threading.Thread(target=Handler, kwargs={'start':start, 'end':end, 'url':url, 'filename':file_name})
        t.setDaemon(True)
        t.start()

    main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()
    print('%s Download Complete!' % file_name)


if __name__ == '__main__':
    start = datetime.datetime.now().replace(microsecond=0)  
    download_file(url)
    end = datetime.datetime.now().replace(microsecond=0)
    print("用时: ")
    print(end-start)
