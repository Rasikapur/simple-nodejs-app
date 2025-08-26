import boto3

# Create an ECR client
ecr = boto3.client('ecr', region_name="ap-south-1")

# Create repository
response = ecr.create_repository(
    repositoryName="simple-nodejs"
)

print("Repository created:", response["repository"]["repositoryUri"])

