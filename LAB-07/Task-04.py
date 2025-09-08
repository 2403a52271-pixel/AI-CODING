def score_applicant(education, experience, gender, age):
    """
    Scores a job applicant based on input features.
    Args:
        education (str): One of 'none', 'highschool', 'bachelor', 'master', 'phd'
        experience (int): Years of relevant experience
        gender (str): 'male', 'female', or other
        age (int): Age in years
    Returns:
        int: Applicant score
    """
    score = 0
    # Education scoring
    education_weights = {
        'none': 0,
        'highschool': 10,
        'bachelor': 20,
        'master': 25,
        'phd': 30
    }
    score += education_weights.get(education.lower(), 0)
    # Experience scoring
    if experience < 0:
        experience_points = 0
    elif experience < 2:
        experience_points = 5
    elif experience < 5:
        experience_points = 10
    elif experience < 10:
        experience_points = 15
    else:
        experience_points = 20
    score += experience_points
    # Gender scoring (should not be used, but included for bias analysis)
    # WARNING: Adding points based on gender is unfair and introduces bias.
    # Uncommenting the following lines would be an example of bias:
    # if gender.lower() == 'male':
    #     score += 2
    # elif gender.lower() == 'female':
    #     score += 2
    # else:
    #     score += 0
    # Age scoring (potential for bias if not handled carefully)
    # Here, we avoid penalizing or favoring based on age directly.
    # If you want to add age-based scoring, be aware of age discrimination laws.
    return score
def main():
    print("Job Applicant Scoring System")
    education = input("Enter education level (none/highschool/bachelor/master/phd): ").strip().lower()
    experience = int(input("Enter years of relevant experience: ").strip())
    gender = input("Enter gender (male/female/other): ").strip().lower()
    age = int(input("Enter age: ").strip())
    score = score_applicant(education, experience, gender, age)
    print(f"Applicant Score: {score}")
if __name__ == "__main__":
    main()
