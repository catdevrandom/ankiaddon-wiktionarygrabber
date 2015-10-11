'''
Created on 8 Oct 2015

@author: MBRANDAOCA
'''
import logging

logger = logging.getLogger('ankiwiktionarygrabber')
    
from dutchparser import DutchParser
import re

class Parser:
    def __init__(self):
        pass
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
                myParser = DutchParser(self.wordName, languageData)
                return myParser.extractData()
            else:
                return False
        else:
            logger.error('Sorry, the parser for language "%s" has not been implemented yet.')
            return False
        
    def extractLanguageData(self, fetchedText):
        # Extract only the relevant section from the desired language
        regex = '==%s==(.*?)(----\s*==[^=]+==|</text>|\{\{bottom\}\}|$)' % self.language
        matches = re.search(regex, fetchedText, re.I|re.S)
        if not matches:
            logger.error('Did not find target language.')
            return False
        else:
            targetText = matches.group(1)
            logger.info('Found word in target language')
            return targetText
        
