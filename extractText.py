from pdfminer.high_level import extract_text

def extract_resume_text(pdf_path):
    try:
        return extract_text(pdf_path)
    except Exception as e:
            print(f"Error reading {pdf_path}:{e}")
            return ""

def extract_job_text(pdf_path2):
    try:
        return extract_text(pdf_path2)
    except Exception as e:
        print(f"Error reading {pdf_path2}:{e}")
        return ""
