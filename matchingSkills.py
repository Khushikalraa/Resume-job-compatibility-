from dataStructuring import resume_data
from dataStructuring import job_listing_data

def match_skills(resume_skills, job_skills):
    return set(resume_skills)&set(job_skills)

matching_skills=match_skills(resume_data["skills"],job_listing_data["skills"])
print("Matching Skills: ",matching_skills)

def match_experience(resume_experience, job_experience):
    return set(resume_experience) & set(job_experience)

matching_experience = match_experience(resume_data["experience"], job_listing_data["experience"])
print("Matching Experience:", matching_experience)

def match_education(resume_education, job_education):
    return set(resume_education) & set(job_education)

matching_education = match_education(resume_data["education"], job_listing_data["education"])
print("Matching Education:", matching_education)

def match_all(resume_data, job_listing_data):
    matched_skills = match_skills(resume_data["skills"], job_listing_data["skills"])
    matched_experience = match_experience(resume_data["experience"], job_listing_data["experience"])
    matched_education = match_education(resume_data["education"], job_listing_data["education"])

    return {
        "skills": matched_skills,
        "experience": matched_experience,
        "education": matched_education
    }

# Calling the matching function and print results
matching_data = match_all(resume_data, job_listing_data)
print("Matching Data:", matching_data)
