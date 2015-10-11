'''
Created on 8 Oct 2015

@author: MBRANDAOCA
'''
from __future__ import print_function
import sys
def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)
    
import re
from .entities import Word
import pprint

class DutchParser:
    def __init__(self, wordName, sourceText, verbose):
        self.verbose = verbose
        self.wordName = wordName
        self.sourceText = sourceText
        self.myWord = Word(self.wordName)
        self.myWord.audio = ''
        self.myWord.ipa = ''
        self.myWord.gender = ''
        self.myWord.plural = ''
        self.myWord.diminutive = ''
        self.myWord.classes = {}

    def extractData(self):
        if (self.verbose):
            warning(self.sourceText)
        self.getPronunciation()
        self.getWordClasses()
        if (self.verbose):
            pprint.pprint(self.myWord.classes)
        for item in self.myWord.classes.keys():
            if (item == 'Noun'):
                self.getNoun()
        return self.myWord

    def getPronunciation(self):
        self.myWord.ipa = ''
        self.myWord.audio = ''
        # Fetch Pronunciation
        pronunciationMatch = re.search('={3,4}\s*Pronunciation\s*={3,4}(.*?)={3,4}[^=]+={3,4}', self.sourceText, re.I|re.M|re.S)
        
        if pronunciationMatch:
            warning('pronunciation match')
            pronunciationText = pronunciationMatch.group(1)
            ipaMatch = re.search('.*?\{\{IPA\|([^}]+)\}\}', pronunciationText, re.I|re.M|re.S)
            if ipaMatch:
                ipaFull = ipaMatch.group(1)
                ipaParts = ipaFull.split('|')
                for item in ipaParts:
                    if re.match('/([^/]+)/', item, re.S|re.M):
                        self.myWord.ipa = item
                
            audioMatch = re.search('.*?\{\{audio\|([^}]+)\}', pronunciationText, re.I|re.M|re.S)
            if audioMatch:
                audioFull = audioMatch.group(1)
                audioParts = audioFull.split('|')
                for item in audioParts:
                    if (re.match('[^.]+\.[a-z]{3,4}', item, re.I|re.M|re.S)):
                        self.myWord.audio = item
            return True
        else:
            warning('no pronunciation match')
            return False
        

    def getWordClasses(self):
        #Get all word classes
        word_classes = {}
        matchClasses = re.finditer('={3,4}\s*(Noun|Adjective|Adverb|Preposition|Article|Numeral|Pronoun|Verb|Postposition|Conjunction|Interjection)\s*={3,4}(.+?)(={3,4}\s*|$)', self.sourceText, re.I|re.S)
        if matchClasses:
            for item in matchClasses:
                warning(item.group(1))
                warning(item.group(2))
                if item.group(1) not in word_classes:
                    word_classes[item.group(1)] = item.group(2)
                else:
                    word_classes[item.group(1)+'-2'] = item.group(2) #this needs fixing. allow for more than one entry in each word class
            self.myWord.classes = word_classes
            if self.verbose:
                warning(word_classes)
        else:
            if self.verbose:
                warning('Could not find word classes list.')


                
    def getNoun(self):        
        #Gender
        #Plural
        #Diminutive
        #Dutch noun template: {{nl-noun|n|huizen|huisje}}        
        self.verbose=False
        nounContent = self.myWord.classes.get("Noun")
        if self.verbose:
            warning('noun content:----------------')
            warning(nounContent)
            warning('-------'*10)
        #Split the parameters
        matchParameters = re.search('\{\{([^}]+)\}\}', nounContent, re.S|re.I|re.M)
        if matchParameters:
            allParameters = matchParameters.group(1)
            allParameters = allParameters.split('|')
            if self.verbose:
                warning(allParameters)
            itemsToPutInTheEnd = []
            for item in allParameters:
                if item.find('=') > 0:
                    itemsToPutInTheEnd.append(item)
            for item in itemsToPutInTheEnd:
                allParameters.append(item)
                del allParameters[allParameters.index(item)]
            if len(allParameters)>1:
                self.myWord.gender = allParameters[1]
            if len(allParameters)>2:
                self.myWord.plural = allParameters[2]
            if len(allParameters)>3:
                self.myWord.diminutive = allParameters[3]
        else:
            warning('no match')        
        return False
            
    def getVerb(self):
        #If  verb,  verify  first  if  it  is  the  infinitive.  If  not,  ignore
     
        #From  verbs,  get  past  singular  and  past  participle
        return False

    def getAdverb(self):
        #From  adverb,  get  definition  only
        return False

    def getAdjective(self):                 
        #From  adjective,  get  comparative  and  superlative  and  definitions
        return False
                 
    def getPreposition(self):                 
        #From  prepositions,  get  definition  only
        return False
