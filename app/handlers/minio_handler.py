from minio import Minio

class MinioHandler:
    def __init__(self, minio_endpoint: str,
                 access_key: str,
                 secret_key: str,
                 bucket: str,
                 secure: bool = False):

        self.client = Minio(
            minio_endpoint,
            access_key=access_key,
            secret_key=secret_key,
            secure=secure
        )
        self.bucket = bucket

