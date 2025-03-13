# MinIO Bucket Service

## Description
This is a RESTful API for creating and listing MinIO buckets.

## Technologies
- FastAPI
- MinIO (via boto3)
- Docker & Docker Compose

## Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/minio-bucket-service.git
   cd minio-bucket-service
2. Create `.env` from `.env.template`  
   **⚠️ Warning**: Access key length should be at least 3, and secret key length at least 8 characters
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
4. Run locally:
   ```sh
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
5. Run with Docker:
   ```sh
   docker-compose up --build
6. Test the API:
   ```sh
   curl -X POST "http://127.0.0.1:8000/buckets?bucket_name=my-versioned_bucket&enable_versioning=true"
   curl -X POST "http://127.0.0.1:8000/buckets?bucket_name=my-bucket"
   curl -X GET "http://127.0.0.1:8000/buckets"
7. Run tests:
   ```sh
   pytest tests/
