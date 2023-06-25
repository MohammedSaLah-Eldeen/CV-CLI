#!/usr/bin/env python

import click
import boto3



def labeler(bucket, name):
    """Takes an image name from a given bucket and returns labels from it"""
    
    rekognition = boto3.client('rekognition')
    s3_object = {'Bucket': bucket, 'Name': name}
    response = rekognition.detect_labels(Image={'S3Object': s3_object})
    
    for label in response['Labels']:
        click.echo(
            click.style(f"{label['Name']}: {label['Confidence']}", fg="red")    
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
    """A tool for extracting labels from images"""
    
    print(f"Bucket name: {kwargs.get('bucket')}\nObject name: {kwargs.get('name')}")
    labeler(kwargs.get('bucket'), kwargs.get('name'))
    



if __name__ == '__main__':
    main()