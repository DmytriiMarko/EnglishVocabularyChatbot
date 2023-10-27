from gtts import gTTS
from random import randint
from telegraph import Telegraph
from config import telegraph_api
from utils import uk_dict


def get_voice(word: str) -> str:
    # Generates a name for the audio file
    name = str(randint(1000000, 9999999)) + ".mp3"

    # Voices the text and saves the result
    tts = gTTS(text=word, lang='en')
    tts.save(name)

    # Returns name of the audio file
    return name


def create_dictionary(list_of_words) -> str:
    # Generates HTML code for a page
    words = ''.join([f'<p><strong>{i[2]}:</strong> {i[3]}</p>' for i in list_of_words])

    # Sends a request to API and generates a dictionary page
    telegraph = Telegraph(telegraph_api)
    response = telegraph.create_page(
        title=uk_dict['your_dict'],
        html_content=words
    )

    # Returns a link to the created dictionary
    return response['url']
