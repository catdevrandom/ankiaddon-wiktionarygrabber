# -*- coding: utf-8 -*-
'''
Created on 8 Oct 2015

@author: MBRANDAOCA
'''
import logging

logger = logging.getLogger('ankiwiktionarygrabber')


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
    def __init__(self):
        self.url = 'http://en.wiktionary.org/w/index.php?title=Special:Export&action=submit'
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
        logger.info('Fetching URL: ' + self.url)
        req = Request(self.url, data)
        response = urlopen(req)
        logger.info('Received response.')
        the_page = BeautifulSoup(response.read().decode('utf-8', 'ignore'), self.parser, from_encoding=self.encoding)
        if the_page:    
            logger.info('Got a page.')
            the_text = the_page.find('text') #Get the "text" tag in the Beautiful Soup
            if the_text:
                the_text = the_text.get_text() #Store it as unicode/str
                logger.info('Found the text tag.')
                logger.info('Type: ' + str(type(the_text)))
                logger.info('Content of text tag: '+ '-----'*10)
                logger.info(the_text)
                logger.info('-----'*10)
                logger.info('-----'*10)
                return the_text
            else:
                logger.warning('Did not get the text tag.')
                return False
        else:
            logger.warning('Did not get a page.')
            return False
