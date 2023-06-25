#!/usr/bin/env python

import click
import boto3



def labeler(bucket, name):
    # Create a client object for Amazon Rekognition
    rekognition = boto3.client('rekognition')
    
    # Create a dictionary containing the S3 bucket and object key
    s3_object = {'Bucket': bucket, 'Name': name}
    
    # Call the detect_labels() method of the Rekognition client
    response = rekognition.detect_labels(Image={'S3Object': s3_object})
    
    # Print the labels detected in the image
    for label in response['Labels']:
        click.echo(
            click.style(f"{label['Name']}: {label['Confidence']}", fg="white", bg="red")    
        )
        




@click.command()
@click.option(
    '-b',
    '--bucket',
    type=str,
    required=True,
    prompt="S3 Bucket Name",
    help="name of a S3 bucket"
)
@click.option(
    '-n',
    '--name',
    type=str,
    required=True,
    prompt="Image Name",
    help="Object Name - image - jungle.png"
)
def main(**kwargs):
    print(f"Bucket name: {kwargs.get('bucket')}\nObject name: {kwargs.get('name')}")
    labeler(kwargs.get('bucket'), kwargs.get('name'))
    



if __name__ == '__main__':
    main()