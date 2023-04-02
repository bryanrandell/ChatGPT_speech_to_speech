# Description: Convert text to speech using Google Cloud Text-to-Speech API and play it to the default audio device.
# Bryan Randell 2023

from google.cloud import texttospeech
import os
from pydub import AudioSegment
from pydub.playback import play
import io

# Set your Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/path/to/your/secret_gc_api_key_file.json"

voices_dict = {
    'en-US': {
        'FEMALE': {
            'voice_name_1': 'en-US-Wavenet-A',
            'voice_name_2': 'en-US-Wavenet-B',
            'voice_name_3': 'en-US-Wavenet-F',
        },
        'MALE': {
            'voice_name_1': 'en-US-Wavenet-C',
            'voice_name_2': 'en-US-Wavenet-D',
            'voice_name_3': 'en-US-Wavenet-E',
        },
    },
    'fr-FR': {
        'FEMALE': {
            'voice_name_1': 'fr-FR-Wavenet-A',
            'voice_name_2': 'fr-FR-Wavenet-B',
            'voice_name_3': 'fr-FR-Wavenet-D',
        },
        'MALE': {
            'voice_name_1': 'fr-FR-Wavenet-C',
            'voice_name_2': 'fr-FR-Wavenet-E',
            'voice_name_3': 'fr-FR-Wavenet-F',
        },
    },
}


# Function to convert text to audio using Google Cloud Text-to-Speech API and play it
def text_to_audio(text,
                  voice_name=voices_dict['fr-FR']['FEMALE']['voice_name_1'],
                  text_max_length=5000) -> None:
    if len(text) > text_max_length:
        raise ValueError('Text is too long, max length is {}'.format(text_max_length))
    else:
        client = texttospeech.TextToSpeechClient()

        input_text = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code=voice_name[:5],
            name=voice_name,
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        response = client.synthesize_speech(
            input=input_text, voice=voice, audio_config=audio_config
        )

        audio_data = io.BytesIO(response.audio_content)
        audio_segment = AudioSegment.from_file(audio_data, format='mp3')
        play(audio_segment)


# Main function to convert a string to audio and play it
def main_text_to_speech(text_input) -> None:
    text_to_audio(text=text_input)


if __name__ == '__main__':
    text = """Bonjour, je suis en train de convertir ce texte en discours en utilisant Google Cloud Text-to-Speech API 
    et en le jouant directement."""
    voice_name = voices_dict['fr-FR']['FEMALE']['voice_name_1']
    main_text_to_speech(text)
