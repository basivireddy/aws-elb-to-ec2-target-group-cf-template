import boto3
region = 'us-east-2'

ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    instance_ids = []
    response = ec2.describe_instances()
    instances_full_details = response['Reservations']
    for instance_detail in instances_full_details:
        group_instances = instance_detail['Instances']

        for instance in group_instances:
            instance_tags = instance['Tags']
            instance_id = instance['InstanceId']
            for tag in instance_tags:
                print(tag, tag.values())
                if "aws:cloudformation:stack-name" in tag.values():
                        instance_ids.append(instance_id)
    
    print(instance_ids)                  
    response = ec2.create_tags(
    Resources= instance_ids,
    Tags=[
        {
            'Key': 'DeplymentType',
            'Value': 'ASG'
        },
    ]
    )

    return response
