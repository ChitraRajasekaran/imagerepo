import boto3, botocore 
from botocore.config import Config
import os
from io import BytesIO

session = boto3.Session(region_name='us-east-2',
                        aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
                        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
                    )

s3 = session.client('s3')
r = s3.generate_presigned_url('get_object',
                                Params={'Bucket': 'qtimagerepo',
                                        'Key': 'GM 1.JPG'})
print(r)