#!/usr/bin/env python
#coding:utf-8

#script name check_web_stat.py

import socket #tcp建立socket连接用到

import re #正则表达式模块

import sys



def check_webserver(address, port, resource):

   #建立http请求串

   if not resource.startswith('/'): #判断是否以‘/’开头

       resource = '/' + resource

   request_string = "GET %s HTTP/1.1\r\nHost: %s\r\n\r\n" % (resource, address)

   print 'HTTP request:'

   print '|||%s|||' % request_string

    #创建一个 TCP socket

   s = socket.socket()

   print "Attempting to connect to %s on port %s" % (address, port)

   try:

       s.connect((address, port))

       print "Connected to %s on port %s" % (address, port)

       s.send(request_string)

       #获取前100个字节

       rsp = s.recv(100)

       print 'Received 100 bytes of HTTP response'

       print '|||%s|||' % rsp

   except socket.error, e:

       print "Connection to %s on port %s failed: %s" % (address, port, e)

       return False

   finally:

       #关闭socket连接

       print "Closing the connection"

       s.close()

   lines = rsp.splitlines() #将一个段落的字符串以行为单位分割成一个列表

   print 'First line of HTTP response: %s' % lines[0]

   try:

       version, status, message = re.split(r'\s+', lines[0], 2)

       print 'Version: %s, Status: %s, Message: %s' % (version, status, message)

   except ValueError:

       print 'Failed to split status line'

       return False

   if status in ['200', '301']:

       print 'Success - status was %s' % status

       return True

   else:

       print 'Status was %s' % status

       return False

if __name__ == '__main__':

   from optparse import OptionParser  #导入optionparser命令行工具模块

   parser = OptionParser()   #构造optionparser的对象

   parser.add_option("-a", "--address", dest="address", default='localhost',

                     help="ADDRESS for webserver", metavar="ADDRESS")

   parser.add_option("-p", "--port", dest="port", type="int", default=80,

                     help="PORT for webserver", metavar="PORT")

   parser.add_option("-r", "--resource", dest="resource", default='index.html',

                     help="RESOURCE to check", metavar="RESOURCE")

#往optionparser对象中增加option ：parser.add_option()

   (options, args) = parser.parse_args()  #调用optionparser的解析函数,在options中使用解析到的options，在args中使用其他的位置参数args

   print 'options: %s, args: %s' % (options, args)

   check = check_webserver(options.address, options.port, options.resource)

   print 'check_webserver returned %s' % check

   sys.exit(not check)

# python check_web.py -a www.baidu.com  -r index.php