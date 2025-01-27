import spacy
from spacy.matcher import Matcher
from cleaningJobListing import cleaned_job_text

# Loading spaCy's pre-trained model
nlp = spacy.load("en_core_web_sm")

# Defining skill extraction function
def extract_skills(text):
    doc = nlp(text)
    matcher = Matcher(nlp.vocab)
    
    # Defining patterns for skills (e.g., programming languages, tools)
    patterns = [[{"LOWER": "python"}], [{"LOWER": "java"}], [{"LOWER": "c"}], [{"LOWER": "c++"}], [{"LOWER": "c#"}],
    [{"LOWER": "sql"}], [{"LOWER": "javascript"}], [{"LOWER": "typescript"}], [{"LOWER": "html"}],
    [{"LOWER": "css"}], [{"LOWER": "bash"}], [{"LOWER": "powershell"}], [{"LOWER": "kotlin"}],
    [{"LOWER": "swift"}], [{"LOWER": "php"}], [{"LOWER": "ruby"}], [{"LOWER": "go"}], [{"LOWER": "r"}],
    [{"LOWER": "matlab"}], [{"LOWER": "sas"}], [{"LOWER": "scala"}], [{"LOWER": "dart"}], [{"LOWER": "perl"}],
    [{"LOWER": "shell"}], [{"LOWER": "tensorflow"}], [{"LOWER": "pandas"}], [{"LOWER": "numpy"}],
    [{"LOWER": "matplotlib"}], [{"LOWER": "seaborn"}], [{"LOWER": "scikit"}, {"LOWER": "learn"}],
    [{"LOWER": "keras"}], [{"LOWER": "torch"}], [{"LOWER": "pytorch"}], [{"LOWER": "nlp"}], [{"LOWER": "spacy"}],
    [{"LOWER": "nltk"}], [{"LOWER": "hadoop"}], [{"LOWER": "spark"}], [{"LOWER": "kafka"}],
    [{"LOWER": "airflow"}], [{"LOWER": "mysql"}], [{"LOWER": "postgresql"}], [{"LOWER": "mongodb"}],
    [{"LOWER": "firebase"}], [{"LOWER": "elasticsearch"}], [{"LOWER": "redis"}], [{"LOWER": "docker"}],
    [{"LOWER": "kubernetes"}], [{"LOWER": "aws"}], [{"LOWER": "azure"}], [{"LOWER": "gcp"}],
    [{"LOWER": "heroku"}], [{"LOWER": "terraform"}], [{"LOWER": "ansible"}], [{"LOWER": "jenkins"}],
    [{"LOWER": "circleci"}], [{"LOWER": "travis"}], [{"LOWER": "github"}], [{"LOWER": "gitlab"}],
    [{"LOWER": "bitbucket"}], [{"LOWER": "jira"}], [{"LOWER": "trello"}], [{"LOWER": "confluence"}],
    [{"LOWER": "salesforce"}], [{"LOWER": "sap"}], [{"LOWER": "tableau"}], [{"LOWER": "power"}, {"LOWER": "bi"}],
    [{"LOWER": "excel"}], [{"LOWER": "microsoft"}, {"LOWER": "office"}], [{"LOWER": "visual"}, {"LOWER": "studio"}],
    [{"LOWER": "intellij"}], [{"LOWER": "pycharm"}], [{"LOWER": "eclipse"}], [{"LOWER": "vscode"}],
    [{"LOWER": "notepad++"}], [{"LOWER": "flask"}], [{"LOWER": "django"}], [{"LOWER": "fastapi"}],
    [{"LOWER": "react"}], [{"LOWER": "angular"}], [{"LOWER": "vue"}], [{"LOWER": "svelte"}],
    [{"LOWER": "nextjs"}], [{"LOWER": "nestjs"}], [{"LOWER": "spring"}], [{"LOWER": "springboot"}],
    [{"LOWER": "hibernate"}], [{"LOWER": "express"}], [{"LOWER": "laravel"}], [{"LOWER": "ruby"}, {"LOWER": "rails"}],
    [{"LOWER": "flutter"}], [{"LOWER": "react"}, {"LOWER": "native"}], [{"LOWER": "ionic"}],
    [{"LOWER": "capacitor"}], [{"LOWER": "tailwindcss"}], [{"LOWER": "bootstrap"}], [{"LOWER": "git"}],
    [{"LOWER": "tesseract"}], [{"LOWER": "creative"}, {"LOWER": "problem"}, {"LOWER": "solving"}],
    [{"LOWER": "cooperative"}, {"LOWER": "teamwork"}], [{"LOWER": "time"}, {"LOWER": "management"}],
    [{"LOWER": "communication"}, {"LOWER": "skills"}], [{"LOWER": "powerpoint"}], [{"LOWER": "word"}],
    [{"LOWER": "leadership"}], [{"LOWER": "critical"}, {"LOWER": "thinking"}], [{"LOWER": "adaptability"}],
    [{"LOWER": "decision"}, {"LOWER": "making"}], [{"LOWER": "problem"}, {"LOWER": "solving"}],
    [{"LOWER": "machine"}, {"LOWER": "learning"}], [{"LOWER": "deep"}, {"LOWER": "learning"}],
    [{"LOWER": "business"}, {"LOWER": "analysis"}], [{"LOWER": "cloud"}, {"LOWER": "computing"}],
    [{"LOWER": "data"}, {"LOWER": "visualization"}], [{"LOWER": "data"}, {"LOWER": "engineering"}],
    [{"LOWER": "agile"}, {"LOWER": "development"}], [{"LOWER": "scrum"}], [{"LOWER": "kanban"}],
    [{"LOWER": "big"}, {"LOWER": "data"}], [{"LOWER": "ci/cd"}], [{"LOWER": "observability"}],
    [{"LOWER": "devops"}], [{"LOWER": "test"}, {"LOWER": "automation"}], [{"LOWER": "ui"}, {"LOWER": "design"}],
    [{"LOWER": "ux"}, {"LOWER": "research"}], [{"LOWER": "product"}, {"LOWER": "management"}],
    [{"LOWER": "software"}, {"LOWER": "architecture"}], [{"LOWER": "mobile"}, {"LOWER": "development"}],[{"LOWER": "node"}, {"LOWER": "js"}],]
    
    matcher.add("SKILL", patterns)

    # Finding matches
    matches = matcher(doc)
    skills = set([doc[start:end].text for match_id, start, end in matches])

    return skills

