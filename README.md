# OTP-verification

The `OTP.py` file contains the skeleton of the code used to generate a random 4-digit OTP, send it via email, and perform two-factor authentication.

## How the System Works
1. **Collect Email**: The system first collects the email address from the user to be verified.
2. **Generate OTP**: A 4-digit random number is generated as the OTP using Python's `random` module.
3. **Send Email**: The system uses the `smtplib` library to log in to the sender's email and send the OTP.
4. **Verify OTP**: The system prompts the user to enter the OTP. The user is given 5 attempts to enter the correct OTP.

## Prerequisites
Before using this code, ensure you have the following:
- A Gmail account (preferably not a personal account for security reasons).
- An app password for the Gmail account, which allows the SMTP object to log in to the sender's email. Note that you cannot use the password created during Gmail registration in place of the app password.
- An active internet connection when executing the code.

## Using the Code
To use the code:
1. Copy the code from `OTP.py`.
2. Replace `<sender address>` with your email address.
3. Replace `<sender email password ie.app password>` with the app password generated.
4. Modify the subject and body of the email message accordingly.
5. Also modify the number of attempts to enter a correct OTP.
6. Execute the code and follow the prompts.
