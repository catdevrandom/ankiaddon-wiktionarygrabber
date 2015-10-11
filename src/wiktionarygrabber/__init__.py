# -*- coding: utf-8 -*-

"""
Add-on package initialization
"""
import logging

logger = logging.getLogger('ankiwiktionarygrabber')

__all__ = ['entities', 'exporter', 'fetcher', 'parser']


#import entities
import fetcher
import parser

VERSION = '0.1'

#import bs4

   
def get_wiktionary_fields(entry, language):
    """
    Fetch Wiktionary info about the work and update fields
    """

    
    myFetcher = fetcher.Fetcher()
    fetchedPage = myFetcher.fetch(entry)
            
    if fetchedPage:
        myParser = parser.Parser()
        myParser.setLanguage(language)
        myParser.setWordName(entry)
        extractedWord = myParser.extractData(fetchedPage)
        return extractedWord
    else:
        return False

