import boto3
ec2 = boto3.client('ec2')
instances = ec2.describe_instances()
echo '$InstanceID'
for reservations in instances['Reservations']:
  for instance in reservations['Instances']:
     if(instance['State']['Name'] == 'running'):
       #ec2.stop_instances(InstanceIds=[instance['InstanceId']])
        print("this is instanceid", '$InstanceID')
        ec2.stop_instances(InstanceIds=['$InstanceID'])
        ec2.modify_instance_attribute(InstanceId='$InstanceID', Attribute='instanceType', Value='$type')
        ec2.start_instances(InstanceIds=['$InstanceID'])
     else:
       ec2.modify_instance_attribute(InstanceId='$InstanceID', Attribute='instanceType', Value='$type')
       ec2.start_instances(InstanceIds=['$InstanceID'])
