1. Create iam role of type lambada and add below policy
 ```
 {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EC2InstanceConnect",
            "Action": [
                "ec2:DescribeInstances",
                "ec2:CreateTags"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```
2. Create lambda with python 3 add above role 
