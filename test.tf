provider "aws" {
access_key = "AKIARSFXJH4XFYOKXUN2"
secret_key = "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"
region = "us-east-1"

}
locals {
  common_tag ={
    "name"="testingme"
     "jenkins"= "true"
     "account"="own"
  }
  common_naming= "learning"
}
resource "aws_instance" "SecondInstance" {
  ami = "ami-0fc61db8544a617ed"
  instance_type = "t2.medium"
  associate_public_ip_address = "true"
  vpc_security_group_ids =[ "sg-016e5d1813783a362" ]
  subnet_id = "subnet-225cb77d"
  key_name = "jenkinstest"

  ebs_block_device {
    device_name="/dev/xvda"
    volume_size="20"
    volume_type="gp2"
   }
  tags = {
    name = "${local.common_naming}"


  }

user_data=<<EOF
  #!/bin/bash -ex
  sudo yum update -y
  sudo yum install httpd -y
  sudo service httpd start

EOF
}
