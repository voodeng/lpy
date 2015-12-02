#!/usr/bin/python
# -*- coding: utf-8 -*-
#注释！见鬼的运算符号和该死的运算符号英文啊
###ps: "#"这玩意洋气的叫法为"pound"英镑符？gaga
'''
+ 	plus 加号     	#加法
- 	minus 减号		#减法
/ 	slash 斜杠		#除法
* 	asterisk 星号	#乘法
% 	percent 百分号	#求余数
< 	less-than 小于号
> 	greater-than 大于号
<= 	less-than-equal 小于等于号
>= 	greater-than-equal 大于等于号
'''
# import 
import sys 


def pTax(before,safaty):	
	print "===================================="
	print u"2015 新个税计算下："
	print u"工资的起征点变成3500  公式是（工资 - 三险一金 - 起征点）× 对应税率 - 速算扣除数"
	print "===================================="
	#当月工资收入的个人所得税=[5000－3500-5000×10%（个人社保部分）-5000*5%（个人住房公积金部分）]×3%－0（速算扣除数）=22.5元。

	if (before == ""):
		before  = 8500 #税前 
	if (safaty == ""):
		safaty = before * 0.16 #保险
	elif (0 < safaty < 1):
		safaty = before * safaty
		print safaty
	start   = 3500  #起征
	taxRate = 0.03 #最低税率

	tax = before - start #税级计算
	if tax         <= 1500 : taxRate = [0.03,0]
	if 1500 < tax  <= 4500 : taxRate = [0.1,105]
	if 4500 < tax  <= 9000 : taxRate = [0.2,555]
	if 9000 < tax  <= 35000 : taxRate = [0.25,1005] 
	if 35000 < tax <= 55000 : taxRate = [0.30,2755]
	if 55000 < tax <= 80000 : taxRate = [0.35,5055]
	if 80000 < tax : taxRate = [0.45,13505]

	deduction = ( before - start - safaty ) * taxRate[0] - taxRate[1] #扣除
	after     = before - deduction - safaty #税后

	print u"税前收入: ￥",before
	print u"税率：",taxRate[0]*100,"%"
	print u"速算扣除数：￥", taxRate[1]
	print u"保险缴纳：￥",safaty
	print u"应该缴税：￥",deduction
	print u"税后所得：￥",after

def main():
	if len(sys.argv)>=3:
		str1 = int(sys.argv[1])
		str2 = float(sys.argv[2])
		pTax(str1,str2)
	elif (len(sys.argv)>=2 and sys.argv[1]=="-h"):
		print "U Need a Help!"
		print u"参数写 ‘ 金额 保险额或百分比 ’"
	else:
		print u"8000起低"
		pTax(8000,800)

if __name__ == "__main__":
    main()