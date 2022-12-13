import hashlib
import argparse
from colorama import Fore


def read_file(file_name):
    # Open the file and read the contents
    with open(file_name, 'r') as file:
        # Read the contents of the file
        file_contents = file.read()

        # Split the contents of the file into a list
        file_contents = file_contents.split('\n')

    # Return the contents of the file
    return file_contents


def SHA1(arr):
    res = []
    for i in arr:
        res.append(hashlib.sha1(i.encode()).hexdigest())
    return res


def SHA256(arr):
    res = []
    for i in arr:
        res.append(hashlib.sha256(i.encode()).hexdigest())
    return res


def MD5(arr):
    res = []
    for i in arr:
        res.append(hashlib.md5(i.encode()).hexdigest())
    return res


def SHA512(arr):
    res = []
    for i in arr:
        res.append(hashlib.sha512(i.encode()).hexdigest())
    return res


def hash_to_password(common_passwords, hashed_passwords, hash, verbose=False):
    for i in range(len(hashed_passwords)):
        if verbose:
            print("Trying password " + str(i+1) + ": " + common_passwords[i])
        if hashed_passwords[i] == hash:
            return common_passwords[i]
    return Fore.RED + "PASSWORD NOT IN DATABASE" + Fore.RESET


def crack(hash, file_name, use_salts=False, mode="SHA1", verbose=False):
    common_passwords = read_file(file_name)
    hashed_passwords = []
    if use_salts:
        # load known salts into a list
        salts = read_file("known-salts.txt")

        passwords_with_salts = []
        new_passwords = []

        # Check if the hash matches any of the common passwords
        for salt in salts:
            for password in common_passwords:

                passwords_with_salts.append(password+salt)
                passwords_with_salts.append(salt+password)

                new_passwords.append(password)
                new_passwords.append(password)

        # Calculate the SHA-1 hash of the password+salt
        if mode == "SHA1":
            hashed_passwords = SHA1(passwords_with_salts)
        elif mode == "SHA256":
            hashed_passwords = SHA256(passwords_with_salts)
        elif mode == "SHA512":
            hashed_passwords = SHA512(passwords_with_salts)
        elif mode == "MD5":
            hashed_passwords = MD5(passwords_with_salts)
        return Fore.GREEN + "Password found: " + hash_to_password(new_passwords, hashed_passwords, hash, verbose) + Fore.RESET
    else:
        if mode == "SHA1":
            hashed_passwords = SHA1(common_passwords)
        elif mode == "SHA256":
            hashed_passwords = SHA256(common_passwords)
        elif mode == "SHA512":
            hashed_passwords = SHA512(common_passwords)
        elif mode == "MD5":
            hashed_passwords = MD5(common_passwords)
        return Fore.GREEN + "Password found: " + hash_to_password(common_passwords, hashed_passwords, hash, verbose) + Fore.RESET


def main():
    parser = argparse.ArgumentParser(description="Hash Cracker")

    # add a positional argument for the path to the wordlist
    parser.add_argument(
        "wordlist", help="path to the wordlist to use for cracking the hash")

    # add a positional argument for the hash to crack
    parser.add_argument("hash", help="the hash to crack")

    # add an optional argument for the cracking mode (default to "fast")
    parser.add_argument("-m", "--mode", default="SHA1",
                        choices=["SHA1", "SHA256", "SHA512", "MD5"], help="cracking algorithm to use")

    # add an optional flag to enable verbose output
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="enable verbose output")

    # add an optional flag to enable salted cracking
    parser.add_argument("-s", "--salt", action="store_true",
                        help="enable salted cracking")

    # parse the arguments
    args = parser.parse_args()

    # extract the arguments
    wordlist = args.wordlist
    hash_to_crack = args.hash
    mode = args.mode
    verbose = args.verbose
    use_salts = args.salt

    result = crack(hash_to_crack, wordlist, use_salts=use_salts,
                   mode=mode, verbose=verbose)

    # print the arguments to the terminal
    print(Fore.YELLOW + "Wordlist:", wordlist + Fore.RESET)
    print(Fore.YELLOW + "Hash to crack:", hash_to_crack + Fore.RESET)
    print(Fore.CYAN + "Mode:", mode + Fore.RESET)
    print(Fore.CYAN + "Verbose:", str(verbose) + Fore.RESET)
    print(result)


if __name__ == '__main__':
    main()
