import os
import sys
import string
import secrets
import platform
import subprocess
import logging
import logging.config
import argparse
import json
from typing import List, Optional
from logging import getLogger
from logging.config import dictConfig
from cryptography.fernet import Fernet
from pathlib import Path
import keyring
from zxcvbn import zxcvbn

# Constants
VERSION = '1.3.0'

# ANSI color codes
NORMAL = '\033[0m'
BOLD = '\033[1m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'

# Banner
BANNER = f'''
 _____   _____  ______  ______  _  _  _  _____   ______  _____       ______  ______ __   _  ______  ______  _____  _______  _____   ______
|_____] |_____| |_____  |_____  |  |  | |     | |_____/ |     \     |  ____ |______ | \  | |______ |_____/ |_____|    |    |     | |_____/
|       |     | ______| ______| |__|__| |_____| |    \_ |_____/     |_____| |______ |  \_| |______ |    \_ |     |    |    |_____| |    \_
'''

def get_banner_dimensions() -> tuple[int, int]:
    """Calculate the width and height of the banner."""
    lines = BANNER.split('\n')
    width = max(len(line) for line in lines)
    height = len(lines)
    return width, height

def resize_terminal():
    """Resize the terminal window to fit the banner."""
    width, height = get_banner_dimensions()
    
    # Add some padding
    width += 4  # Add 2 characters of padding on each side
    height += 4  # Add some vertical space for commands
    
    if platform.system() == "Darwin":  # macOS
        cmd = f"printf '\\e[8;{height};{width}t'"
        os.system(cmd)
    elif platform.system() == "Linux":
        cmd = f"printf '\\e[8;{height};{width}t'"
        os.system(cmd)
    elif platform.system() == "Windows":
        cmd = f"mode con: cols={width} lines={height}"
        os.system(cmd)

class Config:
    def __init__(self, config_file: str = 'config.json'):
        self.config_file = config_file
        self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            self.config = {
                'passwords_file': 'passwords.txt',
                'key_name': 'password_generator_key',
                'min_password_length': 8,
                'min_password_strength': 3
            }
            self.save_config()
        else:
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)

    def save_config(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)

    def __getitem__(self, key):
        return self.config[key]

class PasswordGenerator:
    def __init__(self, config: Config):
        self.config = config

    def generate_password(self, length: int) -> str:
        if length < self.config['min_password_length']:
            raise ValueError(f"Password length must be at least {self.config['min_password_length']} characters.")

        password_set = string.ascii_letters + string.digits + string.punctuation
        while True:
            password = ''.join(secrets.choice(password_set) for _ in range(length))
            if self.check_password_strength(password) >= self.config['min_password_strength']:
                return password

    def generate_passphrase(self, num_words: int) -> str:
        word_list = Path('words.txt').read_text().splitlines()
        return ' '.join(secrets.choice(word_list) for _ in range(num_words))

    def check_password_strength(self, password: str) -> int:
        return zxcvbn(password)['score']

class FileHelper:
    def __init__(self, config: Config):
        self.config = config

    def file_exists(self, filename: str) -> bool:
        return os.path.exists(filename)

    def remove_file(self, filename: str):
        os.remove(filename)

    def write_to_file(self, filename: str, content: str):
        with open(filename, 'a') as file:
            file.write(content)

    def read_from_file(self, filename: str) -> bytes:
        if not self.file_exists(filename):
            raise FileNotFoundError(f"File '{filename}' does not exist.")
        with open(filename, 'rb') as file:
            return file.read()

