import boto3
ec2 = boto3.client('ec2')
instances = ec2.describe_instances()
print("this is instanceid", '$InstanceID')

