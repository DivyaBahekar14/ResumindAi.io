from fastapi import FastAPI, UploadFile, File, HTTPException

from validators.file_validator import validate_file
from services.pdf_extractor import extract_text_from_pdf
from utils.text_cleaner import clean_text
from services.llm_parser import parse_resume_with_llm

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    
    try:
        # Step 1: Validate
        content = await validate_file(file)

        # Step 2: Extract text
        extracted_text = extract_text_from_pdf(content)

        # Step 3: Clean text
        cleaned_text = clean_text(extracted_text)

        # Step 4: LLM parsing
        parsed_data = parse_resume_with_llm(cleaned_text)

        return {
            "filename": file.filename,
            "parsed_data": parsed_data
        }

    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))