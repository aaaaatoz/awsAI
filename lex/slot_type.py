#!env python

"""
demo to show Lex bot related APIs
"""

# - ** CreateSlotTypeVersion **
# - ** DeleteSlotTypeVersion **
# - ** GetSlotTypeVersions **

import boto3
import time

client = boto3.client('lex-models', region_name="us-east-1")


def create_slot_type_liquor_type():
    client.put_slot_type(
        name='LiquorType',
        description='LiquorType by Expand Values',
        enumerationValues=[
            {
                'value': 'Cooktail'
            },
            {
                'value': 'Cider'
            },
            {
                'value': 'Wine'
            },
            {
                'value': 'Beer'
            },
        ],
        valueSelectionStrategy='ORIGINAL_VALUE'
    )


def create_slot_type_liquor_size():
    client.put_slot_type(
        name='LiquorSize',
        description='LiquorType by Expand Values',
        enumerationValues=[
            {
                'value': 'jar',
                'synonyms': [
                    'jug', "beaker"
                ]
            },
            {
                'value': 'bottle',
                'synonyms': [
                    'flask'
                ]
            },
            {
                'value': 'cup'
            },
        ],
        valueSelectionStrategy='TOP_RESOLUTION'
    )


def create_slot_type_dummy():
    client.put_slot_type(
        name='dummy',
        enumerationValues=[
            {
                'value': 'foo'
            }
        ],
        valueSelectionStrategy='ORIGINAL_VALUE'
    )
    print "slot type dummy created successfully"


def slot_type_version_management():

    # check if the dummy slot type is in the account
    all_my_slot_type=get_all_my_slot_types()
    my_slot_types = [ slot['name'] for slot in all_my_slot_type]
    if 'dummy' in my_slot_types:
        print "In the demo, we use dummy as example, you need to delete dummy slot type manually in case it is referenced by other entity"
        return

    #create a dummy slot_type and create the version - version - 1
    create_slot_type_dummy()
    time.sleep(5)
    dummy_slot_type=get_latest_slot_type("dummy")
    client.create_slot_type_version(
        name='dummy'
    )
    print "version 1 created"

    #update the slot_type and create a new version - version -2
    time.sleep(5)
    client.put_slot_type(
        name='dummy',
        enumerationValues=[
            {
                'value': 'foo'
            },
            {
                'value': 'bar'
            }
        ],
        checksum = dummy_slot_type['checksum'],
        valueSelectionStrategy='ORIGINAL_VALUE'
    )
    print "dummy updated"
    time.sleep(5)
    client.create_slot_type_version(
        name='dummy'
    )
    print "version 2 created"

    response = client.get_slot_type_versions(
        name='dummy'
    )
    versions = [ slottype['version'] for slottype in response['slotTypes']]
    print "Now dummy has %d versions: They are %s" %(len(versions), str(versions))

    # delete one version
    time.sleep(5)
    print "slot type dummy version 1 is deleted"
    client.delete_slot_type_version(
        name="dummy",
        version='1'
    )
    time.sleep(5)
    response = client.get_slot_type_versions(
        name='dummy'
    )
    versions = [slottype['version'] for slottype in response['slotTypes']]
    print "Now dummy has %d versions: They are %s" % (len(versions), str(versions))

    # clean up / delete the slot type
    print "cleaning up..."
    delete_slot_type_dummy()


def delete_slot_type_dummy():
    """
    delete the dummy slot_type in your account. the dummy slot type shouldn't be used in any intent
    :return: None
    """
    try:
        client.get_slot_type(
            name="dummy",
            version='$LATEST'
        )
        answer = raw_input("Do you want to delete slot type dummy from your account(Y/y for YES, other NO):")
        if answer in ['Y', 'y']:
            client.delete_slot_type(
                name="dummy"
            )
            print "You chose to delete the slot type %s, deleted..." %("dummy")
        else:
            print "You chose not to delete the slot type %s, exiting..." %("dummy")
    except:
        print "There is no slot type called %s, exiting..." %("dummy")
    return


def get_all_my_slot_types():
    """
    get all my custom slot types, you may use nameContains to get slot types, parameter as substring.
    :return:
    """
    #response=client.get_slot_types(nameContains='dummy')
    response=client.get_slot_types()
    # unhash to print the raw response
    # print response
    return response[u'slotTypes']


def get_latest_slot_type(slot_type_name):
    response = client.get_slot_type(
        name=slot_type_name,
        version='$LATEST'
    )
    # unhash it to see the raw response
    print response
    return response


def get_build_in_slot_type():
    response = client.get_builtin_slot_types(
        locale='en-US',
        signatureContains='AMAZON.B',
        maxResults=50 # 50 is the max number
    )
    # unhash to print the raw response
    # print response
    return response['slotTypes']


def format_print(slot_type_information):
    """
    a help function to print the slot type information in format
    :param slot_type_information: the bot information as a dictionary
    :return: None but will print the output
    """
    print "\nSlot_Type Name: %s" %(slot_type_information['name'])
    for k,v in slot_type_information.iteritems():
        if k <> 'name' and k <> 'ResponseMetadata':
            print "\t" + str(k) + ": " + str(v)

if __name__ == "__main__":
    # create_slot_type_liquor_type()
    # time.sleep(5)
    # create_slot_type_liquor_size()
    # time.sleep(10)
    # get_intent_configuration("rafademointent_book_hotel")
    # delete_intent("rafademointent_book_hotel")
    # format_print(get_latest_slot_type("LiquorSize"))
    # format_print(get_latest_slot_type("LiquorType"))
    # create_slot_type_dummy()
    # time.sleep(10)
    get_latest_slot_type('Car_brand')
    #for slot_type in get_all_my_slot_types(): format_print(slot_type)
    # delete_slot_type_dummy()
    # get_build_in_slot_type()
    #slot_type_version_management()
    pass