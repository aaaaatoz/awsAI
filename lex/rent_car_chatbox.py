#!env python

"""
demo to show how to build up a working bot from scratch
 to rent a car: you need to provide:
 -) car type
 -) car brand
 -) picking up time
 -) return time
 -) optional: if you have a lambda to calculate the all cost, then return cost, otherwise returns all your values

"""
import boto3
import slot_type
import intent
import sys


client = boto3.client('lex-models', region_name="us-east-1")

def build_slot_type_car_type():
    client.put_slot_type(
        name='my_car_type',
        description='car type by Expand Values',
        enumerationValues=[
            {u'value': u'MPV'}, 
            {u'value': u'Convertible'}, 
            {u'value': u'SUV'}, 
            {u'value': u'Coupe'}, 
            {u'value': u'Hatchback'}, 
            {u'value': u'Crossover'}, 
            {u'value': u'Sedan'}],
        valueSelectionStrategy='TOP_RESOLUTION'
    )

def build_slot_type_car_brand():
    client.put_slot_type(
        name='my_car_brand',
        description='Car brand',
        enumerationValues=[{u'value': u'Benz'},
                           {u'value': u'Holden'},
                           {u'value': u'Toyota'},
                           {u'value': u'Audi'},
                           {u'value': u'Ford'},
                           {u'value': u'BMW'},
                           {u'value': u'Honda'}],
        valueSelectionStrategy='ORIGINAL_VALUE'
    )

def slot_list():
    slots = [
        {
            'name': 'CarType',
            'description': 'car type',
            'slotConstraint': 'Required' ,
            'slotType': 'my_car_type',
            'slotTypeVersion': '$LATEST',
            'valueElicitationPrompt': {
                'messages': [
                    {
                        'contentType': 'PlainText' ,
                        'content': 'What types of car do you want to rent?'
                    },
                ],
                'maxAttempts': 3
            },
            'priority': 10
        },
        {
            'name': 'CarBrand',
            'description': 'car brand',
            'slotConstraint': 'Required',
            'slotType': 'my_car_brand',
            'slotTypeVersion': '$LATEST',
            'valueElicitationPrompt': {
                'messages': [
                    {
                        'contentType': 'PlainText',
                        'content': 'What car brand do you want to rent?'
                    },
                ],
                'maxAttempts': 3
            },
            'priority': 20
        },
        {
            'name': 'pickupdate',
            'description': 'which day to pick up',
            'slotConstraint': 'Required',
            'slotType': 'AMAZON.DATE',
            'slotTypeVersion': 'Build-in',
            'valueElicitationPrompt': {
                'messages': [
                    {
                        'contentType': 'PlainText',
                        'content': 'When do you want to pick up your car?'
                    },
                ],
                'maxAttempts': 3
            },
            'priority': 20
        }
    ]

def build_intent():
    pass

def build_bot():
    pass

if __name__ =="__main__":
    all_my_slot_type = slot_type.get_all_my_slot_types()
    my_slot_types = [slot['name'] for slot in all_my_slot_type]
    if 'my_car_brand' in my_slot_types or 'my_car_type' in my_slot_types:
        print "the slot type [my_car_brand] or [my_car_type] is already in the lex service, you need to clean it up..."
        sys.exit(-1)

    all_my_intent = intent.get_my_intents()
    my_intents = [intent['name'] for intent in all_my_intent]

    if 'rent_car' in my_intents:
        print "the intent [rent_car] is already in the lex service, you need to clean it up..."
        sys.exit(-1)

