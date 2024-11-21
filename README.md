# Password Generator

Lightweight and easy-to-use CLI Password Generator. This password generator provides a simple yet powerful command-line interface for generating strong and cryptographically randomised passwords for Windows and Linux operating systems. With it's focus on performance, security, and usability, this password generator enables anyone to conveniently and quickly create strong passwords whether or not they use a password manager.

# Table of Contents

1. [Features](#features)
2. [Minimum System Requirements](#minimum-system-requirements)
3. [Getting Started](#getting-started)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [Contact](#contact)
7. [License](#license)

## Features

- Lightweight and user-friendly CLI
- Performs many times faster than GUI-based alternatives
- Native-OS executable file available for Windows, Linux and macOS
- Configurable password length (8-64 characters)
- Password strength checking using zxcvbn
- Uses Python's `secrets` module for cryptographically secure password generation
- Does not require admin privileges
- Automatically logs generated passwords into a text file
- Generates symmetric cryptographic key to encrypt and decrypt text file
- Opens text file using the operating system's default text editor
- Secure key storage using system keyring
- Configurable via JSON configuration file
- Wipe stored passwords or encryption keys
- Runs offline and makes no outgoing or incoming network connections
- Executable is only 8 MB in size
- Uses an average of 20 MB of RAM (and only for a second) when generating passwords
- Source code contains plenty of docstrings, is easily readable and editable

## Minimum System Requirements

**NOTE:** Generating passwords with a character length of 16 or less will be instantaneous or take only a few seconds, consuming an average of 15 to 20 MB of RAM. However, generating passwords exceeding 16 characters may take over a minute and utilise more than 100 MB of RAM, though this largely depends on your computer's specifications. For instance, testing on the M1 chip (on macOS) demonstrated that passwords with character lengths as long as 99999 could be generated in under a second.

- **Processor (CPU):** Intel Core Solo
- **Windows Operating System:** Microsoft Windows XP
- **macOS Operating System:** Mac OS X
- **Linux Operating System:** Ubuntu Oneiric Ocelot
- **Memory:** 500 MB RAM
- **Storage:** 1 GB (or 8 MB excl. neccessary OS files)

## Dependencies

- [Python](https://www.python.org/) - high-level, general-purpose programming language.
- [`cryptography`](https://cryptography.io/en/latest/) -  package which provides cryptographic recipes and primitives to Python developers.
- [`keyring`](https://pypi.org/project/keyring/) - cross-platform library for secure password and key storage
- [`zxcvbn`](https://pypi.org/project/zxcvbn/) - realistic password strength estimation

## Getting Started

Use the package manager `pip3` to install the required dependencies:
```sh
pip3 install cryptography keyring zxcvbn
```
To clone this repository:
```sh
git clone https://github.com/sharma-it/password-generator.git
```
To change into this repository's directory:
```sh
cd password-generator
```
To run the script:
```sh
python password-generator.py
```

## Usage Information

The application uses a configuration file (`config.json`) to store settings like:
- Password file location
- Minimum and maximum password length (default: 8-64 characters)
- Minimum required password strength (0-4, default: 3)
- Key storage name

The script stores generated passwords into a text file named `passwords.txt`. The encryption key is securely stored in your system's keyring. Both the password file and configuration are located in the same directory as the script.

### Command-Line Arguments

| Argument | Description |
| -------- | ----------- |
| -g p, --generate p | Generate a new password |
| -g k, --generate k | Generate new encryption key |
| -w t, --wipe t | Wipe the passwords file |
| -w k, --wipe k | Wipe the stored encryption key |
| -o, --open | Open the passwords file |
| -e, --encrypt | Encrypt the passwords file |
| -d, --decrypt | Decrypt the passwords file |
| -h, --help | Show help message |

## Contributing

Pull requests are welcomed. For major changes, please open an issue first to discuss what you would like to change.

## Contact

Shubham Sharma - [My LinkedIn](https://www.linkedin.com/in/sharma-it/) - shubhamsharma.emails@gmail.com.

## License

This project is licensed under the GPL 3.0 License - see the [LICENSE](LICENSE) file for details.
