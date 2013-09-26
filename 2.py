#coding:utf-8
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

print "买两只烧鸡吧，骚年："
print "1号钱：$", 35 * 0.9
print "===================================="
print "新个税计算下："
print "工资的起征点变成3500  公式是（工资 - 起征点）× 对应税率 - 速算扣除数"
#当月工资收入的个人所得税=[5000－3500-5000×10%（个人社保部分）-5000*5%（个人住房公积金部分）]×3%－0（速算扣除数）=22.5元。

before = 20000 #税前
safaty = 200  #保险
start = 3500  #起征
taxRate = 0.03 #税率

tax = before - start #税级计算
if tax <= 1500 : taxRate = [0.03,0]
if 1500 < tax <= 4500 : taxRate = [0.1,105]
if 4500 < tax <= 9000 : taxRate = [0.2,555]
if 9000 < tax <= 35000 : taxRate = [0.25,1005] 
if 35000 < tax <= 55000 : taxRate = [0.30,2755]
if 55000 < tax <= 80000 : taxRate = [0.35,5055]
if 80000 < tax : taxRate = [0.45,13505]

deduction = ( before - start ) * taxRate[0] - taxRate[1] #扣除
after = before - deduction #税后

print "税前收入: ￥",before
print "税率：",taxRate[0]*100,"%"
print "速算扣除数：￥", taxRate[1]
print "应该缴税：￥",deduction
print "税后所得：￥",after
