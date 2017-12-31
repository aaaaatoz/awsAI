import boto3


if __name__=="__main__":
    client = boto3.client("rekognition", region_name = "us-east-1")
    # unhash the below section if you use S3
    # response = client.detect_text(
    #     Image={
    #         'S3Object': {
    #             'Bucket': 'rafarekognition',
    #             'Name': 'text/vehicle.png'
    #         }
    #     }
    # )

    file = open('./text/vehicle.png', 'rb')
    image = file.read()
    response = client.detect_text(
        Image={
            'Bytes': image
        }
    )

    # unhash the print statement to print the raw response
    # print response

    for text in response['TextDetections']:
        if "ParentId" not in text:
            print text['DetectedText']
