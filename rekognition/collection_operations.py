import boto3

class rekognition_collection:
    def __init__(self, collection_name, region="us-east-1"):
        self.region = region
        self.collection_name = collection_name
        self.client = boto3.client("rekognition", region_name = region)
        try:
            self.client.delete_collection(
                CollectionId=collection_name,
            )
        except:
            pass

        self.client.create_collection(
                CollectionId=collection_name,
        )

    def index_faces_from_s3(self, bucket, prefix=""):

        s3client = boto3.client("s3", self.region)
        objects = s3client.list_objects(
            Bucket=bucket,
            Prefix=prefix
        )
        faces_objects = [ face['Key'] for face in objects["Contents"] if face['Key'] != prefix]

        for face in faces_objects:
            self.client.index_faces(
                CollectionId=self.collection_name,
                Image={
                    'S3Object': {
                        'Bucket': bucket,
                        'Name': face
                    }
                },
                ExternalImageId=face[len(prefix):face.index(".")],
            )

if __name__=="__main__":
    collection = rekognition_collection("my_celebrities_collection")
    collection.index_faces_from_s3("rafarekognition", "faces/")

