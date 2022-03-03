import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION_LT='2018-05-01'
authenticator=IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(version=VERSION_LT,authenticator=authenticator)
lt.set_service_url(url)

def english_to_french(english_text):
    enfr_translation=lt.translate(text=english_text,model_id='en-fr').get_result()
    enfr_translation_str=enfr_translation['translations'][0]['translation']
    print(enfr_translation_str)
    return enfr_translation_str
def french_to_english(french_text):
    fren_translation=lt.translate(text=french_text,model_id='fr-en').get_result()
    fren_translation_str=fren_translation['translations'][0]['translation']
    print(fren_translation_str)
    return fren_translation_str 
#english_to_french("hello")
#french_to_english("bonjour")
