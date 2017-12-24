#!env python
# -*- coding: utf-8 -*-

"""
Output:	    sample Rate	                 speech Marker
JSON	       NA	                         sentence ssml viseme word
mp3	        8000, 16000, 22050*	         NA
pcm	        8000, 16000*	               NA
ogg_vorbis	8000, 16000, 22050*	         NA
:return:
"""
import boto3
import time

client = boto3.client("polly", region_name="us-east-1")

english_text = r"""
Amazon Polly is a service that turns text into lifelike speech, allowing you to create applications that talk, and build entirely new categories of speech-enabled products. Amazon Polly is a text-to-speech service that uses advanced deep learning technologies to synthesize speech that sounds like a human voice.

With dozens of lifelike voices across a variety of languages, you can select the ideal voice and build speech-enabled applications that work in many different countries.
"""

french_text = r"""
Amazon Polly est un service qui transforme le texte en un discours réaliste, vous permettant de créer des applications qui parlent et de créer de toutes nouvelles catégories de produits vocaux. Amazon Polly est un service de synthèse vocale qui utilise des technologies avancées d'apprentissage en profondeur pour synthétiser un discours qui sonne comme une voix humaine.

Avec des dizaines de voix réalistes à travers une variété de langues, vous pouvez sélectionner la voix idéale et construire des applications vocales qui fonctionnent dans de nombreux pays différents.
"""

def play_audio_on_mac(audio_file):
    import subprocess
    subprocess.call(["afplay", audio_file])

def english_mp3():
    # use English ssml to generate pcm
    # use English text string to generate 'sentence'|'ssml'|'viseme'|'word'
    # change the sample rate for mp3 and ogg_vorbis


    response = client.synthesize_speech(
        OutputFormat='mp3',
        Text=english_text,
        VoiceId='Russell'
    )
    file = "./media/test_en.mp3"
    mp3file = open(file, "w")
    mp3file.write(response['AudioStream'].read())
    mp3file.flush()
    mp3file.close()
    play_audio_on_mac(file)

def french_mp3():
    response = client.synthesize_speech(
        OutputFormat='mp3',
        Text=french_text,
        VoiceId='Mathieu'
    )
    file = "./media/test_fr.mp3"
    mp3file = open(file, "w")
    mp3file.write(response['AudioStream'].read())
    mp3file.flush()
    mp3file.close()
    play_audio_on_mac(file)

def voice_with_lexicon():
    import lexicon_management
    lexicon_management.create_lexicon()

    sample_text_1 = "voice with one lexicon: The WHO is affiliated with the UN, it's found in 1946"
    sample_text_2 = "voice with two lexicons: The WHO is affiliated with the UN, it's found in 1946"

    time.sleep(5)
    response = client.synthesize_speech(
        LexiconNames=['lexicondemo1'],
        OutputFormat='mp3',
        Text=sample_text_1,
        VoiceId='Joanna'
    )

    file = "./media/output.mp3"
    mp3file = open(file, "w")
    mp3file.write(response['AudioStream'].read())
    mp3file.flush()
    mp3file.close()
    play_audio_on_mac(file)

    response = client.synthesize_speech(
        # multiple lexicons, first one overwrites the second one.
        LexiconNames=["lexicondemo2", "lexicondemo1"],
        OutputFormat='mp3',
        Text=sample_text_2,
        VoiceId='Joanna'
    )

    mp3file = open(file, "w")
    mp3file.write(response['AudioStream'].read())
    mp3file.flush()
    mp3file.close()
    play_audio_on_mac(file)

    lexicon_management.delete_lexicon()

if __name__=="__main__":
    voice_with_lexicon()

