# ecr.py

import boto3

# ✅ Make sure this is your correct AWS region (e.g., 'ap-south-1' for Mumbai)
ecr_client = boto3.client('ecr', region_name='ap-south-1')

repo_name = "cloud-native-monitoring-app"

response = ecr_client.create_repository(
    repositoryName=repo_name
)

repo_uri = response['repository']['repositoryUri']
print(repo_uri)

