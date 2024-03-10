''' Insert heading comments here.'''
import math, string

# Define constants for punctuation and alphanumeric characters
#  string.punctuation is a string constant that contains all the punctuation characters on the keyboard.
#  except space is not included in this string
PUNCTUATION = string.punctuation

#  string.ascii_lowercase is a string constant that contains all the lowercase letters in the alphabet.
#  string.digits is a string constant that contains all the digits 0-9.
ALPHA_NUM = string.ascii_lowercase + string.digits


BANNER = ''' Welcome to the world of 'dumbcrypt,' where cryptography meets comedy! 
    We're combining Affine Cipher with Caesar Cipher to create a code 
    so 'dumb,' it's brilliant. 
    Remember, in 'dumbcrypt,' spaces are as rare as a unicorn wearing a top hat! 
    Let's dive into this cryptographic comedy adventure!             
    '''


def print_banner(message):
    '''Display the message as a banner.
    It formats the message inside a border of asterisks, creating the banner effect.'''
    border = '*' * 50
    print(border)
    print(f'* {message} *')
    print(border)
    print()

def multiplicative_inverse(A, M):
    '''Return the multiplicative inverse for A given M.
       Find it by trying possibilities until one is found.
        Args:
        A (int): The number for which the inverse is to be found.
        M (int): The modulo value.
        Returns:
            int: The multiplicative inverse of A modulo M.
    '''
    # Find the inverse of A for decrypting purposes
    for x in range(1, M):
        if (A * x) % M == 1:
            return x


def check_co_prime(num, M):
    # Find the greatest common denominator
    return math.gcd(num, M) == 1


def get_smallest_co_prime(M):
    # Calculate the smallest co prime number besides 1
    smallest_co = 2
    for i in range(2, M):
        if check_co_prime(i, M):
            return smallest_co

        smallest_co += 1


def caesar_cipher_encryption(ch, N, alphabet):
    # Find the index of the character and calculate the decryption character
    # (punctuation)
    if ch in alphabet:
        index = int(alphabet.index(ch))
        caesar_encrypt_calculation = (index + N) % len(alphabet)
        return alphabet[caesar_encrypt_calculation]


def caesar_cipher_decryption(ch, N, alphabet):
    # Find the index of the character and calculate the decryption character
    # (punctuation)
    if ch in alphabet:
        index = alphabet.index(ch)
        caesar_decrypt_calculation = (index - N) % len(alphabet)
        return alphabet[caesar_decrypt_calculation]


def affine_cipher_encryption(ch, N, alphabet):
    # Find the A value key
    A = get_smallest_co_prime(len(alphabet))

    # Find the index of the character and calculate the encryption character
    # (num or let)
    if ch in alphabet:
        index = alphabet.index(ch)
        affine_encrypt_calculation = (A * index + N) % len(alphabet)
        return alphabet[affine_encrypt_calculation]


def affine_cipher_decryption(ch, N, alphabet):
    # Find the A value key and the inverse key
    A = get_smallest_co_prime(len(alphabet))
    A1 = multiplicative_inverse(A, len(alphabet))

    # Find the index of the character and calculate the decryption character
    # (num or let)
    if ch in alphabet:
        index = (alphabet.index(ch))
        affine_decrypt_calculation = (A1 * (index - N)) % len(alphabet)
        return alphabet[affine_decrypt_calculation]



def main():
    print_banner(BANNER)

    # Set a variable to enter while loop
    user_command = ''

    # Prompt user for an integer (N)
    user_rotation = input("Input a rotation (int): ")
    user_rotation_check = user_rotation.isdigit()

    # If user did not enter an integer have them try again
    while user_rotation_check is False:
        print("\nError; rotation must be an integer.")
        user_rotation = input("Input a rotation (int): ")
        user_rotation_check = user_rotation.isdigit()

    # Make the rotation an integer instead of a string
    user_rotation = int(user_rotation)

    # Create while loop to allow the user to enter multiple commands
    while user_command != 'q':
        # Set a variable for the encryption text
        cipher_text = ''
        decode_text = ''

        # Prompt user for a command process
        user_command = input("\n\nInput a command (e)ncrypt, (d)ecrypt, (q)uit: ")
        user_command = user_command.lower()

        # Exit code if user wishes to do so
        if user_command == 'q':
            break

        # If the command is invalid re-prompt the user for a new selection
        elif user_command != 'e' and user_command != 'd':
            print("\nCommand not recognized.")
            user_command = input("\n\nInput a command (e)ncrypt, (d)ecrypt, (q)uit: ")
            user_command = user_command.lower()

        # Prompt user for a string
        # If the user selected 'e' change the input statement to 'Encrypt'
        if user_command == 'e':
            user_string_original = input("\nInput a string to encrypt: ")
            user_string = user_string_original.lower()

        # If the user selected 'd' change the input statement to 'Decrypt'
        elif user_command == 'd':
            user_string_original = input("\nInput a string to decrypt: ")
            user_string = user_string_original.lower()

        user_string_checker = user_string.find(' ')

        # If the string contains a space ask the user for a command and string again
        if user_string_checker != -1:
            print("\nError with character:")
            print("Cannot encrypt this string.")
            continue


        # Decide if the String is Affine or Cipher code
        # User selected Encrypt
        if user_command == 'e':
            for ch in user_string:
                if ch.isalnum():
                    alphabet = ALPHA_NUM
                    cipher_text += affine_cipher_encryption(ch, user_rotation, alphabet)

                else:
                    alphabet = PUNCTUATION
                    cipher_text += caesar_cipher_encryption(ch, user_rotation, alphabet)

            # Print the output of the Encryption code
            print(f"\nPlain text: {user_string_original}")
            print(f"\nCipher text: {cipher_text}")

        # User selected Decrypt
        elif user_command == 'd':
            for ch in user_string:
                if ch.isalnum():
                    alphabet = ALPHA_NUM
                    decode_text += affine_cipher_decryption(ch, user_rotation, alphabet)

                else:
                    alphabet = PUNCTUATION
                    decode_text += caesar_cipher_decryption(ch, user_rotation, alphabet)

            # Print the output of the Decryption code
            print(f"\nCipher text: {user_string_original}")
            print(f"\nPlain text: {decode_text}")

    pass  # delete and replace with your code




# These two lines allow this program to be imported into other codes
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
# DO NOT CHANGE THESE 2 lines or Do NOT add code to them. Everything
# you add should be in the 'main' function above.
if __name__ == '__main__':
    main()



