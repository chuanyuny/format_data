#-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def write_txt(strings):
	fw=open('after.txt','a')
	fw.writelines(strings)
	fw.close



def read_txt():
	fo=open("data20170620.txt",'r')
	content=fo.readlines()
	fo.close
	tem=[]
	for i in range(37):
		tem=content[2:]
		print tem
	tem2=[]
	for each in tem:
		aa=each.split('|')   #  aa is a list
		
		tem2=aa[1:6]

		tem3=[]
		for item in tem2:
			tem2=item.strip()
			tem3.append(tem2)
		b=" ".join(tem3)
		write_txt(b+'\n')

read_txt()



