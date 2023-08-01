'''This module use GoogleTranslate API for translation'''
import sys
from deep_translator import GoogleTranslator

LANG1 = 'en'
TEXT1 = 'Hello'
LANG2 = 'de'
TEXT2 = 'Hallo'
T_LANG = 'fr'

translator = None
# Use GoogleTranslator to translate the TEXT from English to French

# def en_translated(TEXT, LANG1, T_LANG):
#     global en_translator
#     en_translator = GoogleTranslator(source=LANG1, target=T_LANG).translate(TEXT)
#     return en_translator

def translated(text, source, target):
    global translator
    translator = GoogleTranslator(source=source, target=target).translate(text)
    return translator


# Call the en_translated function to update the en_translator variable
translated(TEXT1, LANG1, T_LANG)

# Print the translated text, handling encoding errors
try:
    print(translator)
except UnicodeEncodeError:
    # Handle encoding errors by printing to sys.stdout with utf-8 encoding
    sys.stdout.buffer.write(translator.encode('utf-8'))
    sys.stdout.buffer.write(b'\n')
    
# Call the en_translated function to update the ge_translator variable
translated(TEXT2, LANG2, T_LANG)

# Print the translated text, handling encoding errors
try:
    print(translator)
except UnicodeEncodeError:
    # Handle encoding errors by printing to sys.stdout with utf-8 encoding
    sys.stdout.buffer.write(translator.encode('utf-8'))
    sys.stdout.buffer.write(b'\n')