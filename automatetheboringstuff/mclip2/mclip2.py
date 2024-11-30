"""
Extending the Multi-Clipboard
Extend the multi-clipboard program in this chapter so that it has a delete <keyword>
command line argument that will delete a keyword from the shelf.
Then add a delete command line argument that will delete all keywords.
"""

#! python3

# mclip.py -A multi-clipboard program.
import os
from pathlib import Path as path
import pyperclip
import shelve
import sys

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

keyphrases = shelve.open('keyphrases')

if 'text' not in keyphrases:
    keyphrases['text'] = TEXT

text_dict = keyphrases['text']

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()


keyphrase = sys.argv[1]  # first command line arg is the keyphrase

if keyphrase == '--delete':
    p = path.cwd()
    saved_phrases_list = list(p.glob('keyphrases.*'))
    saved_phrases_path = str(saved_phrases_list[0])
    keyphrases.close()
    os.remove(saved_phrases_path)
    print('delete successful')
elif keyphrase == 'delete':
    phrase = sys.argv[2]
    if phrase in text_dict:
        del text_dict[phrase]
        keyphrases['text'] = text_dict
        print(f"'{phrase}' deleted successfully")
    else:
        print(f"'{phrase}' does not exist")
elif keyphrase in text_dict:
    pyperclip.copy(text_dict[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)

keyphrases.close()
