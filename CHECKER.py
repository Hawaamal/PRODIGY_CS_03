import re

# Function to check password strength
def check_password_strength(password):
    # Criteria checks
    length_ok = len(password) >= 8
    upper_case_ok = bool(re.search(r'[A-Z]', password))
    lower_case_ok = bool(re.search(r'[a-z]', password))
    number_ok = bool(re.search(r'\d', password))
    special_char_ok = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Feedback collection
    feedback = []

    if not length_ok:
        feedback.append("Password must be at least 8 characters long.")
    if not upper_case_ok:
        feedback.append("Password must contain at least one uppercase letter.")
    if not lower_case_ok:
        feedback.append("Password must contain at least one lowercase letter.")
    if not number_ok:
        feedback.append("Password must contain at least one number.")
    if not special_char_ok:
        feedback.append("Password must contain at least one special character (e.g., @, #, $, %, etc.).")

    # Determine password strength
    if len(feedback) == 0:
        strength = "Very Strong"
    elif len(feedback) == 1:
        strength = "Moderate"
    elif len(feedback) == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return feedback, strength

def main():
    # Custom ASCII Art for "Check It" Tool Header
    print(r"""
    
_________   ___ _______________________  ____  __. .______________
\_   ___ \ /   |   \_   _____/\_   ___ \|    |/ _| |   \__    ___/
/    \  \//    ~    \    __)_ /    \  \/|      <   |   | |    |   
\     \___\    Y    /        \\     \___|    |  \  |   | |    |   
 \______  /\___|_  /_______  / \______  /____|__ \ |___| |____|   
        \/       \/        \/         \/        \/                

                                                                
                            Password Strength Checker
    """)

    print("=" * 70)
    print("Welcome to Check It - Your Password Strength Checker Tool!")
    print("=" * 70)

    # Ask user for password input
    password = input("Enter your password to check its strength: ")

    # Get feedback and strength from the function
    feedback, strength = check_password_strength(password)

    print("\nPassword Strength:", strength)
    print("=" * 70)

    # Display the feedback if there are any issues with the password
    if feedback:
        print("Feedback for improving your password:")
        for message in feedback:
            print(f"- {message}")
    else:
        print("Your password meets all the strength criteria!")

    print("=" * 70)
    print("Thank you for using Check It!")

if __name__ == "__main__":
    main()
