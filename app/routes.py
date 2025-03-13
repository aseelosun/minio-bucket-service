from fastapi import APIRouter,Query
from .minio_client import create_bucket, list_buckets, remove_bucket

router = APIRouter()

@router.post("/buckets")
def create_new_bucket(bucket_name: str, enable_versioning: bool = Query(False)):
    return create_bucket(bucket_name, enable_versioning)

@router.get("/buckets")
def get_buckets():
    return list_buckets()

@router.delete("/buckets")
def delete_bucket(bucket_name: str):
    return remove_bucket(bucket_name)
