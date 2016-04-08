import urllib
import urllib2
import sys,re,time
import fileinput
import socket

path='C:\Users\StMatengss\Desktop\learning\spliter'
#http://ichart.finance.yahoo.com/table.csv?s=YHOO&d=0&
#e=28&f=2010&g=d&a=3&b=12&c=1996&ignore=.csv
socket.setdefaulttimeout(20)

names=[line[0:len(line)-1] for line in fileinput.input\
      (path+'\B.txt')]
for n,name in enumerate(names):
    if n%7==0 and n!=0:time.sleep(120)
    url='http://ichart.finance.yahoo.com/table.csv?s='+name+\
        '&d=0&e=01&f=2014&g=d&a=0&b=01&c=2009&ignore=.csv'
    try:
        urllib.urlretrieve(url,path+'\\'+name+'.csv')
        print name
    except:
        print name+':error!'
print 'end!!!!'
