import re

def is_valid_email(email):
    """Check if the provided email address is valid."""
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if re.match(email_regex, email):
        return True
    return False

def validate_emails_from_file(file_path):
    """Read emails from a file and check their validity."""
    try:
        with open(file_path, 'r') as file:
            emails = file.readlines()
        # Clean up newlines and extra spaces
        emails = [email.strip() for email in emails]

        for email in emails:
            if is_valid_email(email):
                print(f"{email} is a valid email.")
            else:
                print(f"{email} is not a valid email.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"Error: {e}")

if name == "main":
    file_path = input("Enter the path to the email list file: ")
    validate_emails_from_file(file_path)
