import xlrd
import numpy as np
from numpy import *
import define
import kmeans
import csv

OPEN=1
HIGH=2
LOW=3
CLOSE=4
VOL=5
ADJ=6

l=[]
fr=file('_use.csv','r')
r=csv.reader(fr)
fw=file('_data.csv','w')
w=csv.writer(fw)

for i in r:
	l.append(i[0])
	ft=file(i[0]+'.csv','r')
	t=csv.reader(ft)
	counter=0
	sum_bv=0
	for j in t:
		if j[0]!='Data':
			counter=counter+1
			
	

data=transpose(array(data))
data.dtype=float

kmeans.kmeans(data,4,['1','4'])


