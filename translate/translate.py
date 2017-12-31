#!/bin/python

import boto3
import sys
translate = boto3.client("translate", region_name = "us-east-1")

sample_source_text = \
"""Amazon Translate is a neural machine translation service that delivers fast, high-quality, and affordable text translation. Neural machine translation is a form of text translation automation that uses machine learning and deep learning models to deliver more accurate and more natural sounding translation than traditional statistical and rule-based translation algorithms. and to localize websites and applications for international users. """

sample_language_code = "en"

supported_language = {"ar":"Arabic","zh": "Chinese (Simplified)", "fr":"French", "de":"German", "pt":"Portuguese", \
                      "es":"Spanish", "en":"English"}

print "The source Text is: " + sample_source_text
print "The source Text is in " + supported_language[sample_language_code] +"\n"

if sample_language_code not in supported_language:
    print "At the moment AWS Translate service only support text in "
    for language in supported_language:
        print supported_language[language],
    sys.exit(0)

if sample_language_code == "en":
    for language in supported_language:
        response = translate.translate_text(
            Text=sample_source_text,
            SourceLanguageCode=sample_language_code,
            TargetLanguageCode=language
        )
        print "if translated into " + supported_language[language] + ":"
        print response['TranslatedText'] + "\n"
else:
    response = translate.translate_text(
            Text=sample_source_text,
            SourceLanguageCode=sample_language_code,
            TargetLanguageCode="en"
        )
    print "if translated into " + supported_language["en"] + ":"
    print response['TranslatedText'] + "\n"



