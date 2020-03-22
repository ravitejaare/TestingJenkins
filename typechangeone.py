import boto3
import sys
ec2 = boto3.client('ec2',region_name='us-east-1')
instances = ec2.describe_instances()
for reservations in instances['Reservations']:
  for instance in reservations['Instances']:
     if((instance['State']['Name'] == 'running') and (instance['InstanceId'] ==$InstanceID)):
       #ec2.stop_instances(InstanceIds=[instance['InstanceId']])
        print("this is instanceid", sys.argv[2])
        ec2.stop_instances(InstanceIds=[$InstanceID])
        waiter=ec2.get_waiter('instance_stopped')
        waiter.wait(InstanceIds=[$InstanceID])
        ec2.modify_instance_attribute(InstanceId=$InstanceID, Attribute='instanceType', Value=$type)
        ec2.start_instances(InstanceIds=[$InstanceID])
     else:
       ec2.modify_instance_attribute(InstanceId=$InstanceID, Attribute='instanceType', Value=$type)
       ec2.start_instances(InstanceIds=[$InstanceID])
