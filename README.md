# 🚀 MinIO Bucket Service

## 📋 Description
This is a RESTful API for creating, deleting and listing MinIO buckets.

## ⚙️ Technologies
- FastAPI
- MinIO (via boto3)
- Docker & Docker Compose

## 🛠️ Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/aseelosun/minio-bucket-service.git
   cd minio-bucket-service
   ```
2. Create `.env` from `.env.template`  
   Fill out `MINIO_ACCESS_KEY` and `MINIO_SECRET_KEY` in the `.env`
   For example:
     ```env
     MINIO_ACCESS_KEY=admin
     MINIO_SECRET_KEY=adminsecret
     ```
   **⚠️ Warning**: Access key length should be at least 3, and secret key length at least 8 characters
4. Run with Docker:
   ```sh
   docker compose up --build -d 
   ```
5. Test the API:
   ```sh
   curl -X POST "http://127.0.0.1:8000/buckets?bucket_name=my-versioned-bucket&enable_versioning=true"
   curl -X POST "http://127.0.0.1:8000/buckets?bucket_name=my-bucket"
   curl -X GET "http://127.0.0.1:8000/buckets"
   curl -X DELETE "http://127.0.0.1:8000/buckets?bucket_name=my-bucket"
   ```
6. Run tests:
   ```sh
   docker exec minio-bucket-service pytest
   ```
7. You can also access the MinIO UI at [http://localhost:9001/](http://localhost:9001/) in your browser. 

