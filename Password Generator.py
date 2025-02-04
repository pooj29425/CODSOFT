import random
import string

def generate_password(length=8):
    if length < 8:
        return "Password must be at least 8 characters long"
    
    chars = string.ascii_letters + string.digits + string.punctuation
    password = (
        random.choice(string.ascii_lowercase) +
        random.choice(string.ascii_uppercase) +
        random.choice(string.digits) +
        random.choice(string.punctuation) +
        ''.join(random.choices(chars, k=length - 4))
    )
    
    return ''.join(random.sample(password, len(password)))  # Shuffle the password

while True:
    try:
        length = int(input("Enter password length (min 8): "))
        print(f"Generated Password: {generate_password(length)}")
        
        if input("Generate another? (y/n): ").lower() != 'y':
            print("Goodbye!")
            break
    except ValueError:
        print("Please enter a valid number.")
