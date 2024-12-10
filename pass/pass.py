import random
import string
def generate_password(length, use_uppercase, use_digits, use_special):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special_characters = string.punctuation if use_special else ''
    all_characters = lowercase + uppercase + digits + special_characters
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_digits:
        password.append(random.choice(digits))
    if use_special:
        password.append(random.choice(special_characters))
    password += random.choices(all_characters, k=length - len(password))
    random.shuffle(password)
    return ''.join(password)
def main():
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    password = generate_password(length, use_uppercase, use_digits, use_special)
    print(f"Generated Password: {password}")
if __name__ == "__main__":
    main()
