# Anki2 Add-on -- Wiktionary Grabber

This is an add-on to retrieve some fields from Wiktionary to enrich Anki2 cards.

## Requirements

You need a copy of Beautiful Soup 4. Download the latest version here:
http://www.crummy.com/software/BeautifulSoup/bs4/download/

Unzip the code and copy the folder "bs4" to the Anki Add-On folder.

## Installation

Download the code and copy the contents of the "src" folder to the Anki Add-On folder.

## Usage

Currently implemented only for Dutch words.

Requires a field called "Dutch" (observe capitalization) containing a single Dutch word to be looked up at Wiktionary.

It updates the fields below:

- "IPA" with the IPA pronunciation
- "Gender" with a letter indicating the gender of the word (if available): masculine, feminine, neutral
- "Plural" with an indication about how to form the plural of the word

The plugin adds a button to the Notes browser and Notes Editor (it has a "W" in it). Select a note, select a field, and click the button. If the required fields are available, they will be updated. If the plugin has trouble finding the work in Wiktionary, it will throw a warning.


## More information
 
To learn more about Anki, please see the website at:

http://ankisrs.net/
