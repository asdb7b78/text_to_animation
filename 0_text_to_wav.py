"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech
import argparse

parser = argparse.ArgumentParser(description='Without option argument, it will not run properly.')
parser.add_argument('-n', '--name', action='store', default='output', help="name of output .wav file")
args = parser.parse_args()

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
print("Text want to transform:")
synthesis_input = texttospeech.SynthesisInput(text=input())

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open(args.name + ".wav", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "'+ args.name +'.wav"')
