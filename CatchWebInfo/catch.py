#!/usr/bin/python
# -*- coding: utf-8 -*-

# 抓取  www.hznzcn.com  的一些必要品牌信息
# Test by Voodeng
 
#---------------------------------import---------------------------------------
import urllib2;
import re;
from BeautifulSoup import BeautifulSoup;
 
#------------------------------------------------------------------------------
def main(vaule):
    print vaule;
    userMainUrl = vaule;
    req = urllib2.Request(userMainUrl);
    resp = urllib2.urlopen(req);
    respHtml = resp.read();
    #print "respHtml=",respHtml; # you should see the ouput html
 
    # print "Method 2: Use python third lib BeautifulSoup to extract info from html";
    songtasteHtmlEncoding = "GB2312";
    soup = BeautifulSoup(respHtml, fromEncoding=songtasteHtmlEncoding);

    fountbrand = soup.find(attrs={"id":"ECS_FORMBUY"});
    weight = soup.find(attrs={"id":"Product_Weight"});
    coods = soup.find(attrs={"id":"productCoodsNo"});
    price = soup.find(attrs={"id":"productShopPrice"});
    colors = soup.find(attrs={"id":"em0"});
    sizes = soup.find(attrs={"id":"em1"});

    fbranda = fountbrand.findAll(attrs={"class":"list-sptitle"});
    # print colors
    # print type(sizes)
    # print coods.string," > ",price.string," > ", weight.string;
    fp = open("weight.txt","a");
    lcs = coods.string, weight.string;
    print >> fp, coods.string," > ",price.string," > ", weight.string," >| ", colors.text.encode('utf-8')," | ", sizes.text.encode('utf-8')

    fp.close(); #关闭文件  

def loadbr(brurl):
    userMainUrl = brurl;
    req = urllib2.Request(userMainUrl);
    resp = urllib2.urlopen(req);
    respHtml = resp.read();
 
    # print "Method 2: Use python third lib BeautifulSoup to extract info from html";
    songtasteHtmlEncoding = "GB2312";
    soup = BeautifulSoup(respHtml, fromEncoding=songtasteHtmlEncoding);


    fountbrand = soup.find(attrs={"id":"brand_tab_1_2"});
    # foundp = fountbrand.find(attrs={"class":"list-sptitle"})
    
    fbranda = fountbrand.findAll(attrs={"class":"list-sptitle"});
    fp = open("value.txt","w") #打开一个文本文件
    
    for link in fbranda:
        link = link.find('a');
        print 'name:',link.string;
        print 'link:',link.get("href");
        lhref = link.get("href");
        lhref += "\n";
        fp.write(lhref); #写入数据
    fp.close() #关闭文件    

def downs(brands):
    brand = urllib2.quote(brands)
    userMainUrl = "http://www.hznzcn.com/page-yyrz.html?q_day=2015-12-30&q_name="+ brand;
    req = urllib2.Request(userMainUrl);
    resp = urllib2.urlopen(req);
    respHtml = resp.read();
    #print "respHtml=",respHtml; # you should see the ouput html

    songtasteHtmlEncoding = "GB2312";
    soup = BeautifulSoup(respHtml, fromEncoding=songtasteHtmlEncoding);

    
    fbranda = soup.findAll(attrs={"class":"box"});
    fp = open("down.txt","a") #打开一个文本文件
    
    # print fbranda
    for link in fbranda:
       l=  link.find(attrs={'class':'name'})
       op=  link.find(attrs={'class':'operating'})
       print l.text+ " > " + op.text
       # ks = str(l.text+ " > " + op.text)
       print >> fp, l.text.encode('utf-8')+ " > " + op.text.encode('utf-8')

    fp.close();

def redwe():
    for line in open("value.txt"):    
        main(line);

###############################################################################
if __name__=="__main__":
    loadbr("http://www.hznzcn.com/brand-637.html");
    downs("小林双子");
    redwe();
