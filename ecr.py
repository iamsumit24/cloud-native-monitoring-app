# ecr.py

import boto3

ecr_client = boto3.client('ecr')

repo_name = "cloud-monitoring-app-12"

response = ecr_client.create_repository(
    repositoryName=repo_name
)

repo_uri = response['repository']['repositoryUri']
print(repo_uri)
