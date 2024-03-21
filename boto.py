import boto3
from pprint import pprint
"""
s3_instance = boto3.client('s3')
buckets = s3_instance.list_buckets()
pprint(buckets['Buckets'])"""

ec2= boto3.client('ec2','us-east-1')
instances =ec2.describe_instances()
pprint(instances['Reservations'])

"""iam_instance = boto3.client('iam')
users = iam_instance.list_users()

for user in users['Users']:
    print(user['UserName'])
    print(user['CreateDate'])"""
    




