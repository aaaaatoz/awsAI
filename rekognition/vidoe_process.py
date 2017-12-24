#!/bin/python

import boto3

class video_processing:
    def __init__(self,
                 snstopic = "arn:aws:sns:us-east-1:620428855768:rekognition",
                 role = "arn:aws:iam::620428855768:role/rekognitionnotification",
                 region="us-east-1"):
        self.client = boto3.client('rekognition', region_name=region)
        self.NotificationChannel={
        'SNSTopicArn': snstopic,
        'RoleArn': role
    }

    def start_celebrity_recognition(self, bucket, object):
        bucket = "rafacomprehend"
        object = "lots-of-people.mp4"
        jobResponse = self.client.start_celebrity_recognition(
            Video={
                'S3Object': {
                    'Bucket': bucket,
                    'Name': object
                }
            },
            ClientRequestToken='celebrity',
            NotificationChannel=self.NotificationChannel,
            JobTag='string'
        )
        print jobResponse['JobId']

    def get_celebrity_recognition(self, jobId):
        jobResponse = self.client.get_celebrity_recognition(jobId)

    def face_search(self, bucket, object, collectionId):
        face_search_response = self.client.start_face_search(
        Video={
                'S3Object': {
                    'Bucket': bucket,
                    'Name': object
                }
            },
            ClientRequestToken ='search_face',
            CollectionId = collectionId,
            NotificationChannel=self.NotificationChannel,
            JobTag='search_face'
        )
        print face_search_response['JobId']


if __name__== "__main__":
    video_processing_object = video_processing()
    video_processing_object.face_search("rafacomprehend", "lots-of-people.mp4", "my_celebrities_collection")