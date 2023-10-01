# Password Generator

A Lightweight and easy-to-use CLI Password Generator. This open-source password generator provides a simple yet powerful command-line interface for generating strong and cryptographically randomised passwords for PCs running Windows, Linux and/or macOS. With its focus on performance, security, and usability, this password generator enables anyone to conveniently and quickly create strong passwords whether or not they use a password manager.

## Features

- Lightweight and user-friendly CLI

- Performs faster than GUI-based alternatives

- Native-OS executable file avaliable for Windows, Linux and macOS

- User can specify password length

- Uses Python's 'secret' module for cryptographically secure password generation

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

**NOTE:** Generating passwords less than or equal to the character length of 16 will be done instantly or within a few seconds and will only consume an average of 15 to 20 MB of RAM. Generating passwords over the character length of 16 digits can take over a minute to generate and can use up more than 100 MBs of RAM, though this largerly depends on your PC's specs. For e.g. testing on the M1 chip showed that passwords with character lengths as long as 99999 could be generated under a second.

Processor (CPU): Intel Core Solo

Windows Operating System: Microsoft Windows XP

macOS Operating System: Mac OS X

Linux Operating System: Ubuntu Oneiric Ocelot

Memory: 500 MB RAM

Storage: 1 GB (8 MB excl. neccessary OS files)

## Getting Started

To edit the .py file, use the package manager pip(3) to install cryptography:
```
(sudo) pip(3) install cryptography
```
To clone the repo:
```
git clone https://github.com/sharma-it/password-generator.git
```
To change to the project directory:
```
cd password-generator
```

## Usage

- Generated passwords are stored into a text file named 'password list.txt' and the generated cryptographic key is named 'password list key.key'. Both can be found in the same file path where the application sits. **Do not rename either files and always keep both of them in the same file path of the application.**

- Opening the text file through the application exhibits different behabiours from OS to OS. On MacOS and Linux, the text file can remain open while the applicaiton is running, however you should still manually close the text file before continuing to use the Password Generator. Whereas on Windows, after opening the text file through the application, you cannot continue to use the Password Generator without first closing the text file, that's if you have 'Notepad' set as your default text editor. Using another program or a Windows 10/11 app such as 'Notepads App' can allow the application to run without needing to close the text file, however you should still close the text file before continuing to use the Password Generator.

- In order to encrypt and decrypt the text file, you need to generate a cryptographic key which can be done with the commands '-g k' or 'gen k'.

Below is a key for the list of in-built commands and arguments that can be used to make the application perform certain actions.

**Commands/Arguments Key:**

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
| exit |	string | Exits application. |

## Contributing

Pull requests are welcomed. For major changes, please open an issue first to discuss what you would like to change.

## Contact

Shubham Sharma - [My LinkedIn](https://www.linkedin.com/in/sharma-it/) - shubhamsharma.emails@gmail.com.

## License

This project is licensed under the GPL 3.0 License - see the [LICENSE](LICENSE) file for details.
