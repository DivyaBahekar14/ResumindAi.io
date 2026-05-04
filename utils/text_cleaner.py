import re

def clean_text(text: str) -> str:
    
    # 1. Convert to lowercase
    text = text.lower()

    # 2. Remove emails extra spaces formatting issues
    text = re.sub(r'\s+', ' ', text)

    # 3. Remove special characters (keep basic ones)
    text = re.sub(r'[^a-z0-9@.\s]', '', text)

    # 4. Remove multiple spaces again
    text = re.sub(r'\s+', ' ', text)

    # 5. Trim
    text = text.strip()

    return text