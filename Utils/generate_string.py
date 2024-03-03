import random
import string


def generate_text(length=6):
    """
    Generates a secure password of a given length.

    Parameters:
    - length (int): The desired length of the password.

    Returns:
    - str: A secure password string.
    """
    # Combine all the required character groups
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

    # Ensure the password contains at least one character from each group
    if length < 4:
        raise ValueError("Password length must be at least 4 characters to include all character types.")

    # Securely select at least one character from each group
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    # Fill the rest of the password length with random choices from the combined characters
    password += random.choices(characters, k=length - 4)

    # Shuffle the password list to mix up the character types
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)
