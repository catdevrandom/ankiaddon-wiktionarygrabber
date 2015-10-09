'''
Created on 8 Oct 2015

@author: MBRANDAOCA
'''

class Exporter:
    # This class takes a word and generates a csv file with the fields
    # dutch, english, ipa, audio, gender, tag
    def __init__(self, verbose):
        self.verbose = verbose
    def export(self, word, output):
        if (self.verbose):
            print(word)        
            print('going to write word "%s" to file "%s"' % (word.entry,output))
        # generate line
        myLine = '%s, %s, %s\n' % (word.entry, word.audio, word.ipa)
        # write line to file "output"
        f = open(output, 'a')
        f.write(myLine)
        f.close()