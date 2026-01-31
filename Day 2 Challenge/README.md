# Student Registration Validator

## Description
This is a simple Python program that validates student registration details based on a set of predefined rules. The program checks whether the student ID, email, password, and referral code meet specific conditions and then approves or rejects the registration.

## Features
- **Student ID Validation:** Must follow the format `CSE-XXX` where `XXX` are digits.
- **Email Validation:** Must contain `@`, have at least one dot, and end with `.edu`.
- **Password Validation:** Must be at least 8 characters long, start with an uppercase letter, and contain at least one digit.
- **Referral Code Validation:** Must follow the format `REFXX@` where `X` are digits.

## How It Works
1. The program asks the user to enter:
   - Student ID
   - Email ID
   - Password
   - Referral Code
2. Each input is checked against the rules using **conditional statements** and **string manipulation**.
3. If all inputs are valid, the registration is **APPROVED**; otherwise, it is **REJECTED**.

## Skills Learned
- Validating user input in Python
- Using string operations such as slicing, counting characters, and checking digits
- Applying conditional statements for multiple checks
- Logical thinking for real-world data validation scenarios

## How to Run
1. Open Python on your system.
2. Copy the program code into a `.py` file.
3. Run the file and follow the prompts to enter the required details.

## Example
Enter Student ID: CSE-123
Enter Email ID: example@university.edu

Enter Password: Password1
Enter Referral Code: REF12@
APPROVED
