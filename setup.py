import os
from setuptools import setup, find_packages

setup(
    name="passgen",
    version="1.4.0",
    packages=find_packages(),
    install_requires=[
        'cryptography',
        'keyring',
        'zxcvbn'
    ],
    entry_points={
        'console_scripts': [
            'passgen=src.password_generator:main',
        ],
    },
    author="Shubham Sharma",
    description="A secure password generator with encryption capabilities",
    long_description=open('README.md').read() if os.path.exists('README.md') else '',
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
)
