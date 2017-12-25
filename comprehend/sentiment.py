#!env python
"""
the demo APIs to show how to use Comprehend service to detect the entities
"""
import boto3

client = boto3.client('comprehend', region_name="us-east-1")

sampleText = []
file1 = open("./text/positive_en.txt", "r")
file2 = open("./text/negative_en.txt", "r")
file3 = open("./text/neutral_en.txt", "r")
file4 = open("./text/mixed_en.txt", "r")

sampleText.append(file1.read())
sampleText.append(file2.read())
sampleText.append(file3.read())
sampleText.append(file4.read())

positive_es = open("./text/positive_es.txt", "r").read()


def detect_sentiment():
    print "Sample text is:\n%s" %(positive_es)
    sentiment = client.detect_sentiment(
        Text=positive_es,
        LanguageCode = "es"
    )
    sentiment_score = sentiment['SentimentScore']
    print "the four sentiments and scores are:\n%20s\t%20s\t%20s\t%20s"  %("Positive", "Negative", "Neutral", "Mixed")
    print "%1.18f\t%1.18f\t%1.18f\t%1.18f" %(sentiment_score['Positive'], sentiment_score['Negative'], sentiment_score['Neutral'], sentiment_score['Mixed'])
    print "Conclusion: the sample text is %s with a score: %1.18f\n\n" %(sentiment['Sentiment'], sentiment_score[convert_sentiment(sentiment['Sentiment'])])


def batch_detect_sentiment():
    sentiments = client.batch_detect_sentiment(
        TextList=sampleText,
        LanguageCode="en"
    )['ResultList']
    for result in sentiments:
        print "Sample text is:\n%s" %(sampleText[result['Index']])
        print "the four sentiments and scores are:\n%20s\t%20s\t%20s\t%20s" % ("Positive", "Negative", "Neutral", "Mixed")
        print "%1.18f\t%1.18f\t%1.18f\t%1.18f" % (result['SentimentScore']['Positive'], result['SentimentScore']['Negative'], result['SentimentScore']['Neutral'], result['SentimentScore']['Mixed'])
        print "Conclusion: the sample text is %s with a score: %1.18f\n\n" % (
            result['Sentiment'], result['SentimentScore'][convert_sentiment(result['Sentiment'])])


def convert_sentiment(sentiment):
    """
    a help function. For some reasons, the returned Sentiment is all uppercase but in the score they are lowercase with first letter capitalised.
    this is the helper function to conver it
    :param sentiment:
    :return: the requirement format with first letter uppercase and left are lower case
    """
    return sentiment[0] + sentiment[1:].lower()


if __name__ == "__main__":
    # detect_sentiment()
    # batch_detect_sentiment()
    pass