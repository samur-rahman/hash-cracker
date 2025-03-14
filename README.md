# Hash Cracker (Brute Force & Dictionary Attack)

## Overview
This is a simple Python tool that attempts to crack hashed passwords using **Brute Force** and **Dictionary Attack** techniques. The tool supports common hashing algorithms and simulates rainbow tables and salted hashes.

## Tech Stack
- **Python** (`hashlib`, `itertools`)

## Concepts Covered
- **Hashing**
- **Brute-Force Attacks**
- **Dictionary Attack**
- **Rainbow Tables**
- **Salted Hashes**

## Project Structure
 **`hash-cracker/`** (Main Project Folder)  
  - **`hash_cracker.py`** - Main script to execute the hash cracking process  
  - **`wordlist.txt`** - List of common passwords for dictionary attack  
  - **`README.md`** - Documentation for the project  


## How It Works

1. **Hashing**: The `hash_password` function hashes passwords using the selected algorithm (default is SHA-256).
2. **Brute Force Attack**: Attempts to crack the hash by testing all combinations of characters (letters, digits, and punctuation) for passwords of length 1 to 8.
3. **Dictionary Attack**: Uses a wordlist (`wordlist.txt`) to check common passwords against the given hash.
4. **Crack Result**: The tool will output the cracked password or inform the user if it couldn't find a match.

## Setup & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/samur-rahman/hash-cracker.git
