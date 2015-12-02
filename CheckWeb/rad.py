#coding:utf-8
#raad file and 
import check_web

a=open(r'site.txt')
b=a.readlines()
print len(b)

print (b[34])

for i in b:
	print i