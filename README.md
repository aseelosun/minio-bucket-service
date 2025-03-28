# 🚀 MinIO Bucket Service

## 📋 Description
This is a RESTful API for creating and listing MinIO buckets.

## ⚙️ Technologies
- FastAPI
- MinIO (via boto3)
- Docker & Docker Compose

## 🛠️ Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/aseelosun/minio-bucket-service.git
   cd minio-bucket-service
2. Create `.env` from `.env.template`  
   **⚠️ Warning**: Access key length should be at least 3, and secret key length at least 8 characters
3. Run with Docker:
   ```sh
   docker compose up --build
4. Test the API:
   ```sh
   curl -X POST "http://127.0.0.1:8000/buckets?bucket_name=my-versioned-bucket&enable_versioning=true"
   curl -X POST "http://127.0.0.1:8000/buckets?bucket_name=my-bucket"
   curl -X GET "http://127.0.0.1:8000/buckets"
4. Run tests:
   ```sh
   docker exec minio-bucket-service pytest

