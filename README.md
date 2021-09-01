## Password Generator

For those who still don't use a password manager; a powerful, secure and simple open-source password generator.

## Features
- Uses a console that acts as the UI: for a simplified end user experience, a fully-adjustable window size, and an increase in performance compared to a GUI
- Simple and esy to use application file that doesn't require admin privileges
- Automatically stores generated passwords into text file
- Can generate a symmetric cryptographic key to encrypt and decrypt text file
- Can run offline and makes no outgoing or incoming network connections
- Virtually no limit on generated passwords lengths
- Only 8.23 mb in size and uses an average of 20 mb of RAM (when generating passwords less than the character length of 1 million)

## System Requirements

**NOTE:** Generating passwords less than the character length of 1 million will be done instantly or within a few seconds and will only consume an average of 15 - 20 mb of RAM. Generating passwords over the character length of 1 million can take over a minute to generate and can use up more than 100 mb of RAM.

Processor (CPU): Intel Core Solo

Operating System: Microsoft Windows XP

Memory: 500 MB RAM

Storage: 1 GB

To run this application on a **Linux OS**, you can use a program such as Wine (winehq.org) which can run the excecutable file on the Linux OS by translating Windows API calls to calls a Linux kernel can understand.

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
- As you generate a password the text file will open up showing you what the generated password looks like. If you have Notepad set as your default program for opening .txt files you have to close the text file if you want to continue to use the application. Using another program or Windows 10 app such as 'Notepads App' can allow for the application to run without having to close the text file
- In order to encrypt and decrypt the text file you need to generate a cryptographic key which can be done with the command 'k'.
- To cancel the generation of a password, use 0. This will generate no password and will open the text file.

Below is a key for the list of in-built commands that you or whoever as the end user can use to perform certain actions in this application.

**User Commands Key:**

| User Command Type | Input Type | Parse Types |
| ----------------- | ---------- | ----------- |
| p |	string | Generates password. |
| k |	string | Generates cryptographic key. |
| w |	string | Wipes text file. |
| o |	string | Opens text file. |
| e |	string | Encrypts text file. |
| d |	string | Decrypts text file. |
| h |	string | Lists all in-built commands. |
| c |	string | Closes program. |

## FAQ

Q.1: Why does Notepad force the application to stop after the text file is opened through it?

A: Simply due to how Notepad is built, Notepad can't show an appended change done by an external script or program to an opened .txt file in real-time, thus the .txt file has to be closed before being able to perform another action in the application.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact

Shubham Sharma - [My LinkedIn](https://www.linkedin.com/in/ssjuniorit/) - shubhamsharma.emails@gmail.com

## License

This project is licensed under the GPL 3.0 License - see the [LICENSE](LICENCE) file for details
