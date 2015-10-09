'''
Created on 8 Oct 2015

@author: MBRANDAOCA
'''
from __future__ import print_function
def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)
    
from dutchparser import DutchParser
import re

class Parser:
    def __init__(self, verbose):
        self.verbose = verbose
    def setLanguage(self, language):
        self.language = language
    def setWordName(self, wordName):
        self.wordName = wordName
    def extractData(self, fetchedText):
        #extract the text
        languageData = self.extractLanguageData(fetchedText)
        #construct the language-specific parser
        if (self.language == 'Dutch'):
            if languageData:
                myParser = DutchParser(self.wordName, languageData, self.verbose)
                return myParser.extractData()
            else:
                return False
        else:
            print('Sorry, the parser for language "%s" has not been implemented yet.')
            return False
        
    def extractLanguageData(self, fetchedText):
        # Extract only the relevant section from the desired language
        regex = '==%s==(.*?)(----\s*==[^=]+==|</text>|\{\{bottom\}\}|$)' % self.language
        matches = re.search(regex, fetchedText, re.I|re.S)
        if not matches:
            print('Did not find target language.')
            return False
        else:
            targetText = matches.group(1)
            if self.verbose:
                print('Found word in target language')
                #print(type(targetText))
            return targetText
        