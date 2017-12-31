#!env python

"""
demo to show Lex assiciation related APIs
 - **DeleteBotChannelAssociation**:
 - **GetBotChannelAssociation**:
 - **GetBotChannelAssociations**:
 - **Note**: creating channel association is only allowed from GUI
"""
import boto3
client = boto3.client('lex-models', region_name="us-east-1")

def get_bot_associations():
    response = client.get_bot_channel_associations(
        botName='BotIntegration',
        botAlias='integration',
        maxResults=10
    )
    # print response
    return response['botChannelAssociations']

def get_bot_association(association_name):
    response = client.get_bot_channel_association(
        name=association_name,
        botName='BotIntegration',
        botAlias='integration'
    )
    #print response
    # should return an 204 if successful
    return response

def delete_bot_association(assication_name):
    response = client.delete_bot_channel_association(
        name=assication_name,
        botName='slackbot',
        botAlias='slacktest'
    )
    print response

def format_print_assoication(association):
    """
    a help function to print the intentinformation in format
    :param association: the intentinformation as a dictionary
    :return: None but will print the output
    """
    print "\nBotChannelAssociations Name: %s" %(association['name'])
    for k,v in association.iteritems():
        if k <> 'name' and k <> 'ResponseMetadata':
            print "\t" + str(k) + ": " + str(v)


if __name__ == "__main__":
    # associations = get_bot_associations()
    # for association in associations:
    #     format_print_assoication(association)
    # format_print_assoication(get_bot_association("TwilioSMSIntegration"))
    # delete_bot_association("BotSlackIntegration")
    pass