# Python Password Manager (CLI + Encrypted)

A simple command-line password manager built in Python as my 3rd python project.

## Features

- Generate secure random passwords
- Store passwords per service
- Retrieve saved passwords
- Update existing passwords
- Delete passwords safely
- List all saved services
- Encrypt password storage via Fernet

## Security

Passwords are encrypted before being saved to a JSON file and decrypted only when accessed.

A local key file (`key.key`) is used for encryption (not included in repo for safety).

## Technologies

- Python
- JSON file storage
- Fernet

## What I learned

I made this program in approximately 4 hours, this is what i leanred:

- how to handle files in Python
- the foundation of how encryption works
- CLI app design
- How to create snapshots with Git
- How to properly upload a project to github

## How to run

```bash
python main.py
