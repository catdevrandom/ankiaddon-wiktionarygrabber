'''
Created on 8 Oct 2015

@author: MBRANDAOCA
'''
from __future__ import print_function
def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)
    
class Word():
    def __init__(self, entry):
        self.entry = entry
        self.audio = ''
        self.ipa = ''
        self.gender = ''
        self.plural = ''
        self.diminutive = ''
        self.representation = '<Word: entry=%s, audio=%s, ipa=%s, gender=%s, plural=%s, diminutive=%s, classes=%s>' 
        self.classes = {}
    def __repr__(self):
        myOutput = self.representation % (self.entry, self.audio, self.ipa, self.gender, self.plural, self.diminutive, list(self.classes.keys()))
        return myOutput
    def __str__(self):
        myOutput = self.representation % (self.entry, self.audio, self.ipa, self.gender, self.plural, self.diminutive, list(self.classes.keys()))
        return myOutput
    def string(self):
        myOutput = self.representation % (self.entry, self.audio, self.ipa, self.gender, self.plural, self.diminutive, list(self.classes.keys()))
        return myOutput
    
    