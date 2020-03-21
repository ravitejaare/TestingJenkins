import boto3
import sys
ec2 = boto3.client('ec2')
instances = ec2.describe_instances()
print("this is instanceid", 'sys.argv[0]')

#print("this is id: os.getenv("InstanceID")")
for reservations in instances['Reservations']:
  for instance in reservations['Instances']:
     if(instance['State']['Name'] == 'running'):
       #ec2.stop_instances(InstanceIds=[instance['InstanceId']])
        print("this is instanceid", 'sys.argv[0]')
        ec2.stop_instances(InstanceIds=['sys.argv[0]'])
        ec2.modify_instance_attribute(InstanceId='sys.argv[0]', Attribute='instanceType', Value='sys.argv[1]')
        ec2.start_instances(InstanceIds=['sys.argv[0]'])
     else:
       ec2.modify_instance_attribute(InstanceId='sys.argv[0]', Attribute='instanceType', Value='sys.argv[1]')
       ec2.start_instances(InstanceIds=['sys.argv[0]'])

