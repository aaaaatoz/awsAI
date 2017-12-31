#!env python

"""
demo to show API describe voice
"""

import boto3

def print_voice_matrix():
    client = boto3.client("polly", region_name="us-east-1")
    response = client.describe_voices()
    print "%15s%15s%15s%25s%15s" %("VoiceID", "VoiceName", "Gender", "Language", "LanguageCode")
    for voice in response[u'Voices']:
        print "%15s%15s%15s%25s%15s" % (voice["Id"], voice["Name"], voice["Gender"], voice[u'LanguageName'], voice[u'LanguageCode'])

if __name__=="__main__":
    # print_voice_matrix()
    pass