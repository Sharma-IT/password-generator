import os
import string
import random
from cryptography.fernet import Fernet  # pip3 install cryptography

os.system('mode 143,20') # resiszes console window

__location__ = os.path.realpath(  # ensures that any file that is created is created in the file path of application

    os.path.join(os.path.dirname(__file__)))

get_cwd = (os.getcwd())

version = '1.1.0'

NORM = '\033[0m'
BOLD = '\033[1m'
RED = '\033[91m'
GREEN = '\033[92m'
 

def banner():
    banner_str = ('\n'
                  r' ______  _____  _______ _______ _  _  _  _____   ______  _____       ______  ______ __   _  ______  ______  _____  _______  _____   ______' '\n'
                  r'|_____] |_____| |_____  |_____  |  |  | |     | |_____/ |     \     |  ____ |______ | \  | |______ |_____/ |_____|    |    |     | |_____/' '\n'
                  r'|       |     | ______| ______| |__|__| |_____| |    \_ |_____/     |_____| |______ |  \_| |______ |    \_ |     |    |    |_____| |    \_ ')

    print(
        BOLD
        + banner_str
        + '\n\n[>] Created by : Shubham Sharma'
        + '\n[>] Version    : '
        + version
    )


def generate_password():
    while True:

        try:

            user_input_length = int(input(BOLD + "\n[>] Enter the no. of characters for the length of the password, to cancel process input '0': " + NORM))

            if user_input_length == 0:
                print(BOLD + GREEN + '\n[+] Password generation has successfully been cancelled')
                main()

        except ValueError:

            print(BOLD + RED + '\n[-] ERROR : Non-numeric value inputted' + NORM)

            continue

        else:

            password_set = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.SystemRandom().choice(password_set)
                for _ in range(user_input_length))
            
            with open('password list.txt', 'a') as passwordfile:
                passwordfile.writelines(password + '\n\n')

            print(BOLD + GREEN + '\n[+] Password has been generated successfully')
            main()

        break


def generate_key():  # generates symmetric cryptographic key
    
    if os.path.exists('password list key.key'):
        print(BOLD + RED + "\n[-] ERROR: Key already exists")
            
    else:
        key = Fernet.generate_key()
        with open('password list key.key', 'wb') as filekey:
            filekey.write(key)

        print(BOLD + GREEN + "\n[+] Symmetric cryptographic key has successfully been created")

    main()


def wipe_key():
    
    if os.path.exists("password list key.key"):
        os.remove("password list key.key")
        print(BOLD + GREEN + '\n[+] Key has successfully been wiped')
        
    else:
        print(BOLD + RED + "\n[-] ERROR: Cryptographic key does not exist")

    main()


def wipe_text_file():
    
    if os.path.exists("password list.txt"):
        
        os.remove("password list.txt")
        print(BOLD + GREEN + "\n[+] Text file has successfully been wiped")
        
    else:
        print(BOLD + RED + "\n[-] ERROR: Text file does not exist")

    main()


def open_text_file():
    
    if os.path.exists("password list.txt"):
        
        os.system('"password list.txt"')
        
        print(
            BOLD + GREEN + 
            "\n[+] Text file successfully opened"
            + NORM + BOLD + 
            '\n\n[>] Close Notepad window to continue using Password Generator')
            
    else:
        
        print(BOLD + RED + "\n[-] ERROR: Text file is missing")

    main()


def encrypt_text_file():  # encrypts text file with symmetric cryptographic key
    
    if os.path.exists('password list key.key') and os.path.exists('password list.txt'):
        
        with open('password list key.key', 'rb') as filekey:
            key = filekey.read()  # opens symmetric cryptographic key; checks for an existing key
            
        fernet = Fernet(key)  # creates symmetric cryptographic key

        with open('password list.txt', 'rb') as text_file:  
            original_text_file = text_file.read() # opens to-be-encrypted text file

        encrypted = fernet.encrypt(original_text_file)  # creates encrypted data

        with open('password list.txt','wb') as encrypted_text_file:  
            encrypted_text_file.write(encrypted) # opens text file in write only mode and replaces original data with encrypted data

        print(BOLD + GREEN + '\n[+] Text file has successfully been encrypted')
            
    else:
        print(BOLD + RED + '\n[-] ERROR: Key and/or text file is missing')
        
    main()


def decrypt_text_file():  # decrypts text file with symmetric cryptographic key
    
    if os.path.exists('password list key.key') and os.path.exists('password list.txt'):
        
        with open('password list key.key', 'rb') as filekey:
                key = filekey.read()  # opens symmetric cryptographic key; checks for an existing key

        fernet = Fernet(key)  # creates symmetric cryptographic key

        with open('password list.txt', 'rb') as enc_text_file: 
            encrypted = enc_text_file.read()  # opens encrypted text file using generated key

        decrypted = fernet.decrypt(encrypted)  # decrypts text file

        with open('password list.txt', 'wb') as dec_text_file: 
            dec_text_file.write(decrypted)  # opens text file in write only mode and replaces encrypted data with decrypted data

        print(BOLD + GREEN + '\n [+] Text file has been successfully decrypted')
        
    else:
        print(BOLD + RED + '\n[-] ERROR: Key and/or text file is missing')
            
    main()


def commands_and_arguments():
    
    print(
        BOLD +
        '\n[>] h, help : shows this list of in-built commands and necessary arguments'
        '\n    -g [p/k], --gen [p/k] : generate password/symmetric cryptographic key'
        '\n    -w [t/k], --wipe [t/k] : wipe text file/symmetric cryptographic key'
        '\n    o : open text file'
        '\n    e : encrypt text file'
        '\n    d : decrypt text file'
        '\n    exit : exit application')
    
    main()


def main():
    
    user_prompt = input(NORM + '\n' + get_cwd + '> ')

    if user_prompt in ['-g p', "--gen p"]:
        generate_password()
    if user_prompt in ['-g k', "--gen k"]:
        generate_key()
    if user_prompt in ['-w t', "--wipe t"]:
        wipe_text_file()
    if user_prompt in ['-w k', "--wipe k"]:
        wipe_key()
    if user_prompt == 'o':
        open_text_file()
    if user_prompt == 'exit':
        raise SystemExit()  # exits the application
    if user_prompt == 'e':
        encrypt_text_file()
    if user_prompt == 'd':
        decrypt_text_file()
    if user_prompt in ['h', 'help']:
        commands_and_arguments()
    else:

        print(
            BOLD + RED +
            "\n[-] ERROR : '" + user_prompt + "' is not recognised as a command or an argument"
            + NORM + BOLD +
            "\n\n[>] Use 'h' or 'help' for a list of in-built commands and necessary arguments")
        main()


banner()
main()
