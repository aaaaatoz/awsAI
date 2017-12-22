#!env python

"""
Output:	    sample Rate	                 speech Marker
JSON	       NA	                         sentence ssml viseme word
mp3	        8000, 16000, 22050*	         NA
pcm	        8000, 16000*	               NA
ogg_vorbis	8000, 16000, 22050*	         NA
:return:
"""
import boto3


def play_audio_on_mac(audio_file):
    import subprocess
    subprocess.call(["afplay", audio_file])

def syntheesize_speech_demo():
    # use English text file to generate mp3
    # use French text file with French void to generate mp3
    # use English ssml to generate pcm
    # use English text string to generate 'sentence'|'ssml'|'viseme'|'word'
    # change the sample rate for mp3 and ogg_vorbis
    # use English text with one LexiconName
    # use English text with three LexiconName
    client = boto3.client("polly", region_name="us-east-1")
    response = client.synthesize_speech(
        OutputFormat='mp3',
        Text='This is Australia, my name is Rafa',
        VoiceId='Russell'
    )
    mp3file = open("test.mp3", "w")
    mp3file.write(response['AudioStream'].read())
    mp3file.flush()
    mp3file.close()
    play_audio_on_mac("./test.mp3")
    pass

if __name__=="__main__":
    syntheesize_speech_demo()

