# -*- coding: utf-8 -*-

"""
Add-on package initialization
"""
from __future__ import print_function
import sys
def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)

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
    
    verbose = False
    
    myFetcher = fetcher.Fetcher(verbose)
    fetchedPage = myFetcher.fetch(entry)
            
    if fetchedPage:
        myParser = parser.Parser(verbose)
        myParser.setLanguage(language)
        myParser.setWordName(entry)
        extractedWord = myParser.extractData(fetchedPage)
        return extractedWord
    else:
        return False

