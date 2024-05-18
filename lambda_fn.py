import boto3
import datetime

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    ebs = boto3.client('ec2')

    # Get all EBS snapshots
    snapshots = ebs.describe_snapshots(OwnerIds=['self'])['Snapshots']

    # Get all active EC2 instances
    instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running', 'stopped']}])['Reservations']

    # Dictionary to hold instance IDs and their corresponding volumes
    instance_volumes = {}

    for reservation in instances:
        for instance in reservation['Instances']:
            for volume in instance['BlockDeviceMappings']:
                instance_volumes[volume['VolumeId']] = True

    # Find and delete stale snapshots
    for snapshot in snapshots:
        if snapshot['State'] == 'completed' and snapshot['Progress'] == '100%' and snapshot['Description'].startswith('EBS Snap'):
            if snapshot['VolumeId'] not in instance_volumes:
                ebs.delete_snapshot(SnapshotId=snapshot['SnapshotId'])
                print(f"Deleted snapshot {snapshot['SnapshotId']}")

    return {
        'statusCode': 200,
        'body': 'Snapshot cleanup completed.'
    }
