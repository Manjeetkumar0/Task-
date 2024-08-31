import re

def password_complexity_checker(password):
    # Ensure the password is a string
    if not isinstance(password, str):
        raise ValueError("Password must be a string.")

    # Check conditions using regex for better accuracy
    length = len(password) >= 8
    uppercase = re.search(r'[A-Z]', password) is not None
    lowercase = re.search(r'[a-z]', password) is not None
    digit = re.search(r'\d', password) is not None
    special = re.search(r'[^A-Za-z0-9]', password) is not None

    # Display individual checks
    print(f"Password: {password}")
    print(f"Length (>= 8 characters): {'Pass' if length else 'Fail'}")
    print(f"Contains Uppercase Letter: {'Pass' if uppercase else 'Fail'}")
    print(f"Contains Lowercase Letter: {'Pass' if lowercase else 'Fail'}")
    print(f"Contains Digit: {'Pass' if digit else 'Fail'}")
    print(f"Contains Special Character: {'Pass' if special else 'Fail'}")

    # Calculate strength score
    score = sum([length, uppercase, lowercase, digit, special])

    # Map score to password strength
    strength_map = {
        5: "Very Strong",
        4: "Strong",
        3: "Medium",
        2: "Weak",
        1: "Very Weak",
        0: "Very Weak"
    }

    # Output the password strength
    print(f"Password Strength: {strength_map[score]}")

    # Provide feedback for improvement
    if not length:
        print("Tip: Use at least 8 characters.")
    if not uppercase:
        print("Tip: Include uppercase letters (A-Z).")
    if not lowercase:
        print("Tip: Include lowercase letters (a-z).")
    if not digit:
        print("Tip: Add at least one digit (0-9).")
    if not special:
        print("Tip: Use special characters (e.g., @, #, $, etc.).")

# Exception handling for user input
try:
    password = input("Enter a password to check its strength: ")
    password_complexity_checker(password)
except ValueError as e:
    print(f"Error: {e}")