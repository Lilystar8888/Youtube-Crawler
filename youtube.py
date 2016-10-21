# -*- coding: UTF-8 -*-
import os, sys, urllib, urllib2, traceback
import urllib
from bs4 import BeautifulSoup
from time import strftime
import re
import json

def print_help():
	print 'python youtube.py [-h] [-n] keyword'
	print '-h     print help'
	print '-n     number of search result. default is 5' 
	print '-p     page that you parse'
	print "-------------------------------------------------------"
	print 'Youtube contains at most 20 results in a page. And 50 pages at most for any search.'
	print 'Therefore, n<=20, p<=50'

reload(sys)
sys.setdefaultencoding('utf8')

#convert sys.argv to string
SearchString=''
NumberOutput=5
SearchPage=1

if sys.argv[1]=="-h":
	if len(sys.argv)==2:
		print_help()
		sys.exit()
	else:
		print "Wrong Argument Input: Please Check Below And Try Again:"
		print "-------------------------------------------------------"
		print_help()
		sys.exit()

KeywordStartPosition=1

for j in range (1,len(sys.argv),1):
	if sys.argv[j]=="-n":
		if sys.argv[j+1].isdigit()==True:
			if int(sys.argv[j+1])<=20 and int(sys.argv[j+1])>0:
				NumberOutput=int(sys.argv[j+1])
				KeywordStartPosition=KeywordStartPosition+2
			else:
				print "Wrong Argument Input: Please Check Below And Try Again:"
				print "-------------------------------------------------------"
				print_help()
				sys.exit()
		else:
			print "Wrong Argument Input: Please Check Below And Try Again:"
			print "-------------------------------------------------------"
			print_help()
			sys.exit()
	elif sys.argv[j]=="-p":
		if sys.argv[j+1].isdigit()==True:
			if int(sys.argv[j+1])<=50 and int(sys.argv[j+1])>0:
				SearchPage=int(sys.argv[j+1])
				KeywordStartPosition=KeywordStartPosition+1
			else:
				print "Wrong Argument Input: Please Check Below And Try Again:"
				print "-------------------------------------------------------"
				print_help()				
				sys.exit()
		else:
			print "Wrong Argument Input: Please Check Below And Try Again:"
			print "-------------------------------------------------------"
			print_help()			
			sys.exit()
	elif sys.argv[j]=="-h":
		print "Wrong Argument Input: Please Check Below And Try Again:"
		print "-------------------------------------------------------"
		print_help()			
		sys.exit()
	elif sys.argv[j].isdigit()==False:
		break
for i in range (KeywordStartPosition,len(sys.argv),1):
	SearchString=SearchString+sys.argv[i]+" "



url='https://www.youtube.com/results?search_query='+SearchString+'&page='+str(SearchPage)
first_page='https://www.youtube.com/results?search_query='+SearchString+'&page='
search_result=urllib.urlopen(url)

soup=BeautifulSoup(search_result)
ResultItem=soup.findAll('ol', {"class":"item-section" })


#while(1):
	#ResultItem=soup.findAll('ol'.{"class":"item-section"})
result_content=soup.findAll('div', {"class":"yt-lockup-content" })
result_description_list=soup.findAll('div', {"class":"yt-lockup-description"})
result_title_list=soup.findAll('a', {"class":"yt-uix-tile-link" })


NonDescIdx=[]
if NumberOutput>len(result_title_list):
	NumberOutput=len(result_title_list)
	print "Exists Only %d Search Result(s) In Page %d:" %( NumberOutput, SearchPage )
for i in range(0,NumberOutput,1):
	if result_content[i].findAll('ol', {"class":"yt-lockup-playlist-items" })!=[]:
		NonDescIdx=NonDescIdx+[i]
	elif result_content[i].findAll('div', {"class":"yt-lockup-description"})==[]:
		NonDescIdx=NonDescIdx+[i]
count=0
	
for i in range(0,NumberOutput,1):
	url='https://www.youtube.com'+ result_title_list[i]['href']
	EncodedURL=urllib.quote_plus(url)
	urlfit="https://developer.url.fit/api/shorten?long_url="+EncodedURL

	response = urllib.urlopen(urlfit)
	ShortenURL = json.loads(response.read())

	print result_title_list[i]['title']+' (https://url.fit/'+ ShortenURL['url']+')'
	

	if (i in NonDescIdx)==True:
		print "No Description"
		count=count+1
	else:
		Desc=result_description_list[i-count].text
		print Desc

	SearchContent=urllib.urlopen(url)
	SearchContentHtml=BeautifulSoup(SearchContent)
	Like=SearchContentHtml.findAll('button', {"class":"like-button-renderer-like-button" })
	Dislike=SearchContentHtml.findAll('button', {"class":"like-button-renderer-dislike-button" })
	print "Like: %s, Dislike: %s" %(Like[0].span.text, Dislike[0].span.text)
	print ""
	
		
		
		


