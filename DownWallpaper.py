#coding=utf-8

import urllib
import urllib2
import cookielib
from lxml import etree
import json
import sys
import os


def getPhotoList(url):

	dicPath = '/Users/huajianma/Pictures/ACWallpaper'
    # if not os.path.exists(dicPath):
    #     os.makedirs(dicPath)

	# proxy_handler 		= urllib2.ProxyHandler({"https":"https://huafenr.com/f/a903c12da03e0d3f40be"})
	# # null_proxy_handler  = urllib2.ProxyHandler({})
	# opener 				= urllib2.build_opener(proxy_handler)
	# urllib2.install_opener(opener)#全局
 #    # opener = urllib2.build_opener(null_proxy_handler)


	userAgent	= 	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
	headers		=	{
						'User-Agent':userAgent,
						'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
						'authorization':'Bearer def5b99dc6ec754bee5891044243eea0f021af474f74a465f3c508fe9a7415e6'
					}
	data		=	urllib.urlencode({})
	request 	=	urllib2.Request(url+'?'+data,headers=headers)

	try:
		print "开始访问unsplash.com"
		response 	= 	urllib2.urlopen(request)
		body = response.read().decode('utf-8');
		body = json.loads(body)
		# print body
		# return;

		for wallpaperItem in body:

			print '===='*10

			file_name 		=	 wallpaperItem['id']# + '.jpg'
			img_url			=	 wallpaperItem['links']['download']

			print file_name + "\n" + img_url

			path = dicPath + '/' + file_name
			if os.path.exists(path):
				print('重复'+str(file_name))
				pass
			else:
				print('下载'+str(file_name))
				tempResponse = urllib2.urlopen(urllib2.Request(img_url))
				img_data = tempResponse.read()
				print('保存'+str(file_name))
				output = open(path, 'wb')
				output.write(img_data)
				output.close()


	except urllib2.URLError, e:
		print 'error - %d' % (e.code)

	# return liveList




print getPhotoList("https://unsplash.com/napi/photos?page=1&per_page=30&order_by=latest")





