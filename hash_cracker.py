import hashlib
import itertools
import string

def hash_password(password, algorithm='sha256'):
    """Hashes the given password using the specified hashing algorithm."""
    hash_object = hashlib.new(algorithm)
    hash_object.update(password.encode('utf-8'))
    return hash_object.hexdigest()

def brute_force_crack(hashed_password, algorithm='sha256'):
    """Brute-force approach to crack the hashed password."""
    charset = string.ascii_letters + string.digits + string.punctuation  # Charset for brute-force
    for length in range(1, 9):  # Trying passwords from length 1 to 8
        for attempt in itertools.product(charset, repeat=length):
            password = ''.join(attempt)
            if hash_password(password, algorithm) == hashed_password:
                return password
    return None

def dictionary_attack(hashed_password, wordlist, algorithm='sha256'):
    """Cracks the hashed password using a dictionary attack."""
    with open(wordlist, 'r') as file:
        for line in file:
            password = line.strip()
            if hash_password(password, algorithm) == hashed_password:
                return password
    return None

def main():
    print("Welcome to the Hash Cracker Tool!")
    hashed_password = input("Enter the hashed password: ")
    attack_type = input("Choose attack type (1: Brute Force, 2: Dictionary Attack): ")

    if attack_type == '1':
        print("Starting Brute Force Attack...")
        cracked_password = brute_force_crack(hashed_password)
    elif attack_type == '2':
        wordlist_path = input("Enter the path to the wordlist file (wordlist.txt): ")
        print("Starting Dictionary Attack...")
        cracked_password = dictionary_attack(hashed_password, wordlist_path)
    else:
        print("Invalid attack type.")
        return

    if cracked_password:
        print(f"Password cracked: {cracked_password}")
    else:
        print("Password not found.")

if __name__ == "__main__":
    main()
