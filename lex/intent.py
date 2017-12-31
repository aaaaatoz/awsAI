#!env python

"""
demo to show Lex intent related APIs
 - **PutIntent**
 - **GetIntent**
 - **GetIntents**
 - **DeleteIntent**
 - **DeleteIntentVersion**
 - **CreateIntentVersion**
 - **GetIntentVersions**
 - **GetBuiltinIntent**
 - **GetBuiltinIntents**
 - **DeleteUtterances**
"""

import boto3
client = boto3.client('lex-models', region_name="us-east-1")

def create_intent(intent_name):
    """
    if the intent name exists, then return without action, otherwise create a blank intent
    :param intent_name: the name to create the intent
    :return: None
    """
    try:
        response=client.get_intent(
            name=intent_name,
            version="$LATEST"
        )
        print "There is a %s intent in your account, please consider delete it or using another name" %(intent_name)
        return
    except:
        pass

    response=client.put_intent(
        name=intent_name,
        description='the demo intent',
        sampleUtterances=[
            'Can I book a hotel',
        ],
        confirmationPrompt={
            'messages': [
                {
                    'contentType': 'PlainText',
                    'content': 'Your hotel booking is ready, do you want to place an order?'
                },
            ],
            'maxAttempts': 2,
        },
        rejectionStatement={
            'messages': [
                {
                    'contentType': 'PlainText' ,
                    'content': 'Ok. I will discard the hotel booking information'
                },
            ],
        },
        conclusionStatement={
            'messages': [
                {
                    'contentType': 'PlainText',
                    'content': 'Your hotel booking has been confirmed'
                },
            ],
        },
        fulfillmentActivity={
            'type': 'ReturnIntent'
        }
    )
    print "Intent %s created successfully" %(intent_name)
    return


def get_my_intents():
    response = client.get_intents()
    return response[u'intents']

def builtin_intents():
    client.get_builtin_intents(
        locale='en-US',
        maxResults=50
    )


def delete_intent(intent_name):
    """
    delete the specified intentfrom your account.
    :param intent_name: the intentname to delete
    :return:
    """
    try:
        client.get_intent(
            name=intent_name,
            versionOrAlias='$LATEST'
        )
        answer=raw_input("Do you want to delete %s from your account(Y/y for YES, other NO):" %(intent_name))
        if answer in ['Y', 'y']:
            client.delete_intent(
                name=intent_name
            )
            print "You chose to delete the intent %s, deleted..." %(intent_name)
        else:
            print "You chose not to delete the inten t%s, exiting..."  %(intent_name)
    except:
        print "There is no intent called %s, exiting..." %(intent_name)
    return


def get_intent_configuration(intent_name, version ="$LATEST"):
    """
    demo function to get the intent's latest configuration
    :param intent_name: the name of the intent.
    :param version: default is $LATEST and you can put version or alias here
    :return: print the configuration, no return value
    """
    response=client.get_intent(
        name=intent_name,
        version=version
    )
    return response

def format_print_jobs(intent):
    """
    a help function to print the intentinformation in format
    :param intent: the intentinformation as a dictionary
    :return: None but will print the output
    """
    print "\nintentName: %s" %(intent['name'])
    for k,v in intent.iteritems():
        if k <> 'name':
            print "\t" + str(k) + ": " + str(v)

if __name__ == "__main__":
    #create_intent("rafademointent_book_hotel")
    # time.sleep(10)
    get_intent_configuration("my_car_type")
    # delete_intent("rafademointent_book_hotel")
    pass