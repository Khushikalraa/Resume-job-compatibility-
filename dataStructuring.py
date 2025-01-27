from extractedInfo import extracted_skills, extracted_experience, extracted_education
from extractedInfoJob import extracted_skills_from_job_listing, extracted_experience_from_job_listing, extracted_education_from_job_listing

resume_data={
    "skills":extracted_skills,
    "experience":extracted_experience["job_titles"],
    "education": extracted_education["degrees"]
}

job_listing_data ={
    "skills": extracted_skills_from_job_listing,
    "experience":extracted_experience_from_job_listing["job_titles"],
    "education": extracted_education_from_job_listing["degrees"]
}