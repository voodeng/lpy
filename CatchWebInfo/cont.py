#!/usr/bin/python
# -*- coding: utf-8 -*-

 
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
    # foundp = fountbrand.find(attrs={"class":"list-sptitle"})
    weight = soup.find(attrs={"id":"Product_Weight"});
    coods = soup.find(attrs={"id":"productCoodsNo"});
    price = soup.find(attrs={"id":"productShopPrice"});

    fbranda = fountbrand.findAll(attrs={"class":"list-sptitle"});

    # print coods.string," > ",price.string," > ", weight.string;
    fp = open("weight.txt","a");
    lcs = coods.string, weight.string;
    print >> fp, coods.string," > ",price.string," > ", weight.string;

    fp.close(); #关闭文件  


def redwe():
    for line in open("value.txt"):    
        main(line);

###############################################################################
if __name__=="__main__":
    # main();
    redwe();