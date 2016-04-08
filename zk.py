import xlrd
import numpy as np
from numpy import *
import define
import kmeans
import csv
import os

r=csv.reader(file('C:\Users\StMatengss\Desktop\learning\spliter\list.csv','r'))
rr=csv.writer(file('C:\Users\StMatengss\Desktop\learning\spliter\_using.csv','w'))
for i in r:
	if os.path.exists('C:\Users\StMatengss\Desktop\learning\spliter\\'+i[0]+'.csv'):
		rr.writerow(i)

