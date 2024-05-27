import os
import sys
import string
import secrets
import platform
import subprocess
import logging
import logging.config
from logging import getLogger
from logging.config import dictConfig
from cryptography.fernet import Fernet

# Resizes console window for Windows operating systems

CONSOLE_WIDTH = 143
CONSOLE_HEIGHT = 20

os.system(f'mode {CONSOLE_WIDTH},{CONSOLE_HEIGHT}')

# Resizes console window for Unix operating systems

rows = 16
columns = 140

sys.stdout.write("\x1b[8;{rows};{columns}t".format(rows=rows, columns=columns))

# Ensures that files created by this application are created in the file path of the application
os.path.realpath(os.path.join(os.path.dirname(__file__)))

# Set up logging
logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(levelname)s - %(message)s\n\n'
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'password_generator.log',
            'level': 'DEBUG',
            'formatter': 'standard'
        }
    },
    'root': {
        'handlers': ['file'],
        'level': 'DEBUG'
    }
}
dictConfig(logging_config)

current_os = platform.system()
get_cwd = (os.getcwd())

NORMAL = '\033[0m'
BOLD = '\033[1m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'

VERSION = '1.2.0'
BANNER = f'''
 ______  _____  _______ _______ _  _  _  _____   ______  _____       ______  ______ __   _  ______  ______  _____  _______  _____   ______
|_____] |_____| |_____  |_____  |  |  | |     | |_____/ |     \     |  ____ |______ | \  | |______ |_____/ |_____|    |    |     | |_____/
|       |     | ______| ______| |__|__| |_____| |    \_ |_____/     |_____| |______ |  \_| |______ |    \_ |     |    |    |_____| |    \_
'''

HELP_TEXT = '''
[>] -g [p/k], --gen [p/k]  : generate password/symmetric-cryptographic-key
    -c [t/k], --clear [t/k] : clear text file/symmetric-cryptographic-key
    o                      : open text file
    e                      : encrypt text file
    d                      : decrypt text file
    exit                   : exit application
    h, help                : show list of in-built commands and necessary arguments'''

class FileHelper:
    """
    A class that provides file-related helper functions.

    Args:
        config (dict): A dictionary containing the configuration settings.

    Attributes:
        config (dict): A dictionary containing the configuration settings.

    Methods:
        file_exists(filename): Checks if a file exists.
        remove_file(filename): Removes a file.
        write_to_file(filename, content): Writes content to a file.
        read_from_file(filename): Reads content from a file.
    """
    def __init__(self, config):
        self.config = config

    def file_exists(self, filename):
        """
        Checks if a file exists.

        Args:
            filename (str): The name of the file.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        return os.path.exists(filename)

    def remove_file(self, filename):
        """
        Removes a file.

        Args:
            filename (str): The name of the file.
        """
        os.remove(filename)

    def write_to_file(self, filename, content):
        """
        Writes content to a file.

        Args:
            filename (str): The name of the file.
            content (str): The content to be written to the file.
        """
        with open(filename, 'a') as file:
            file.write(content)

    def read_from_file(self, filename):
        """
        Reads content from a file.

        Args:
            filename (str): The name of the file.

        Returns:
            str: The content read from the file.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        if not self.file_exists(filename):
            raise FileNotFoundError(f"File '{filename}' does not exist.")
        with open(filename, 'rb') as file:
            return file.read()

