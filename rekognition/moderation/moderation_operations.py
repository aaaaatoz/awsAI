import boto3

# test the following
# detect-moderation-labels: image
# start-content-moderation: start a video content moderation job
# get-content-moderation: get a video content moderation job result

#testing detect-moderation-labels
# Explicit Nudity
#     Nudity
#     Graphic Male Nudity
#     Graphic Female Nudity
#     Sexual Activity
#     Partial Nudity

# Suggestive
#       Female Swimwear Or Underwear
#       Male Swimwear Or Underwear
#       Revealing Clothes

client = boto3.client("rekognition", region_name = "us-east-1")

client.detect_moderation_labels(
    Image={
        'S3Object': {
            'Bucket': 'rafarekognition',
            'Name': 'moderation/naked-man.jpg'
        }
    },
    MinConfidence=85
)

client.detect_moderation_labels(
    Image={
        'S3Object': {
            'Bucket': 'rafarekognition',
            'Name': 'moderation/naked-female.jpg'
        }
    }
)

client.detect_moderation_labels(
    Image={
        'S3Object': {
            'Bucket': 'rafarekognition',
            'Name': 'moderation/sex-activity.jpg'
        }
    }
)