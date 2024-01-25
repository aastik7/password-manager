# Password Manager

This is a simple command-line password manager written in Python using the cryptography library.

## Features

- **Secure Storage**: Passwords are encrypted using the Fernet symmetric encryption scheme.
- **Master Password**: A master password is required to add or view passwords.
- **Data Persistence**: Passwords are stored in a file ("password.txt"), and the encryption key is stored in a separate file ("key.key").
- **Usage**: Easily add new passwords and view existing ones through the command-line interface.

## Setup

1. Install Python 3: [Python Downloads](https://www.python.org/downloads/)

2. Clone the repository:

    ```bash
    git clone https://github.com/aastik7/password-manager.git
    ```

3. Navigate to the project directory:

    ```bash
    cd password-manager
    ```

4. Install dependencies (cryptography library):

    ```bash
    pip install cryptography
    ```

5. Run the password manager:

    ```bash
    python password_manager.py
    ```

## Usage

1. **Set Master Password:**

   - The first time you run the script, it will prompt you to set your master password.

2. **View Passwords:**

   - Enter 'view' to see a list of existing usernames and decrypted passwords. You'll need to provide the master password to access this information.

3. **Add Passwords:**

   - Enter 'add' to add a new password. You'll need to provide the master password to add a password.

4. **Quit:**

   - Enter 'q' to quit the password manager.

## Notes

- Make sure to keep your master password secure. Losing it may result in irreversible data loss.
- Back up your "key.key" file regularly to prevent data loss.
- This is a basic password manager and may not be suitable for all use cases. Consider more advanced solutions for sensitive applications.

## License

This project is licensed under the [MIT License](LICENSE).
