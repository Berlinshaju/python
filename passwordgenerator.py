import random
import string

def generate_password(length):
    # Define the character set for the password, excluding specified characters
    characters = string.ascii_letters + string.digits + string.punctuation
    exclude_chars = "}{(%)"  # Characters to exclude
    characters = ''.join([c for c in characters if c not in exclude_chars])
    
    # Generate the password by selecting random characters from the character set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user for password length
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Length must be greater than zero. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    # Generate a password of the specified length, excluding specified characters
    random_password = generate_password(length)
    
    # Print the generated password
    print("Random Password:", random_password)

if __name__ == "__main__":
    main()
