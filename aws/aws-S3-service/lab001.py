from dotenv import load_dotenv
import os
import boto3

load_dotenv()

def upload_file(client):
    filename = 'test.txt'
    bucket_name = os.environ('BUCKET_NAME')
    key = "media/test.txt"
    client.upload_file(filename, bucket_name, key)
    print(f"File '{filename}' uploaded")

def download_file(client):
    filename = 'test.txt'
    bucket_name = os.environ('BUCKET_NAME')
    key = "media/test.txt"
    with open (filename, 'wb') as data:
        client.download_fileobj(bucket_name, key, data)
    print(f"File '{filename}' downloaded")

if __name__ == "__main__":

    client = boto3.client('s3',
        aws_access_key_id=os.environ('ACCESS_KEY'),
        aws_secret_access_key=os.environ('SECRET_KEY'),
    )

    upload_file(client)
    #download_file(client)
