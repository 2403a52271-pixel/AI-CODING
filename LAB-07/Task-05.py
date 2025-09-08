def greet_user(name, gender):
    gender_lower = gender.lower()
    if gender_lower == "male":
        title = "Mr."
    elif gender_lower == "female":
        title = "Ms."
    else:
        title = "Mx."
    return f"Hello {title} {name}! Welcome."
if __name__ == "__main__":
    name = input("Enter your name: ").strip()
    gender = input("Enter your gender (male/female/other): ").strip()
    greeting = greet_user(name, gender)
print(greeting)