"""WatsoTranslator for IT final Project"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
""" This a Watson translator:
Translate english to french So that employees can understand customers
Translate french to english so that customers can use their mother language with the chatbot"""
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3 (version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url(url)

def english_to_french(englishtext):
    """ Translates english text to french"""
    #write the code here
    to_french = language_translator.translate(text=englishtext, model_id ='en-fr').get_result()
    french_text = to_french['translations'][0]['translation']
    return ": " + french_text

def french_to_english(frenchtext):
    """ French to English"""
    #write the code here
    to_english = language_translator.translate(text=frenchtext, model_id ='fr-en').get_result()
    english_text = to_english['translations'][0]['translation']
    return ": " + english_text
    