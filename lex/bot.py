#!env python

"""
demo to show Lex bot related APIs
"""

import boto3
import intent
client = boto3.client('lex-models', region_name="us-east-1")

clarificationPrompt={
    'messages': [
        {
            'contentType': 'PlainText',
            'content': "I don't understand, please try again"
        },
    ],
    'maxAttempts': 3
}

abortStatement={
    'messages': [
        {
            'contentType': 'PlainText',
            'content': 'Sorry, I gave up'
        },
    ]
}

def create_bot(bot_name):
    """
    if the bot name exists, then return without action, otherwise create a blank bot
    :param bot_name: the name to create a bot
    :return: None
    """
    try:
        client.get_bot(
            name=bot_name,
            versionOrAlias='$LATEST'
        )
        print "There is a %s bot in your account, please consider delete it or using another name" %(bot_name)
        return
    except:
        pass

    client.put_bot(
        name=bot_name,
        description='The demo bot',
        idleSessionTTLInSeconds=123,
        voiceId='Joanna',
        processBehavior='SAVE',
        locale='en-US',
        clarificationPrompt=clarificationPrompt,
        abortStatement=abortStatement,
        childDirected=False
    )
    print "bot %s created successfully" %(bot_name)
    return


def add_intent_to_bot(bot_name, intent_name):
    """
    add the intent to the bot
    :param bot_name: add the intent to this bot
    :param intent_name: the intent to add
    :return: procedure, None to return
    """
    intent.create_intent(intent_name)
    latest_version_checksum = get_bot_configuration(bot_name)[u'checksum']
    client.put_bot(
        name=bot_name,
        intents=[
            {
                'intentName': intent_name,
                'intentVersion': "$LATEST"
            },
        ],
        clarificationPrompt=clarificationPrompt,
        abortStatement=abortStatement,
        locale='en-US',
        childDirected=False,
        checksum=latest_version_checksum,
        processBehavior='BUILD' # when the processBehavior set to build, it will build it.
    )
    print "%s added to %s successfully" % (intent_name, bot_name)
    return

def delete_bot(bot_name):
    """
    delete the specified bot from your account.
    :param bot_name: the bot name to delete
    :return:
    """
    try:
        client.get_bot(
            name=bot_name,
            versionOrAlias='$LATEST'
        )
        answer=raw_input("Do you want to delete %s from your account(Y/y for YES, other NO):" %(bot_name))
        if answer in ['Y', 'y']:
            client.delete_bot(
                name=bot_name
            )
            print "You chose to delete the bot %s, deleted..." %(bot_name)
        else:
            print "You chose not to delete the bot %s, exiting..."  %(bot_name)
    except:
        print "There is no bot called %s, exiting..." %(bot_name)
    return


def get_bot_configuration(bot_name, versionOrAlias = "$LATEST"):
    """
    demo function to get the bot's latest configuration
    :param bot_name: the name of the bot.
    :param versionOrAlias: default is $LATEST and you can put version or alias here
    :return: the API response
    """
    response=client.get_bot(
        name=bot_name,
        versionOrAlias=versionOrAlias
    )
    return response


def get_all_botos():
    """
    print all bot in the account and assume they are less than 50
    :return: None but will print
    """
    bots = client.get_bots(
        maxResults=50
    )['bots']
    print "There are %d bots under your account/region." %len(bots)
    for bot in bots:
        format_print_jobs(bot)

def format_print_jobs(bot):
    """
    a help function to print the bot information in format
    :param bot: the bot information as a dictionary
    :return: None but will print the output
    """
    print "\nBot Name: %s" %(bot['name'])
    for k,v in bot.iteritems():
        if k <> 'name':
            print "\t" + str(k) + ": " + str(v)

if __name__ == "__main__":
    create_bot("rafademobot")
    # time.sleep(10)
    #get_bot_configuration("rafademobot")
    #get_all_botos()
    add_intent_to_bot("rafademobot", "rafademointent_book_hotel")
    # delete_bot("rafademobot")
    pass