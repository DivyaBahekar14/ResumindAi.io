from openai import OpenAI

client = OpenAI(api_key="Ysk-proj-uHNUD5TY34MtElNyheV2Zvym3shq0XMbHcdX7rsgVt9T7zH5ekgJpnUyfulLcVGKBm-o0UzL02T3BlbkFJ2Mr4jOd3dGb8qCrvQdd0s_2zq3YyBy06sEMsSQs62SLCSDzZ_wPp-RQ4X39WR_qD9lmKtLancA")

def parse_resume_with_llm(cleaned_text: str):

    prompt = f"""
    Extract the following details from the resume text:

    - Name
    - Email
    - Skills (as list)
    - Education
    - Experience

    Return ONLY valid JSON format.

    Resume Text:
    {cleaned_text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content