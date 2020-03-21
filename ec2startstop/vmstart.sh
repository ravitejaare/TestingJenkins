#!/bin/bash
if [ "$State" = "start" ]
then 
aws ec2 --region us-east-1 start-instances --instance-ids $InstanceID
echo Instance $InstanceID Started
elif [ "$State" = "stop" ]
then
aws ec2  --region us-east-1 stop-instances --instance-ids $InstanceID
echo Instance $InstanceID Stopped
 fi
