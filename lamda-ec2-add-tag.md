1. Create lambda python
2. add below policy
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
