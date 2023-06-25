import boto3
from urllib.parse import unquote_plus


def labeler(bucket, name):
    """Takes an image name from a given bucket and returns labels from it"""
    
    rekognition = boto3.client('rekognition')
    s3_object = {'Bucket': bucket, 'Name': name}
    response = rekognition.detect_labels(Image={'S3Object': s3_object})
    
    for label in response['Labels']:
        print(f"I found {label['Name']}, with confident of {label['Confidence']}")
        
    
def lambda_handler(event, context):
    """This is a lambda handler for the computer vision"""
    
    print(f"Triggred event: {event}")
    
    for record in event["Records"]:
        bucket = record["s3"]["bucket"]["name"]
        print(f"S3 Bucket: {bucket}")
        name = unquote_plus(record["s3"]["object"]["key"])
        print(f"Name of Object: {name}")
        
    
    labeler(bucket, name)