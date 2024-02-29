import random
import string

def generate_password(length, complexity):
    if complexity == 'low':
        chars = string.ascii_letters + string.digits
    elif complexity == 'medium':
        chars = string.ascii_letters + string.digits + string.punctuation
    elif complexity == 'high':
        chars = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("Welcome to Password Generator")

    while True:
        length = int(input("Enter the length of the password: "))
        complexity = input("Enter complexity (low/medium/high): ")

        if complexity not in ['low', 'medium', 'high']:
            print("Invalid complexity level. Please choose from 'low', 'medium', or 'high'.")
            continue

        password = generate_password(length, complexity)
        print("Generated Password:", password)

        another = input("Generate another password? (yes/no): ")
        if another.lower() != 'yes':
            print("Thank you for using Password Generator")
            break

if __name__ == "__main__":
    main()
