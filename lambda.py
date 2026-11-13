import boto3

ec2 = boto3.client('ec2', region_name='ap-south-1')

def lambda_handler(event, context):

    instance_id = 'put your instance id'

    action = event.get('action')

    if action == 'start':
        response = ec2.start_instances(
            InstanceIds=[instance_id]
        )
        message = f"Starting EC2 instance: {instance_id}"

    elif action == 'stop':
        response = ec2.stop_instances(
            InstanceIds=[instance_id]
        )
        message = f"Stopping EC2 instance: {instance_id}"

    else:
        raise ValueError("Action must be 'start' or 'stop'")

    print(message)
    print(response)

    return {
        'statusCode': 200,
        'body': message
    }