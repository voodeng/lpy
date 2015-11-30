#!/usr/bin/python
# -*- coding: utf-8 -*-

 
#---------------------------------import---------------------------------------
import urllib2;
import re;
from BeautifulSoup import BeautifulSoup;
 
#------------------------------------------------------------------------------
def main():
    userMainUrl = "http://www.hznzcn.com/brand-138.html";
    req = urllib2.Request(userMainUrl);
    resp = urllib2.urlopen(req);
    respHtml = resp.read();
    #print "respHtml=",respHtml; # you should see the ouput html
 
    print "Method 1: Use python re to extract info from html";
    #<h1 class="h1user">crifan</h1>
    foundH1user = re.search('<h1\s+?class="h1user">(?P<h1user>.+?)</h1>', respHtml);
    print "foundH1user=",foundH1user;
    if(foundH1user):
        h1user = foundH1user.group("h1user");
        print "h1user=",h1user;
 
    print "Method 2: Use python third lib BeautifulSoup to extract info from html";
    songtasteHtmlEncoding = "GB2312";
    soup = BeautifulSoup(respHtml, fromEncoding=songtasteHtmlEncoding);
    #<h1 class="h1user">crifan</h1>
    foundClassH2user = soup.findAll("a");
    foundClassH1user = soup.find(attrs={"id":"brand_tab_1_2"});
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
    # for link in fountbrand:
    # 	print "name:",link.get("href")
    # print "foundClassH1user=%s",foundClassH1user;
    # if(foundClassH1user):
    #     h1userStr = foundClassH1user.string;
    #     print "h1userStr=",h1userStr;
 
###############################################################################
if __name__=="__main__":
    main();