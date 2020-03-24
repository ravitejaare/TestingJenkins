import boto3
import sys
ec2 = boto3.client('ec2',region_name='us-east-1')
instances = ec2.describe_instances()
print("this is instanceid", sys.argv[1])
print("the instance type",sys.argv[2])
id= sys.argv[1]
type= sys.argv[2]

#print("this is id: os.getenv("InstanceID")")
for reservations in instances['Reservations']:
  for instance in reservations['Instances']:
     if((instance['State']['Name'] == 'running') and (instance['InstanceId'] ==sys.argv[1])):
       #ec2.stop_instances(InstanceIds=[instance['InstanceId']])
        print("this is instanceid", sys.argv[1])
        #ec2.stop_instances(InstanceIds=[id])
        #waiter=ec2.get_waiter('instance_stopped')
        #waiter.wait(InstanceIds=[id])
        ec2.modify_instance_attribute(InstanceId=id, Attribute='instanceType', Value=type)
        ec2.start_instances(InstanceIds=[id])
     else:
       ec2.modify_instance_attribute(InstanceId=id, Attribute='instanceType', Value=type)
       #ec2.start_instances(InstanceIds=[id])
      
 
ec2.start_instances(InstanceIds=[id])


