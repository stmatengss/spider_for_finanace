import urllib
import urllib2
import sys,re


url=urllib.urlopen('http://www.eoddata.com/stocklist/NASDAQ/A.htm')
text=url.read()
text=str(text)
#<A href="/stockquote/NASDAQ/AXSM.htm" title="Display Quote &amp; Chart for NASDAQ,AXSM">AXSM</A></td>
rega=re.compile('<A href=\"/stockquote[^\"]*.htm\" title=\"Display Quote &amp;[^\"]*">[^<]*</A></td>')
regb=re.compile('>[^<>]+<')
regc=re.compile('/[^/]+.pdf')
res=rega.findall(text)
    #res=re.match('<a href="(.+).pdf" target="_blank" h="(.+)">',str(text))
for i in res:
    url=regb.findall(i)[0]
    print url[1:len(url)-1]
##        name=regc.findall(url)[0]
##        if(mp.has_key(name)==True):
##            pass
##        else:
##            print name
##            try:
##                urllib.urlretrieve(url,path+name)
##            except:
##                print 'error'
##        mp[name]=True
    




