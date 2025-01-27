from main import job_text

def clean_text2(text):
    text=text.replace("\n"," ").strip()
    return text

cleaned_job_text = clean_text2(job_text)
# print("Cleaned Text: ", cleaned_job_text)