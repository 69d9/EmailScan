import requests
from termcolor import colored
import argparse

def search_facebook(email):
    """Attempt to check if the email is associated with a Facebook account."""
    try:
        # Searching on Google for the email associated with Facebook
        search_url = f"https://www.google.com/search?q={email}+site:facebook.com"
        response = requests.get(search_url)
        if "facebook.com" in response.text:
            return True
        return False
    except Exception as e:
        return f"Error: {e}"

def search_instagram(email):
    """Attempt to check if the email is associated with an Instagram account."""
    try:
        # Searching on Google for the email associated with Instagram
        search_url = f"https://www.google.com/search?q={email}+site:instagram.com"
        response = requests.get(search_url)
        if "instagram.com" in response.text:
            return True
        return False
    except Exception as e:
        return f"Error: {e}"

def search_discord(email):
    """Attempt to check if the email is associated with a Discord account."""
    try:
        # Searching on Google for the email associated with Discord
        search_url = f"https://www.google.com/search?q={email}+site:discord.com"
        response = requests.get(search_url)
        if "discord.com" in response.text:
            return True
        return False
    except Exception as e:
        return f"Error: {e}"

def check_email_on_platforms(email):
    """Check if an email is associated with multiple platforms (Facebook, Instagram, Discord)."""
    platforms = {
        'Facebook': search_facebook,
        'Instagram': search_instagram,
        'Discord': search_discord
    }

    results = {}
    for platform, search_function in platforms.items():
        try:
            results[platform] = search_function(email)
        except Exception as e:
            results[platform] = f"Error: {e}"

    return results

def check_emails_from_list(email_list):
    """Check multiple emails and print their status on different platforms."""
    for email in email_list:
        results = check_email_on_platforms(email)
        print(f"\nResults for {email}:")
        for platform, status in results.items():
            color = 'green' if status else 'red'
            print(colored(f"{platform}: {'Registered' if status else 'Not Registered'}", color))

def load_emails_from_file(file_path):
    """Load emails from a text file."""
    try:
        with open(file_path, 'r') as file:
            emails = file.readlines()
        # Remove extra whitespace
        return [email.strip() for email in emails]
    except FileNotFoundError:
        print("Error: The file was not found.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

def main():
    # Setting up argument parser to accept the file path from the command line
    parser = argparse.ArgumentParser(description="Check if emails are registered on Facebook, Instagram, and Discord.")
    parser.add_argument('file', type=str, help="The path to the text file containing the email list.")
    args = parser.parse_args()
    
    # Load emails from the file provided in the command line
    email_list = load_emails_from_file(args.file)
    
    if email_list:
        check_emails_from_list(email_list)
    else:
        print("No emails to check.")

if name == "main":
    main()

# Written by a human, for educational purposes.
