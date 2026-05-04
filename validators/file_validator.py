from fastapi import UploadFile, HTTPException

MAX_FILE_SIZE = 2 * 1024 * 1024  # 2MB

async def validate_file(file: UploadFile):
    
    # File type check
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    content = await file.read()

    # File size check
    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File too large")
    
    if len(content) == 0:
        raise HTTPException(status_code=400, detail="Empty file")

    return content