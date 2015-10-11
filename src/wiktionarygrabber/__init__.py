# -*- coding: utf-8 -*-

"""
Add-on package initialization
"""

__all__ = ['entities', 'exporter', 'fetcher', 'parser']


import fetcher
import parser

VERSION = '0.1'


   
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

