# Password Generator

A Lightweight and easy-to-use CLI Password Generator. This open-source password generator provides a simple yet powerful command-line interface for generating strong and cryptographically randomised passwords for computer running Windows, Linux or macOS. With it's focus on performance, security, and usability, this password generator enables anyone to conveniently and quickly create strong passwords whether or not they use a password manager.

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

- Performs amny times faster than GUI-based alternatives

- Native-OS executable file avaliable for Windows, Linux and macOS

- User can specify password length

- Uses Python's `secret` module for cryptographically secure password generation

- Does not require admin privileges

- Automatically logs generated passwords into a text file

- Generates symmetric cryptographic key to encrypt and decrypt text file

- Opens text file using the operating system's default text editor

- Clears the text file

- Runs offline and makes no outgoing or incoming network connections

- Executable is only 8 MB in size

- Uses an average of 20 MB of RAM (and only for a second) when generating passwords with a character length less than or equal to 16

- Source code contains plenty of docstrings, is easily readable and editable

## Minimum System Requirements

**NOTE:** Generating passwords with a character length of 16 or less will be instantaneous or take only a few seconds, consuming an average of 15 to 20 MB of RAM. However, generating passwords exceeding 16 characters may take over a minute and utilise more than 100 MB of RAM, though this largely depends on your computer's specifications. For instance, testing on the M1 chip (on macOS) demonstrated that passwords with character lengths as long as 99999 could be generated in under a second.

**Processor (CPU):** Intel Core Solo

**Windows Operating System:** Microsoft Windows XP

**macOS Operating System:** Mac OS X

**Linux Operating System:** Ubuntu Oneiric Ocelot

**Memory:** 500 MB RAM

**Storage:** 1 GB (or 8 MB excl. neccessary OS files)

## Dependencies

- [Python](https://www.python.org/) - high-level, general-purpose programming language.
- [`cryptography`](https://cryptography.io/en/latest/) -  package which provides cryptographic recipes and primitives to Python developers.

## Getting Started

Use the package manager `pip3` to install `cryptography`:
```sh
sudo pip3 install cryptography
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

- The script stores generated passwords into a text file named `password list.txt`, while the cryptographic key is saved as `password list key.key`. Both files are located in the same directory as the script. It's essential not to rename either file and always keep them in the script's directory.

- Behavior when opening the text file differs across operating systems. On MacOS and Linux, the text file can remain open while the script is running, but it's recommended to manually close it before continuing to use the `password-generator`. However, on Windows, if 'Notepad' is set as your default text editor, you must close the text file before proceeding with the `password-generator`. Alternatively, using another program or a Windows 10 or 11 application like 'Notepads App' can allow the script to run without requiring the text file to be closed, though it's still advisable to do so before using the `password-generator`.

- To encrypt and decrypt the text file, you need to generate a cryptographic key. This can be achieved using the commands `-g k` or `gen k`. 

Below is a key for the list of in-built commands and arguments that can be used to make the script perform certain actions.

### Commands/Arguments Key

| Command/Arugment | Input Type | Parse Outcome |
| ----------------- | ---------- | ----------- |
| -g p, -gen p |	string | Generates password. |
| -g k, -gen k |	string | Generates cryptographic key. |
| -w t, -wipe t |	string | Wipes text file. |
| -w k, -wipe k |	string | Wipes cryptographic key. |
| o |	string | Opens text file. |
| e |	string | Encrypts text file. |
| d |	string | Decrypts text file. |
| h, help |	string | Lists all in-built commands and arguments. |
| exit |	string | Exits script. |

## Contributing

Pull requests are welcomed. For major changes, please open an issue first to discuss what you would like to change.

## Contact

Shubham Sharma - [My LinkedIn](https://www.linkedin.com/in/sharma-it/) - shubhamsharma.emails@gmail.com.

## License

This project is licensed under the GPL 3.0 License - see the [LICENSE](LICENSE) file for details.
