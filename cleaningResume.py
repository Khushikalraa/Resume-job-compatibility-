from main import resume_text

def clean_text(text):
    text=text.replace("\n"," ").strip()
    return text

cleaned_text = clean_text(resume_text)
# print("Cleaned Text: ", cleaned_text)