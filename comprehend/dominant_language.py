#!env python
"""
the demo APIs to show how to use Comprehend service to detect the dominant text
"""
import boto3

client = boto3.client('comprehend', region_name="us-east-1")

sampleText = []
file1 = open("./text/Australia_cn.txt", "r")
file2 = open("./text/Australia_en.txt", "r")
file3 = open("./text/Australia_fr.txt", "r")

sampleText.append(file1.read())
sampleText.append(file2.read())
sampleText.append(file3.read())

mixFile = open("./text/Australia_mix.txt", "r")

mixText = mixFile.read()

def detect_dominant_language():
    print "Sample text is:\n %s" %(mixText)
    languages = client.detect_dominant_language(Text=mixText)['Languages']
    print "Comprehend thinks the sample text's Language code is __ and a score of " + 10 * "_"
    for language in languages:
        print 13 * "\t" + language['LanguageCode'] + 4 * "\t" + str(language['Score'])

def batch_detect_dominant_language():
    languages = client.batch_detect_dominant_language(TextList=sampleText)['ResultList']
    for result in languages:
        print "Sample text is:\n%s" %(sampleText[result['Index']])
        print "Comprehend thinks the sample text's Language code is __ and a score of " + 10 * "_"
        for language in result['Languages']:
            print 13 * "\t" + language['LanguageCode'] + 4 * "\t" + str(language['Score'])
        print "\n"

if __name__ == "__main__":
    detect_dominant_language()
    batch_detect_dominant_language()
