# -*- coding: utf-8 -*-
'''
Created on 8 Oct 2015

@author: MBRANDAOCA
'''
from __future__ import print_function
import sys
def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)

#try:
#    from urllib.parse import urlparse, urlencode
#    from urllib.request import urlopen, Request
#    from urllib.error import HTTPError
#except ImportError:
#    from urlparse import urlparse
#    from urllib import urlencode
#    from urllib2 import urlopen, Request, HTTPError
from urlparse import urlparse
from urllib import urlencode
from urllib2 import urlopen, Request, HTTPError
from bs4 import BeautifulSoup

class Fetcher:
    def __init__(self, verbose):
        self.url = 'http://en.wiktionary.org/w/index.php?title=Special:Export&action=submit'
        self.verbose = verbose
        self.parser = "html.parser"
        self.encoding = "utf-8"
        
    def fetch(self, word):
        values = {}
        values['pages'] = word
        values['catname'] = ''
        values['curonly'] = 1
        values['wpExportTemplates'] = 0
        values['wpDownload'] = 0
        data = urlencode(values)
        data = data.encode('utf-8')
        if self.verbose ==1:
            print('Fetching URL: ' + self.url)
        req = Request(self.url, data)
        response = urlopen(req)
        if self.verbose ==1:
            print('Received response.')
        the_page = BeautifulSoup(response.read().decode('utf-8', 'ignore'), self.parser, from_encoding=self.encoding)
        if the_page:    
            if self.verbose ==1:
                print('Got a page.')
            the_text = the_page.find('text') #Get the "text" tag in the Beautiful Soup
            if the_text:
                the_text = the_text.get_text() #Store it as unicode/str
                if self.verbose == 1:
                    print('Found the text tag.')
                    print('Type: ' + str(type(the_text)))
                    print('Content of text tag: '+ '-----'*10)
                    print(the_text)
                    print('-----'*10)
                    print('-----'*10)
                return the_text
            else:
                print('Did not get the text tag.')
                return False
        else:
            print('Did not get a page.')
            return False
