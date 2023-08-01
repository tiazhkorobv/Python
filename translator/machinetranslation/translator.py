'''This module use Mymemory Translator API for translation'''
import sys
from deep_translator import MyMemoryTranslator

def english_to_french():
    '''Function of translation En to Fr'''
    fr_translator = MyMemoryTranslator(source='en-GB', target='fr-FR').translate(text='Hello')

    # Print the translated text, handling encoding errors
    try:
        print(fr_translator)
    except UnicodeEncodeError:
        # Handle encoding errors by printing to sys.stdout with utf-8 encoding
        sys.stdout.buffer.write(fr_translator.encode('utf-8'))
        sys.stdout.buffer.write(b'\n')
    return fr_translator

english_to_french()# Call the english_to_french function

def english_to_german():
    '''Function of translation En to De'''
    de_translator = MyMemoryTranslator(source='en-GB', target='de-DE').translate(text='Hello')

    # Print the translated text, handling encoding errors
    try:
        print(de_translator)
    except UnicodeEncodeError:
        # Handle encoding errors by printing to sys.stdout with utf-8 encoding
        sys.stdout.buffer.write(de_translator.encode('utf-8'))
        sys.stdout.buffer.write(b'\n')
    return de_translator

english_to_german()# Call the english_to_german function
