## Password Generator

For those who still don't use a password manager; a powerful, secure and simple open-source password generator.

## Features
- Console-based application, simple UI for technical users, and higher performing over a GUI alternative
- Simple and easy to use application file that doesn't require admin privileges
- Automatically stores generated passwords into text file
- Can generate a symmetric cryptographic key to encrypt and decrypt text file
- Can run offline and makes no outgoing or incoming network connections
- Virtually no limit on generated passwords lengths
- Only 8.23 mb in size and uses an average of 20 mb of RAM (when generating passwords less than the character length of 1 million)

## Minimum System Requirements

**NOTE:** Generating passwords less than the character length of 1 million will be done instantly or within a few seconds and will only consume an average of 15 - 20 mb of RAM. Generating passwords over the character length of 1 million can take over a minute to generate and can use up more than 100 mb of RAM.

Processor (CPU): Intel Core Solo

Operating System: Microsoft Windows XP

Memory: 500 MB RAM

Storage: 1 GB

## Getting Started

To run or edit the .py file, use the package manager pip to install cryptography:
```sh
pip3 install cryptography
```
To clone the repo:
```sh
git clone https://github.com/sharma-it/password-generator.git
```

## Usage

**NOTE:**

- Generated passwords will be stored into a text file named 'password list.txt' and the generated cryptographic key named 'password list key.key' can be found in the file path of the application. **Do not rename either files and keep both of them in the file path of the application**
- If you open the text file through the application an if you have Notepad set as your default program for opening .txt files you will have to close the .txt file window if you want to continue to use the application. Using another program or Windows 10 app such as 'Notepads App' can allow the application to run with the .txt file still opened
- In order to encrypt and decrypt the text file you need to generate a cryptographic key which can be done with the commands '-g k' or 'gen k'

Below is a key for the list of in-built commands and arguments that can be used to perform certain actions in this application.

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

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact

Shubham Sharma - [My LinkedIn](https://www.linkedin.com/in/sharma-it/) - shubhamsharma.emails@gmail.com

## License

This project is licensed under the GPL 3.0 License - see the [LICENSE](LICENCE) file for details
