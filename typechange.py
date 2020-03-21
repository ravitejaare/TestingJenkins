import boto3
ec2 = boto3.client('ec2')
instances = ec2.describe_instances()
for reservations in instances['Reservations']:
  for instance in reservations['Instances']:
     if(instance['State']['Name'] == 'running'):
       #ec2.stop_instances(InstanceIds=[instance['InstanceId']])
        ec2.stop_instances(InstanceIds=['$InstanceId'])
        ec2.modify_instance_attribute(InstanceId='$InstanceId', Attribute='instanceType', Value='$type')
        ec2.start_instances(InstanceIds=['$InstanceId'])
     else:
       ec2.modify_instance_attribute(InstanceId='$InstanceId', Attribute='instanceType', Value='$type')
       ec2.start_instances(InstanceIds=['$InstanceId'])