class Console:
    """
    A class that handles the console interface and user input.

    Args:
        file_helper (FileHelper): An instance of the FileHelper class.
        config (dict): A dictionary containing the configuration settings.

    Attributes:
        file_helper (FileHelper): An instance of the FileHelper class.
        config (dict): A dictionary containing the configuration settings.
        show_banner (bool): Indicates whether to display the banner.

    Methods:
        display_banner(): Displays the application banner.
        run(): Runs the console interface.
        get_input(): Gets user input from the console.
        generate_password(): Generates a random password.
        generate_key(): Generates a symmetric cryptographic key.
        clear_key(): Clears the symmetric cryptographic key.
        clear_text_file(): Clears the text file.
        open_text_file(): Opens the text file.
        encrypt_text_file(): Encrypts the text file.
        decrypt_text_file(): Decrypts the text file.
        commands_and_arguments(): Displays a list of in-built commands and necessary arguments.
    """
    def __init__(self, file_helper, config):
        self.file_helper = file_helper
        self.config = config
        self.show_banner = True
        self.display_banner()

    def display_banner(self):
        """
        Displays the application banner.
        
        Description:
            This method prints the application banner to the console if the 'show_banner'
            attribute is set to True. The banner includes information about the creator (Shubham Sharma),
            version, and a message to view a list of in-built commands and necessary arguments.
        """
        if self.show_banner:
            print(
                f'{BANNER}\n[>] Created by : Shubham Sharma'
                + f'\n[>] Version    : {VERSION}'
                + BOLD
                + "\n\n[>] Input 'h' or 'help' to view a list of in-built commands and necessary arguments"
            )
            self.show_banner = False

    def run(self):
        """
        Runs the console interface.

        Description:
            This method continuously prompts the user for input, processes the input,
            and handles any exceptions that may occur during the process. It runs in an
            infinite loop until the user chooses to exit the application.        
        """
        while True:
            user_input = self.get_input()
            try:
                self.process_user_input(user_input)
            except (ValueError, FileNotFoundError) as e:
                print(BOLD + RED + f"\n[x] ERROR: {str(e)}" + NORMAL)
                logging.error(str(e))
            except Exception as e:
                print(BOLD + RED + f"\n[x] ERROR: An unexpected error occurred" + NORMAL)
                logging.exception("Unhandled exception occurred")

    def get_input(self):
        """
        Gets user input from the console.

        Returns:
            str: The user input.
            
        Description:
            This method prompts the user for input and returns the input as a string.
        """
        return input(NORMAL + '\n' + get_cwd + '> ')

    def process_user_input(self, user_input):
        """
        Processes the user input.

        Args:
            user_input (str): The user input.

        Raises:
            ValueError: If the user input is invalid.
            
        Description:
            This method takes the user input and performs the corresponding action based
            on the input. It calls the appropriate methods to generate a password, generate
            a key, clear the text file, open the text file, encrypt the text file, decrypt
            the text file, display the list of commands and arguments, or exit the application.
            If the user input is not recognised, it raises a ValueError.
        """
        if user_input in ['-g p', '--gen p']:
            self.generate_password()
        elif user_input in ['-g k', '--gen k']:
            self.generate_key()
        elif user_input in ['-c t', '--clear t']:
            self.clear_text_file()
        elif user_input in ['-c k', '--clear k']:
            self.clear_key()
        elif user_input == 'o':
            self.open_text_file()
        elif user_input == 'e':
            self.encrypt_text_file()
        elif user_input == 'd':
            self.decrypt_text_file()
        elif user_input in ['h', 'help']:
            self.commands_and_arguments()
        elif user_input == 'exit':
            print(BOLD + GREEN + "\n[+] Exiting application...\n")
            raise SystemExit()
        else:
            logging.error(f"'{user_input}' is not recognised as a command or an argument")
            raise ValueError(f"'{user_input}' is not recognised as a command or an argument")
            

    def generate_password(self):
        """
        Generates a random password.
        
        Description:
            This method prompts the user to enter the desired length of the password.
            It generates a random password of the specified length using a combination
            of letters, digits, and punctuation. The generated password is then written
            to the passwords text file specified in the configuration. If the user cancels
            the password generation, the method returns without generating a password.
        """
        while True:
            try:
                user_input_length = input(BOLD + "\n[>] Enter the number of characters for the length of the password (min. 8), or enter 'cancel' to cancel: " + NORMAL)
                if user_input_length.lower() == 'cancel':
                    print(BOLD + YELLOW + '\n[-] MSG: Password generation canceled' + NORMAL)
                    return
                user_input_length = int(user_input_length)
                if user_input_length < 8:
                    print(BOLD + RED + '\n[x] ERROR: Invalid password length. Please enter a number larger than or equal to 8' + NORMAL)
                    continue
            except ValueError:
                logging.error(
                    f"'{user_input_length}' is not a valid numerical value. Please input a valid numerical value"
                )
                print(BOLD + RED + '\n[-] ERROR: ' + "'" + user_input_length + "'" + ' is not a valid numerical value. Please input a valid numerical value' + NORMAL)
                continue
            else:
                password_set = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(secrets.choice(password_set) for _ in range(user_input_length))
                self.file_helper.write_to_file(self.config['passwords_file'], password + '\n\n')
                print(BOLD + GREEN + '\n[+] Password has been generated successfully')
                return

    def generate_key(self):
        """
        Generates a symmetric cryptographic key.
        
        Description:
            This method generates a symmetric cryptographic key using the Fernet library.
            If the key file specified in the configuration already exists, it raises a ValueError.
            Otherwise, it generates a new key, writes it to the key file, and prints a success message.
        """
        if self.file_helper.file_exists(self.config['key_file']):
            logging.error("Key already exists")
            raise ValueError("Key already exists")
        else:
            key = Fernet.generate_key()
            key_str = key.decode()  # Convert bytes to string
            self.file_helper.write_to_file(self.config['key_file'], key_str)
            print(BOLD + GREEN + "\n[+] Symmetric cryptographic key has successfully been created")

    def clear_key(self):
        """
        Deletes the symmetric cryptographic key.
        
        Description:
            This method deletes the symmetric cryptographic key file specified in the configuration.
            If the key file does not exist, it raises a ValueError. Otherwise, it deletes the file
            and prints a success message.
        """
        if self.file_helper.file_exists(self.config['key_file']):
            self.file_helper.remove_file(self.config['key_file'])
            print(BOLD + GREEN + '\n[+] Key has successfully been cleared')
        else:
            logging.error("Cryptographic key does not exist")
            raise ValueError("Cryptographic key does not exist")

    def clear_text_file(self):
        """
        clears the text file.
        
        Description:
            This method deletes the text file specified in the configuration.
            If the text file does not exist, it raises a ValueError. Otherwise,
            it deletes the file and prints a success message.
        """
        if self.file_helper.file_exists(self.config['passwords_file']):
            self.file_helper.remove_file(self.config['passwords_file'])
            print(BOLD + GREEN + "\n[+] Text file has successfully been cleared")
        else:
            logging.error("Text file does not exist")
            raise ValueError("Text file does not exist")

    def open_text_file(self):
        """
        Opens the text file.
        
        Description:
            This method opens the text file specified in the configuration using the
            appropriate command based on the operating system. If the text file does
            not exist, it raises a ValueError. After opening the file, it prints a
            success message with instructions to close the file to continue using
            the Password Generator.
        """
        if self.file_helper.file_exists(self.config['passwords_file']):
            if current_os == "Windows":
                subprocess.call(["start", self.config['passwords_file']], shell=True)
                print(
                    BOLD + GREEN +
                    "\n[+] Text file successfully opened" +
                    NORMAL + BOLD +
                    '\n\n[>] Close the Notepad window or the text editor you are using to continue using the Password Generator')
            elif current_os == "Darwin":
                subprocess.call(["open", self.config['passwords_file']])
                print(
                    BOLD + GREEN +
                    "\n[+] Text file successfully opened" +
                    NORMAL + BOLD +
                    '\n\n[>] Close the window of TextEdit or the text editor you are using to continue using the Password Generator')
            elif current_os == "Linux":
                subprocess.call(["xdg-open", self.config['passwords_file']])
                print(
                    BOLD + GREEN +
                    "\n[+] Text file successfully opened" +
                    NORMAL + BOLD +
                    '\n\n[>] Close the window of Gedit or the text editor you are using to continue using the Password Generator')
        else:
            logging.error("Text file does not exist")
            raise ValueError("Text file does not exist")

    def encrypt_text_file(self):
        """
        Encrypts the text file.
        
        Description:
            This method encrypts the text file specified in the configuration using
            the symmetric cryptographic key. If the key or text file is missing, it
            raises a ValueError. After encryption, it calls the 'write_encrypted_text_file'
            method to write the encrypted content to the text file and print a success message.
        """
        if self.file_helper.file_exists(self.config['key_file']) and self.file_helper.file_exists(self.config['passwords_file']):
            key = self.file_helper.read_from_file(self.config['key_file'])
            if len(key) != 44:
                logging.error("Invalid encryption key size. The key must be 44 bytes.")
                raise ValueError("Invalid encryption key size. The key must be 44 bytes.")
            fernet = Fernet(key)
            original_text_file = self.file_helper.read_from_file(self.config['passwords_file'])
            original_text_file_bytes = original_text_file # Remove the encode() method call
            encrypted = fernet.encrypt(original_text_file_bytes)
            self.write_encrypted_text_file(
                encrypted, '\n[+] Text file has successfully been encrypted'
            )
        else:
            logging.error("Key and/or text file is missing")
            raise ValueError("Key and/or text file is missing")

    def decrypt_text_file(self):
        """
        Decrypts the text file.
        
        Description:
            This method decrypts the text file specified in the configuration using
            the symmetric cryptographic key. If the key or text file is missing, it
            raises a ValueError. After decryption, it calls the 'write_encrypted_text_file'
            method to write the decrypted content to the text file and print a success message.
        """
        if self.file_helper.file_exists(self.config['key_file']) and self.file_helper.file_exists(self.config['passwords_file']):
            key = self.file_helper.read_from_file(self.config['key_file'])
            if len(key) != 44:
                logging.error("Invalid encryption key size. The key must be 44 bytes.")
                raise ValueError("Invalid encryption key size. The key must be 44 bytes.")
            fernet = Fernet(key)
            encrypted = self.file_helper.read_from_file(self.config['passwords_file'])
            decrypted = fernet.decrypt(encrypted)
            self.write_encrypted_text_file(
                decrypted, '\n[+] Text file has been successfully decrypted'
            )
        else:
            logging.error("Key and/or text file is missing")
            raise ValueError("Key and/or text file is missing")

    def write_encrypted_text_file(self, arg0, arg1):
        """
        Writes the encrypted content to the text file and prints a success message.

        Description:
            This method takes the encrypted content as a byte string and writes it to the text file specified in the
            configuration. It then prints a success message to indicate that the text file has been successfully encrypted
            or decrypted.
        """
        encrypted_str = arg0.decode()
        with open(self.config['passwords_file'], 'w') as file:
            file.write(encrypted_str)
        print(BOLD + GREEN + arg1)

    def commands_and_arguments(self):
        """
        Displays a list of in-built commands and necessary arguments.
        
        Description:
            This method prints a list of in-built commands and their necessary arguments
            to the console. It provides users with information on how to use the application
            and its various functionalities.
        """
        print(BOLD + HELP_TEXT)

class Main:
    """
    The main class that initialises the application.

    Methods:
        validate_config(): Validates the configuration settings.
        run(): Runs the application.
    """
    def __init__(self):
        self.config = {
            'passwords_file': 'passwords.txt',
            'key_file': 'passwords.key'
        }
        self.validate_config()
        self.file_helper = FileHelper(self.config)
        self.console = Console(self.file_helper, self.config)

    def validate_config(self):
        """
        Validates the configuration settings.

        Raises:
            ValueError: If any configuration value is not a string.
        """
        for key, value in self.config.items():
            if not isinstance(value, str):
                logging.error(f"Invalid value '{value}' for config key '{key}'. Must be a string.")
                raise ValueError(f"Invalid value '{value}' for config key '{key}'. Must be a string.")

    def run(self):
        """
        Runs the application.
        
        Description:
            This method runs the application by calling the `run()` method of the `console`
            object. It handles any exceptions that may occur during the execution and logs
            them using the `logger` object.
        """
        try:
            self.console.run()
        except Exception as e:
            logger = getLogger(__name__)
            logger.exception("Unhandled exception occurred")

if __name__ == "__main__":
    app = Main()
    app.run()
