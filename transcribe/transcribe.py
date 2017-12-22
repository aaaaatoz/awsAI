#!/bin/python

#now I am still in the progress of preview application so the code hasn't been tested yet
#Also it seems the service not supported in boto3(or any SDK) yet

import boto3

transcribe = boto3.client("transcribe", region_name = "us-east-1")

transcribe.list_transcription_jobs()