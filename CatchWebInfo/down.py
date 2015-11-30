#!/usr/bin/python
# -*- coding: utf-8 -*-

#---------------------------------import---------------------------------------
import urllib2;
import re;
from BeautifulSoup import BeautifulSoup;
 
#------------------------------------------------------------------------------
def downs(brands):
    brand = urllib2.quote(brands)
    
    userMainUrl = "http://www.hznzcn.com/page-yyrz.html?q_day=2014-12-11&q_name="+ brand;
    print userMainUrl;
    req = urllib2.Request(userMainUrl);
    resp = urllib2.urlopen(req);
    respHtml = resp.read();
    #print "respHtml=",respHtml; # you should see the ouput html

    songtasteHtmlEncoding = "GB2312";
    soup = BeautifulSoup(respHtml, fromEncoding=songtasteHtmlEncoding);

    
    fbranda = soup.findAll(attrs={"class":"box"});
    fp = open("down2.txt","a") #打开一个文本文件
    fp.write("\n");
    # print fbranda
    for link in fbranda:
       l=  link.find(attrs={'class':'name'})
       op=  link.find(attrs={'class':'operating'})
       print l.text+ " > " + op.text
       # ks = str(l.text+ " > " + op.text)
       print >> fp, l.text.encode('utf-8')+ " > " + op.text.encode('utf-8')

    fp.close();

def redwe():
    for line in open("brands.txt"):   
    	print line; 
    	lx = line.strip();
        downs(lx);


###############################################################################
if __name__=="__main__":
    redwe();