import boto3
from botocore.exceptions import BotoCoreError, NoCredentialsError
from .config import MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY

# Initialize MinIO Client
s3_client = boto3.client(
    "s3",
    endpoint_url=MINIO_ENDPOINT,
    aws_access_key_id=MINIO_ACCESS_KEY,
    aws_secret_access_key=MINIO_SECRET_KEY
)

def create_bucket(bucket_name: str, enable_versioning: bool = False ):
    """Create a new bucket in MinIO"""
    try:
        s3_client.create_bucket(Bucket=bucket_name)

        if enable_versioning:
            s3_client.put_bucket_versioning(
                Bucket=bucket_name,
                VersioningConfiguration={"Status": "Enabled"}
            )

        return {"message": f"Bucket '{bucket_name}' created successfully."}
    except s3_client.exceptions.BucketAlreadyOwnedByYou:
        return {"error": f"Bucket '{bucket_name}' already exists."}
    except (BotoCoreError, NoCredentialsError) as e:
        return {"error": str(e)}
    

def list_buckets():
    """List all buckets"""
    try:
        response = s3_client.list_buckets()
        return {"buckets": [bucket["Name"] for bucket in response["Buckets"]]}
    except (BotoCoreError, NoCredentialsError) as e:
        return {"error": str(e)}

def remove_bucket(bucket_name: str):
    """Remove a bucket in MinIO"""
    try:
        s3_client.delete_bucket(Bucket=bucket_name)
        return {"message": f"Bucket '{bucket_name}' removed successfully."}
    except s3_client.exceptions.NoSuchBucket:
        return {"error": f"Bucket '{bucket_name}' does not exist."}
    except (BotoCoreError, NoCredentialsError) as e:
        return {"error": str(e)}
