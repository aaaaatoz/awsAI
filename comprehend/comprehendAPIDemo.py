#!env python
"""

describe_topics_detection_job()


generate_presigned_url()
list_topics_detection_jobs()
start_topics_detection_job()
"""

import boto3

client = boto3.client('comprehend', region_name="us-east-1")
textList = []
textList.append("Grandpa was very proud of me when I got a promotion at work. He took me out to dinner to celebrate.")
textList.append("After Kylie had her heart broken by her ex-boyfriend, she felt so down and blue. I tried to cheer her up, but she just wants to be sad for awhile.")
textList.append("Australia has the world's 9th largest immigrant population, with immigrants accounting for 26% of the population.")

sampleText = []
file1 = open("./language/Australia_cn.txt", "r")
file2 = open("./language/Australia_en.txt", "r")
file3 = open("./language/Australia_fr.txt", "r")

sampleText.append(file1.read())
sampleText.append(file2.read())
sampleText.append(file3.read())



def get_all_files():
    pass

def detect_dominant_language():
    file = open("./language/Australia_cn.txt","r")
    content = file.read()
    client.detect_dominant_language(Text=content)

def batch_detect_dominant_language():
    content1 = file1.read()
    content2 = file2.read()
    content3 = file3.read()
    response = client.batch_detect_dominant_language(
        TextList=[
            content1, content2, content3
        ]
    )

def detect_sentiment():
    for text in textList:
        response = client.detect_sentiment(
            Text = text,
            LanguageCode='en'
        )
        print response[u'SentimentScore']

def batch_detect_sentiment():
    response = client.batch_detect_sentiment(
        TextList=textList,
        LanguageCode='en'
    )

def detect_entities():
    for text in sampleText:
        response = client.detect_entities(
            Text = text,
            LanguageCode='en'
        )
        print response

def detect_key_phrases():
    for text in sampleText:
        response = client.detect_key_phrases(
            Text=text,
            LanguageCode='en'
        )
        print response

def batch_detect_key_phrases():

    response = client.batch_detect_key_phrases(
        Text=textList,
        LanguageCode='en'
    )
    print response

if __name__ == "__main__":
    detect_entities()
