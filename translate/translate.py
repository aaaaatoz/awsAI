#!/bin/python

#now we only support one API
import boto3

translate = boto3.client("translate", region_name = "us-east-1")

sample_source_text = \
"""Amazon Translate is a neural machine translation service that delivers fast, high-quality, and affordable language translation. Neural machine translation is a form of language translation automation that uses machine learning and deep learning models to deliver more accurate and more natural sounding translation than traditional statistical and rule-based translation algorithms. and to localize websites and applications for international users. """

sample_language_code = "en"

supported_language = {"ar":"Arabic","zh": "Chinese (Simplified)", "fr":"French", "de":"German", "pt":"Portuguese", \
                      "es":"Spanish", "en":"English"}

print "The source Text is: " + sample_source_text
print "The source Text is in " + supported_language[sample_language_code] +"\n"

if sample_language_code not in supported_language:
    print "At the moment AWS Translate service only support language in "
    for language in supported_language:
        print supported_language[language],

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
#
#
# print """
# Now AWS Translate service only support translate between English (en) and one of the following languages, \
# or between one of the following languages and English
# """



