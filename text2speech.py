import sys
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from pygame import mixer
import os
import json

with open('test.json') as file:
    data = json.load(file)

speakers = {
  'Filiz': ['tr-TR', 'Filiz'],
  'Zeina': ['arb', 'Zeina'],
  'Matthew':['en-US','Matthew'],
  'Mizuki':['ja-JP','Mizuki'],
  'Bianca':["it-IT","Bianca"],
  'Tatyana':["ru-RU","Tatyana"],
  'Aditi':["hi-IN","Aditi"]
}

text = sys.argv[1]
speaker = sys.argv[2]

def play_audio():
    mixer.init(devicename = 'CABLE Input (VB-Audio Virtual Cable)') # Initialize it with the correct device
    mixer.music.load("output.mp3") # Load the mp3
    mixer.music.play()

    while mixer.music.get_busy():
            pass

        # stop the mixer and unload the music
    mixer.music.stop()
    mixer.music.unload()

        # delete the file after it has been played

    
def speak(text, language_code, voice_id):
    try:
        polly_client = boto3.Session(
            aws_access_key_id=data['aws_access_key_id'],
            aws_secret_access_key=data['aws_secret_access_key'],
            region_name='us-east-1').client('polly')

        response = polly_client.synthesize_speech(
            Text=text,
            OutputFormat='mp3',
            VoiceId=voice_id,
            LanguageCode=language_code
        )

        with open('output.mp3', 'wb') as f:
            f.write(response['AudioStream'].read())

        play_audio()

    except (BotoCoreError, ClientError) as error:
        print(error)

def main(text, language, name):
    speak(text, language, name)


main(text, speakers[speaker][0], speakers[speaker][1])
