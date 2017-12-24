#!/bin/python

import boto3
import time

if __name__== "__main__":
    client = boto3.client('rekognition', region_name = "us-east-1")

    responseProcessing = client.start_face_detection(
        Video={
            'S3Object': {
                'Bucket': 'rafacomprehend',
                'Name': 'lots-of-people.mp4'
            }
        },
        ClientRequestToken='celebrity',
        NotificationChannel={
            'SNSTopicArn': 'arn:aws:sns:us-east-1:620428855768:SNS2SQS',
            'RoleArn': 'arn:aws:iam::620428855768:role/rekognitionnotification'
        },
        JobTag='string'
    )
    print responseProcessing["JobId"]

## once it is finished.
    responseResult = client.get_face_detection(JobId=responseProcessing["JobId"])