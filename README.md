## Password Generator

For those who still don't use a password manager but want to use stronger passwords; a powerful, secure and simple open-source password generator.

## Features

- Lightweight and user-friendly CLI

- Performs faster than GUI-based alternatives

- Cross OS-compatible (Windows/Linux/macOS)

- User can specify password length

- Uses 'secret' module for cryptographically securer password generation

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

Linux Operating System: Ubuntu Oneiric Ocelot

Memory: 500 MB RAM

Storage: 1 GB (8 MB excl. neccessary OS files)

## Getting Started

To run or edit the .py file, use the package manager pip(3) to install cryptography:
```sh
(sudo) pip(3) install cryptography
```
To clone the repo:
```sh
git clone https://github.com/sharma-it/password-generator.git
```

## Usage

**NOTE:**

- Generated passwords are stored into a text file named 'password list.txt' and the generated cryptographic key named 'password list key.key' can be found in the file path of the script. **Do not rename either files and keep both of them in the file path of the application.**

- If you open the text file through the script and if you have 'Notepad' set as your default program for opening '.txt' files, you will have to close the '.txt' file's window, if you want to continue to use the script. Using another program or a Windows 10 app such as 'Notepads App' can allow the application to run without needing to close the .txt file's window.

- In order to encrypt and decrypt the text file, you need to generate a cryptographic key which can be done with the commands '-g k' or 'gen k'.

Below is a key for the list of in-built commands and arguments that can be used to make the script perform certain actions.

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

This project is licensed under the GPL 3.0 License - see the [LICENSE](LICENCE) file for details.
