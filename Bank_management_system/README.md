Bank Management System in Python 🏦

A simple Bank Management System implemented in Python. This console-based project allows users to create a bank account, deposit money, withdraw money, check balance, and change password securely using a password-protected system.

⸻

Features ✨
	•	Create Account: Register with your name, age, phone number, and initial deposit.
	•	Deposit Money: Add money to your account after password verification.
	•	Withdraw Money: Withdraw money from your account with password verification and balance check.
	•	Check Balance: View current account balance.
	•	Change Password: Update your account password securely.
	•	Menu-driven Interface: Simple console menu that continues until exit.

⸻

How It Works 🛠️
	1.	Create Account
	•	User provides name, age, phone number, and initial deposit.
	•	The system generates a 10-digit random account number.
	•	User sets a password for security.
	2.	Deposit and Withdraw
	•	Requires entering the password.
	•	Updates account balance after verifying password.
	•	Withdrawals are allowed only if sufficient balance is available.
	3.	Check Balance
	•	Allows the user to view their current balance securely.
	4.	Change Password
	•	Lets the user update their password to keep the account secure.

________


excepted output:


Welcome to our bank
Enter your name: Rajesh
Enter your age: 22
Enter your phone number: 9876543210
------------------------------------------
        Name          : Rajesh
        Age           : 22
        Phone Number  : 9876543210
        Account Number: 1234567890
        Deposit your initial amount
Enter the amount to deposit: 5000
Create your password
Enter the password: 1234
Account created successfully
---------------------------------------------
Menu:
1. Create Account
2. Cash Deposit
3. Cash Withdraw
4. Balance Inquiry
5. PIN Change
6. Exit
Enter your choice: 2
Enter the password: 1234
Enter the amount to deposit: 2000
2000 deposited successfully
Current balance is 7000

____________

