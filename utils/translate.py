import requests
import uuid
from config import translate_key

# Link to external API handler
constructed_url = "https://api.cognitive.microsofttranslator.com/translate"

# Specify which version of API we are using, and the language codes of the languages we want to translate into
params = {
    'api-version': '3.0',
    'to': ['en', 'uk']
}

headers = {
    'Ocp-Apim-Subscription-Key': translate_key,
    'Ocp-Apim-Subscription-Region': "northeurope",
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}


def translate(word: str) -> tuple:
    try:
        # Create a query to the API, and process the result
        response = requests.post(constructed_url, params=params, headers=headers, json=[{'text': word}])
        response.raise_for_status()
        translations = response.json()[0].get('translations', [])

        # If it returned text in the 2 translations we need, return the result
        if len(translations) == 2:
            return translations[0]['text'].capitalize(), translations[1]['text'].capitalize()

    except requests.RequestException:
        return None, None  # Returns None, None if an error occurred
