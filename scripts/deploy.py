import os
import boto3


commitId = os.getenv('GITHUB_COMMIT_ID')
print("Now we will deploy using AWS Codedeploy")
print("Commit ID is: " + commitId)

deploy_client = boto3.client('codedeploy', region_name='us-west-2')
response = deploy_client.create_deployment(
    applicationName='windows-codedeploy-demo',
    deploymentGroupName='demo',
    revision={
        'revisionType': 'GitHub',
        'gitHubLocation': {
            'repository': 'bhol/windows-codedeploy-demo',
            'commitId': commitId
        }
    }
)