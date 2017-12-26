#!env python
"""
the demo APIs to show how to use Comprehend service to detect the entities
"""
import boto3

client = boto3.client('comprehend', region_name="us-east-1")

sampleText = []
file1 = open("./text/Albert_Einstein_en.txt", "r")
file2 = open("./text/Australia_en.txt", "r")
file3 = open("./text/Amazon_en.txt", "r")

sampleText.append(file1.read())
sampleText.append(file2.read())
sampleText.append(file3.read())


def detect_key_phrases():
    print "Sample text is:\n %s\n" %(sampleText[0])
    key_phrases = client.detect_key_phrases(
        Text=sampleText[0],
        LanguageCode = "en"
    )['KeyPhrases']
    print "It contains key phrases:\n%20s\t\t%14s\t\t%10s\t\t%10s" % (
    "Text", "Score", "BeginOffset", "EndOffset")
    for key_phrase in key_phrases:
        print "%20s\t\t%1.12f\t\t%10d\t\t%10d" % (
            key_phrase['Text'], key_phrase['Score'], key_phrase['BeginOffset'], key_phrase['EndOffset'])


def batch_detect_key_phrases():
    key_phrases = client.batch_detect_key_phrases(
        TextList=sampleText,
        LanguageCode="en"
    )['ResultList']
    print key_phrases
    for result in key_phrases:
        print "Sample text is\n: %s" %(sampleText[result['Index']])
        print "It contains key phrases:\n%20s\t\t%14s\t\t%10s\t\t%10s" % ("Text", "Score", "BeginOffset", "EndOffset")
        for key_phrase in result['KeyPhrases']:
            print "%20s\t\t%1.12f\t\t%10d\t\t%10d" % (key_phrase['Text'], key_phrase['Score'], key_phrase['BeginOffset'], key_phrase['EndOffset'])
        print "\n"

if __name__ == "__main__":
    # detect_key_phrases()
    # batch_detect_key_phrases()
    pass
