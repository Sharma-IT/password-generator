"""
passgen - A secure password generation and management tool.
Created by Shubham Sharma (https://github.com/Sharma-IT)
"""

from .password_generator import (
    VERSION,
    Config,
    Console,
    PasswordGenerator,
    FileHelper,
)

__version__ = VERSION
__author__ = "Shubham Sharma"
__email__ = "shubhamsharma.emails@gmail.com"
__url__ = "https://github.com/Sharma-IT/passgen"

__all__ = [
    "VERSION",
    "Config",
    "Console",
    "PasswordGenerator",
    "FileHelper",
]
