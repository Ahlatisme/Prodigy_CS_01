import re

def password_strength(password):
    # Criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None
    
    # Evaluate strength
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    
    if criteria_met == 5:
        return "Strong"
    elif criteria_met >= 3:
        return "Moderate"
    else:
        return "Weak"

def feedback(password):
    feedback_messages = []
    
    if len(password) < 8:
        feedback_messages.append("Password should be at least 8 characters long.")
    if re.search(r'[A-Z]', password) is None:
        feedback_messages.append("Password should include at least one uppercase letter.")
    if re.search(r'[a-z]', password) is None:
        feedback_messages.append("Password should include at least one lowercase letter.")
    if re.search(r'[0-9]', password) is None:
        feedback_messages.append("Password should include at least one number.")
    if re.search(r'[\W_]', password) is None:
        feedback_messages.append("Password should include at least one special character.")
    
    if not feedback_messages:
        feedback_messages.append("Your password is strong.")
    
    return feedback_messages

def main():
    while True:
        password = input("Enter a password to assess its strength (or type 'Q' to quit): ")
        if password.upper() == 'Q':
            print("Goodbye!")
            break

        strength = password_strength(password)
        feedback_messages = feedback(password)

        print(f"Password Strength: {strength}")
        print("Feedback:")
        for message in feedback_messages:
            print(f"- {message}")

if __name__ == "__main__":
    main()