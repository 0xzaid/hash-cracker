import hashlib


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


def hash_to_password(common_passwords, hashed_passwords, hash):
    for i in range(len(hashed_passwords)):
        if hashed_passwords[i] == hash:
            return common_passwords[i]
    return "PASSWORD NOT IN DATABASE"


def crack_sha1_hash(hash, use_salts=False):
    common_passwords = read_file("top-10000-passwords.txt")
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
        hashed_passwords = SHA1(passwords_with_salts)
        return hash_to_password(new_passwords, hashed_passwords, hash)
    else:
        hashed_passwords = SHA1(common_passwords)
        return hash_to_password(common_passwords, hashed_passwords, hash)


def main():
    pw = crack_sha1_hash(
        "53d8b3dc9d39f0184144674e310185e41a87ffd5", use_salts=True)
    print(pw)


if __name__ == '__main__':
    main()
