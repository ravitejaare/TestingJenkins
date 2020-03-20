#!/bin/bash
if [ "$State" = "start" ]
then 
aws ec2 --region ap-south-1 start-instances --instance-ids $InstanceID
echo Instance $InstanceID Started
elif [ "$State" = "stop" ]
then
aws ec2  --region ap-south-1 stop-instances --instance-ids $InstanceID
echo Instance $InstanceID Stopped
 fi