# Extracting skills from cleaned text
extracted_skills_from_job_listing = extract_skills(cleaned_job_text)
print("Extracted Skills:", extracted_skills_from_job_listing)

print('\n')
print('\n')

# Defining experience extraction function
def extract_experience(text):
    import spacy
    from spacy.matcher import Matcher

    # Loading spaCy language model
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    matcher = Matcher(nlp.vocab)

    # Refining job title patterns
    job_patterns = [
    # Matching three-component titles (e.g., "Data Analytics Intern")
    [{"LOWER": {"REGEX": r"(data|software|machine|business|quality|security|test|backend|frontend|fullstack|solutions|devops|ai|ml|product|project|engineering|research|cto|cso|data visualization|hr|summer)"}}, 
     {"LOWER": {"REGEX": r"(analytics|learning|development|analysis|management|science|engineering|visualization|hr|summer)"}}, 
     {"LOWER": {"REGEX": r"(intern|trainee|engineer|developer|manager|scientist|analyst|consultant|officer)"}}],

    # Matching two-component titles (e.g., "HR Intern", "Summer Trainee")
    [{"LOWER": {"REGEX": r"(data|software|machine|business|quality|security|test|backend|frontend|fullstack|solutions|devops|ai|ml|product|project|engineering|research|cto|cso|data visualization|hr|summer)"}}, 
     {"LOWER": {"REGEX": r"(intern|trainee|engineer|developer|manager|scientist|analyst|consultant|officer)"}}],]


    matcher.add("JOB_TITLES", job_patterns)

    # Matching job titles
    matches = matcher(doc)
    raw_job_titles = [doc[start:end].text.strip() for match_id, start, end in matches]

    # Filtering results to remove overly long or irrelevant matches
    job_titles = [
        title for title in raw_job_titles
        if len(title.split()) <= 5  # Limit to 5 words max for a job title
        and any(keyword in title.lower() for keyword in ["intern", "trainee", "engineer", "analyst", "developer", "manager"])
    ]

    return {"job_titles": job_titles}


extracted_experience_from_job_listing = extract_experience(cleaned_job_text)
print("Extracted Experience:", extracted_experience_from_job_listing)


print('\n')
print('\n')

# Defining education extraction function
def extract_education(text):
    doc = nlp(text)
    matcher = Matcher(nlp.vocab)

    # Patterns for degrees
    degree_patterns = [
    [{"LOWER": "bachelor"}, {"LOWER": "of"}, {"LOWER": "technology"}],
    [{"LOWER": "bachelor"}, {"LOWER": "of"}, {"LOWER": "science"}],
    [{"LOWER": "bachelor"}, {"LOWER": "of"}, {"LOWER": "arts"}],
    [{"LOWER": "bachelor"}, {"LOWER": "of"}, {"LOWER": "engineering"}],
    [{"LOWER": "bachelor"}, {"LOWER": "of"}, {"LOWER": "commerce"}],
    [{"LOWER": "master"}, {"LOWER": "of"}, {"LOWER": "technology"}],
    [{"LOWER": "master"}, {"LOWER": "of"}, {"LOWER": "science"}],
    [{"LOWER": "master"}, {"LOWER": "of"}, {"LOWER": "business"}, {"LOWER": "administration"}],
    [{"LOWER": "master"}, {"LOWER": "of"}, {"LOWER": "arts"}],
    [{"LOWER": "phd"}],
    [{"LOWER": "doctorate"}],
    [{"LOWER": "m.sc"}],
    [{"LOWER": "b.sc"}],
    [{"LOWER": "m.tech"}],
    [{"LOWER": "b.tech"}],
    [{"LOWER": "mba"}],[{"LOWER":"any"},{"LOWER":"graduate"}],[{"LOWER":"any"},{"LOWER":"postgraduate"}]
]


    matcher.add("DEGREES", degree_patterns)

    # Finding degree matches
    matches = matcher(doc)
    degrees = [doc[start:end].text for match_id, start, end in matches]

    # # Extracting institution names and graduation years
    # institutions = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
    # graduation_years = [ent.text for ent in doc.ents if ent.label_ == "DATE"]

    return {"degrees": degrees}

# Extracting education from cleaned text
extracted_education_from_job_listing = extract_education(cleaned_job_text)
print("Extracted Education:", extracted_education_from_job_listing)

