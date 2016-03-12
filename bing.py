import urllib
import urllib2
import sys,re

#&first=40&FORM=PORE

path=r"C:\Users\StMatengss\Desktop\learning\testpdf\\"
mp=dict()

keyword=raw_input()
for i in range(0,1):
    url=urllib.urlopen('https://www.bing.com/search?q='+keyword
                       +'+filetype%3Apdf&first='+str(i*10)+'&FORM=PORE')
    text=url.read()
    #text="".join(text.split())
    text=str(text)
    #fi=open('test.txt','w')
    #fi.writelines(text)
    #print text
    rega=re.compile('<a href=\"[^\"]*.pdf\" target=\"_blank\" h=\"[^\"]*\">')
    regb=re.compile('http[^ ]+\.pdf')
    regc=re.compile('/[^/]+.pdf')
    res=rega.findall(text)
    #res=re.match('<a href="(.+).pdf" target="_blank" h="(.+)">',str(text))
    for i in res:
        url=regb.findall(i)[0]
        name=regc.findall(url)[0]
        if(mp.has_key(name)==True):
            pass
        else:
            print name
            try:
                urllib.urlretrieve(url,path+name)
            except:
                print 'error'
        mp[name]=True
    




