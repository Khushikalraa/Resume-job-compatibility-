from extractText import extract_resume_text
from extractText import extract_job_text

pdf_path="/Users/salonikalra/assignment/Khushi_Kalra_new (1).pdf"
pdf_path2="/Users/salonikalra/assignment/analystjoblisting.pdf"

resume_text=extract_resume_text(pdf_path)

# if resume_text:
#     print("Extracted Text from PDF: ")
#     print(resume_text)
# else:
#     print("No text could be extracted.")

job_text=extract_job_text(pdf_path2)