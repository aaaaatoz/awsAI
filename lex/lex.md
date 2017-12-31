
# Key concept:
 - **Bot**: performs automated tasks, it can contains multiple Intents.
 - **Intent**: an action that the user wants to perform. it can belong to multiple bots
 - **Slot**: the parameter for a intent
 - **Slot Type**: the customer or build-in allowed values for slot  
 - **Utterances**: How a user might convey the intent
 - **Association**: The integration between lex bot with other 3rd party applications
 
# Bot Configuration:
 - **name**: name of a bot
 - **locale**: the locale information of the bot: default en-US
 - **abortStatement**: Once it can't understand for more than max times, the prommpt inforamtion to customer
 - **intents**: an intents(intent name/version pair)list
 - **voiceId**: the voice id of the audio output, referring polly
 - **childDirected**: boolean value for child directed
 - **idleinTTLseconds**: idle value, if not active in given seconds, session timed out
 - **clarificationPrompt**, the prompt message to client when lex can't understand it and the attempt count.
 - **description**: description information.
 
# Bot Meta data:
 - createdDate
 - lastUpdatedDate
 - version
 - checksum
 - status
 
# Intent Configuration:
 - **name**: name of a bot
 - **locale**: the locale information of the bot: default en-US
 - **abortStatement**: Once it can't understand for more than max times, the prommpt inforamtion to customer
 - **intents**: an intents(intent name/version pair)list
 - **voiceId**: the voice id of the audio output, referring polly
 - **childDirected**: boolean value for child directed
 - **idleinTTLseconds**: idle value, if not active in given seconds, session timed out
 - **clarificationPrompt**, the prompt message to client when lex can't understand it and the attempt count.
 - **description**: description information.
 
# Intent Meta data:
 - createdDate
 - lastUpdatedDate
 - version
 - checksum
 - status

# API full list by category

## bot controls 
 - **PutBot**:
 - **GetBot**:
 - **GetBots**:
 - **DeleteBot**:
 - **CreateBotVersion**
 - **PutBotAlias**
 - **GetBotAlias**
 - **GetBotAliases**
 - **GetBotVersions**
 - **DeleteBotAlias**
 - **DeleteBotVersion**
 - **GetUtterancesView**

## intent controls
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
 
## slot type
 - **CreateSlotTypeVersion**
 - **DeleteSlotType**
 - **DeleteSlotTypeVersion**
 - **GetBuiltinSlotTypes**
 - **GetSlotType**
 - **GetSlotTypes**
 - **GetSlotTypeVersions**
 - **PutSlotType**

## Channel association
 - **DeleteBotChannelAssociation**:
 - **GetBotChannelAssociation**:
 - **GetBotChannelAssociations**:
 - **Note**: creating channel association is only allowed from GUI

## Alexa skills
 - **GetExport**
 
# Demo program
