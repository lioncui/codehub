#!/usr/bin/python
#-*- coding: UTF-8 -*-
import urllib2,urllib,os
from pyquery import PyQuery as pq

class Yumlist():
    
    def __init__(self,url):
        self.url=url
        self.page=self.getpage()
        self.packagelist=[]

    def getpage(self):
        request = urllib2.Request(self.url)
        request.add_header('User-Agent', 'fake-client')
        response = urllib2.urlopen(request)
        html=response.read()
        return pq(html)

    def getlist(self):
        for content in self.page('a'):
            packages=pq(content).attr('href')
            self.packagelist.append(packages)
        del self.packagelist[0]
        return tuple(self.packagelist)

    def download(self,rpm=None,path=os.getcwd()):
        downloadurl=self.url+rpm
        urllib.urlretrieve(downloadurl,path+'/'+'%s' %rpm)

if __name__ == '__main__':
    get=Yumlist('http://mirrors.163.com/centos/6.6/xen4/x86_64/Packages/')
    print get.getlist()
    print 'Finish...'