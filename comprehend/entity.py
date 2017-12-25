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


def detect_entities():
    print "Sample text is:\n %s\n" %(sampleText[0])
    entities = client.detect_entities(
        Text=sampleText[0],
        LanguageCode = "en"
    )['Entities']
    print "It contains entities:\n%20s\t\t%10s\t\t%14s\t\t%10s\t\t%10s" %("Text", "Type", "Score", "BeginOffset", "EndOffset")
    for entity in entities:
        print "%20s\t\t%10s\t\t%1.12f\t\t%10d\t\t%10d" %(entity['Text'], entity['Type'], entity['Score'],  entity['BeginOffset'], entity['EndOffset'])

def batch_detect_entities():
    entities = client.batch_detect_entities(
        TextList=sampleText,
        LanguageCode="en"
    )['ResultList']
    for result in entities:
        print "Sample text is\n: %s" %(sampleText[result['Index']])
        print "It contains entities:\n%20s\t\t%10s\t\t%14s\t\t%10s\t\t%10s" % ("Text", "Type", "Score", "BeginOffset", "EndOffset")
        for entity in result['Entities']:
            print "%20s\t\t%10s\t\t%1.12f\t\t%10d\t\t%10d" % (entity['Text'], entity['Type'], entity['Score'], entity['BeginOffset'], entity['EndOffset'])
        print "\n"

if __name__ == "__main__":
    #detect_entities()
    batch_detect_entities()
