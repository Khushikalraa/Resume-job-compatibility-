from dataStructuring import resume_data
from dataStructuring import job_listing_data

def calculate_metrics(matched_set, resume_set, job_listing_set):
    true_positives = len(matched_set)
    false_positives = len(matched_set - job_listing_set)
    false_negatives = len(job_listing_set - matched_set)

    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
    f1_score = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

    return {
        "precision": precision,
        "recall": recall,
        "f1_score": f1_score
    }

# Matching logic
def match_skills(resume_skills, job_skills):
    return set(resume_skills) & set(job_skills)

def match_experience(resume_experience, job_experience):
    return set(resume_experience) & set(job_experience)

def match_education(resume_education, job_education):
    return set(resume_education) & set(job_education)

# Calculation of matching sets
matching_skills = match_skills(resume_data["skills"], job_listing_data["skills"])
matching_experience = match_experience(resume_data["experience"], job_listing_data["experience"])
matching_education = match_education(resume_data["education"], job_listing_data["education"])

# Calculation of metrics for each category
skills_metrics = calculate_metrics(matching_skills, set(resume_data["skills"]), set(job_listing_data["skills"]))
experience_metrics = calculate_metrics(matching_experience, set(resume_data["experience"]), set(job_listing_data["experience"]))
education_metrics = calculate_metrics(matching_education, set(resume_data["education"]), set(job_listing_data["education"]))

# results
print("Skills Metrics:", skills_metrics)
print("Experience Metrics:", experience_metrics)
print("Education Metrics:", education_metrics)

# Overall performance
total_matched = len(matching_skills) + len(matching_experience) + len(matching_education)
total_possible = len(set(job_listing_data["skills"])) + len(set(job_listing_data["experience"])) + len(set(job_listing_data["education"]))
overall_precision = total_matched / total_possible if total_possible > 0 else 0

print("Overall Precision:", overall_precision)
