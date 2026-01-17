from fastapi import APIRouter, Depends
from app.core.r2 import s3_client, R2_BUCKET_NAME
from app.schemas.image import ImageUploadRequest
import os

router = APIRouter(prefix="/images", tags=["Images"])

@router.post("/upload-url")
def get_upload_url(data: ImageUploadRequest):
    key = f"questions/{data.question_id}/{data.filename}"

    upload_url = s3_client.generate_presigned_url(
        "put_object",
        Params={
            "Bucket": os.getenv("R2_BUCKET_NAME"),
            "Key": key,
            "ContentType": data.content_type,
        },
        ExpiresIn=300,
    )

    public_url = f"https://{os.getenv('R2_BUCKET_NAME')}.r2.dev/{key}"

    return {
        "upload_url": upload_url,
        "public_url": public_url,
    }
