import boto3
from botocore.exceptions import ClientError

__aws_access_key_id__ = '<AWS_ACCESS_KEY_ID>'
__aws_secret_access_key__ = '<AWS_SECRET_ACCESS_KEY>'

def create_s3_bucket(bucket_name):
  print("Creating a bucket... " + bucket_name)
  s3 = boto3.client(
    's3', # 사용할 서비스 이름, ec2이면 'ec2', s3이면 's3', dynamodb이면 'dynamodb'
    aws_access_key_id=__aws_access_key_id__, # 액세스 키
    aws_secret_access_key=__aws_secret_access_key__) # 비밀 엑세스 키

try:
  response = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
      'LocationConstraint': 'us-east-2' # us-east-1을 제외한 지역은 LocationConstraint 명시해야함.
    }
  )
  return response
except ClientError as e:
  if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
    print("Bucket already exists. skipping..")
  else: 
    print("Unknown error, exit..")

def main():
  response = create_s3_bucket("myfirstbucket-fsoftwareengineer")
  print("Bucket : " + str(response))


main()
