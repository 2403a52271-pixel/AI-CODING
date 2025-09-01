def classify_age(age):
    if age >= 0:
        if age <= 12:
            return "Child"
        elif age <= 19:
            return "Teen"
        elif age <= 59:
            return "Adult"
        else:
            return "Senior"
    else:
        return "Invalid age"
ages_to_test = [5, 15, 35, 65, -3]
for age in ages_to_test:
    print(f"Age: {age} -> Group: {classify_age(age)}")
def classify_age_flat(age):
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teen"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"
for age in ages_to_test:
    print(f"Age: {age} -> Group (flat): {classify_age_flat(age)}")