class Console:
    def __init__(self, file_helper: FileHelper, config: Config, password_generator: PasswordGenerator):
        self.file_helper = file_helper
        self.config = config
        self.password_generator = password_generator
        self.show_banner = True

    def display_banner(self):
        if self.show_banner:
            resize_terminal()
            print(f'{BANNER}\n[>] Created by : Shubham Sharma\n[>] Version    : {VERSION}\n')
            self.show_banner = False

    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-g', '--generate', choices=['p', 'k'], help='Generate password (p) or key (k)')
        parser.add_argument('-w', '--wipe', choices=['t', 'k'], help='Wipe text file (t) or key (k)')
        parser.add_argument('-o', '--open', action='store_true', help='Open text file')
        parser.add_argument('-e', '--encrypt', action='store_true', help='Encrypt text file')
        parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt text file')

        args = parser.parse_args()

        if args.generate:
            self.generate(args.generate)
        elif args.wipe:
            self.wipe(args.wipe)
        elif args.open:
            self.open_text_file()
        elif args.encrypt:
            self.encrypt_text_file()
        elif args.decrypt:
            self.decrypt_text_file()
        else:
            parser.print_help()

    def generate(self, type: str):
        if type == 'p':
            self.generate_password()
        elif type == 'k':
            self.generate_key()

    def wipe(self, type: str):
        if type == 't':
            self.wipe_text_file()
        elif type == 'k':
            self.wipe_key()

    def generate_password(self):
        while True:
            user_input_length = input(BOLD + f"\n[>] Enter the number of characters for the length of the password (min. {self.config['min_password_length']}), or enter 'cancel' to cancel: " + NORMAL)
            if user_input_length.lower() == 'cancel':
                print(BOLD + YELLOW + '\n[-] MSG: Password generation canceled' + NORMAL)
                return
            try:
                user_input_length = int(user_input_length)
                password = self.password_generator.generate_password(user_input_length)
                self.file_helper.write_to_file(self.config['passwords_file'], password + '\n\n')
                print(BOLD + GREEN + '\n[+] Password has been generated successfully')
                return
            except ValueError as e:
                print(BOLD + RED + f'\n[-] ERROR: {str(e)}' + NORMAL)

    def generate_key(self):
        key = Fernet.generate_key()
        keyring.set_password("system", self.config['key_name'], key.decode())
        print(BOLD + GREEN + "\n[+] Symmetric cryptographic key has successfully been created")

    def wipe_key(self):
        try:
            keyring.delete_password("system", self.config['key_name'])
            print(BOLD + GREEN + '\n[+] Key has successfully been wiped')
        except keyring.errors.PasswordDeleteError:
            print(BOLD + RED + '\n[-] ERROR: Cryptographic key does not exist' + NORMAL)

    def wipe_text_file(self):
        if self.file_helper.file_exists(self.config['passwords_file']):
            self.file_helper.remove_file(self.config['passwords_file'])
            print(BOLD + GREEN + "\n[+] Text file has successfully been wiped")
        else:
            print(BOLD + RED + "\n[-] ERROR: Text file does not exist" + NORMAL)

    def open_text_file(self):
        if self.file_helper.file_exists(self.config['passwords_file']):
            if platform.system() == "Windows":
                subprocess.call(["start", self.config['passwords_file']], shell=True)
            elif platform.system() == "Darwin":
                subprocess.call(["open", self.config['passwords_file']])
            elif platform.system() == "Linux":
                subprocess.call(["xdg-open", self.config['passwords_file']])
            print(BOLD + GREEN + "[+] Text file successfully opened\n" + NORMAL + BOLD)
        else:
            print(BOLD + RED + "\n[-] ERROR: Text file does not exist" + NORMAL)

    def encrypt_text_file(self):
        try:
            key = keyring.get_password("system", self.config['key_name'])
            if key is None:
                raise ValueError("Encryption key not found")
            fernet = Fernet(key.encode())
            original_text_file = self.file_helper.read_from_file(self.config['passwords_file'])
            encrypted = fernet.encrypt(original_text_file)
            self.write_encrypted_text_file(encrypted, '\n[+] Text file has successfully been encrypted')
        except (FileNotFoundError, ValueError) as e:
            print(BOLD + RED + f"\n[-] ERROR: {str(e)}" + NORMAL)

    def decrypt_text_file(self):
        try:
            key = keyring.get_password("system", self.config['key_name'])
            if key is None:
                raise ValueError("Decryption key not found")
            fernet = Fernet(key.encode())
            encrypted = self.file_helper.read_from_file(self.config['passwords_file'])
            decrypted = fernet.decrypt(encrypted)
            self.write_encrypted_text_file(decrypted, '\n[+] Text file has been successfully decrypted')
        except (FileNotFoundError, ValueError) as e:
            print(BOLD + RED + f"\n[-] ERROR: {str(e)}" + NORMAL)

    def write_encrypted_text_file(self, content: bytes, message: str):
        with open(self.config['passwords_file'], 'wb') as file:
            file.write(content)
        print(BOLD + GREEN + message)

def setup_logging():
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

def main():
    setup_logging()
    logger = getLogger(__name__)

    try:
        config = Config()
        file_helper = FileHelper(config)
        password_generator = PasswordGenerator(config)
        console = Console(file_helper, config, password_generator)
        console.display_banner()
        console.run()
    except Exception as e:
        logger.exception("Unhandled exception occurred")
        print(BOLD + RED + f"\n[x] ERROR: An unexpected error occurred: {str(e)}" + NORMAL)

if __name__ == "__main__":
    main()
