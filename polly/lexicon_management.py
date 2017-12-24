#!env python

import boto3
import sys
import botocore.errorfactory
import time

def list_lexicon():
    client = boto3.client("polly", region_name="us-east-1")
    response = client.list_lexicons()
    print ("\nYou have %d in your polly." %len(response['Lexicons']))
    for lexicon in response['Lexicons']:
        print lexicon['Name']

def create_lexicon():
    client = boto3.client("polly", region_name="us-east-1")
    try:
        client.get_lexicon(
            Name='lexicondemo1'
        )
        client.get_lexicon(
            Name='lexicondemo2'
        )
    except botocore.errorfactory.ClientError:
        pass
    else:
        print "You do have lexicondemo1 or lexicondemo2 in your polly, we won't create/overwrite it. quit..."
        sys.exit(0)

    with open('./lexicon/lexicon1.pls', 'r') as content_file:
        lexicon_demo_1 = content_file.read()
    client.put_lexicon(
        Name='lexicondemo1',
        Content=lexicon_demo_1
    )
    print "lexicondemo1 created successfully"
    with open('./lexicon/lexicon2.pls', 'r') as content_file:
        lexicon_demo_2 = content_file.read()
    client.put_lexicon(
        Name='lexicondemo2',
        Content=lexicon_demo_2
    )
    print "lexicondemo2 created successfully"

def get_lexicon():
    client = boto3.client("polly", region_name="us-east-1")

    for i in ["1", "2"]:
        response = client.get_lexicon(
            Name='lexicondemo' + i
        )

        print "\nlexicondemo%s lexicon content: " %(i)
        print response['Lexicon']['Content']

def delete_lexicon():
    client = boto3.client("polly", region_name="us-east-1")
    client.delete_lexicon(Name='lexicondemo1')
    client.delete_lexicon(Name='lexicondemo2')
    print "\nthe demo lexicons have been deleted"

if __name__=="__main__":
    create_lexicon()
    list_lexicon()
    #sorry I need to put a sleep here as the consistency model
    time.sleep(5)
    get_lexicon()
    #delete_lexicon()