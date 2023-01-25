## Password Generator

For those who still don't use a password manager but want to use stronger passwords; a powerful, secure and simple open-source password generator.

## Features

- Console-based script; easy-to-use UI for technical users.

- Performs faster than GUI-based alternatives.

- Usage does not require admin privileges.

- Automatically logs generated passwords into a text file.

- Can generate a symmetric cryptographic key to encrypt and decrypt the text file.

- Can open the text file using the operating system's default text editor.

- Can run offline and makes no outgoing or incoming network connections.

- Virtually no limit on generated passwords lengths.

- Only 8.23 mb in size and uses an average of 20 mb of RAM (when generating passwords with a character length less than 1 million).

## Minimum System Requirements

**NOTE:** Generating passwords less than the character length of 1 million will be done instantly or within a few seconds and will only consume an average of 15 - 20 mb of RAM. Generating passwords over the character length of 1 million can take over a minute to generate and can use up more than 100 mb of RAM.

Processor (CPU): Intel Core Solo

Operating System: Microsoft Windows XP

Memory: 500 MB RAM

Storage: 1 GB

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
