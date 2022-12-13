# Hash Cracker

The project can be found at [FreeCodeCamp](https://www.freecodecamp.org/learn/information-security/information-security-projects/sha-1-password-cracker)

# Install

Open your terminal or command prompt.  
Navigate to the directory where you want to clone the project.

Use the command ```git clone``` followed by the project's URL from GitHub.  
```git clone https://github.com/0xzaid/hash-cracker.git```

This will create a new directory with the project's name in the current directory.  
Navigate to the project's directory using the "cd" command.  
```cd hash-cracker```

The project should is now on your machine.

# Usage

To use password_cracker.py, open a terminal or command prompt and navigate to the directory where the program is saved. Then, run the following command:
```
usage: password_cracker.py [-h] [-m {SHA1,SHA256,SHA512,MD5}] [-v] [-s] wordlist hash
```

To ask for help:
```
python password_cracker.py -h
```
This results in:
```
usage: password_cracker.py [-h] [-m {SHA1,SHA256,SHA512,MD5}] [-v] [-s] wordlist hash

Hash Cracker

positional arguments:
  wordlist              path to the wordlist to use for cracking the hash
  hash                  the hash to crack

options:
  -h, --help            show this help message and exit
  -m {SHA1,SHA256,SHA512,MD5}, --mode {SHA1,SHA256,SHA512,MD5}
                        cracking algorithm to use
  -v, --verbose         enable verbose output
  -s, --salt            enable salted cracking
```
