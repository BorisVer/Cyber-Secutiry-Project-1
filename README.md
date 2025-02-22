# Cyber-Secutiry-Project-1

## How to Run

### 1. Install Dependencies
Ensure you have Python installed, then install the required dependencies:  

```bash
pip install -r requirements.txt
```

Using Top 10 from 2021

Flaw 1:

CSRF: Cross-Site Request Forgery

- The CSRF protection is imported in the app.py on line 2, and its use is shown on line 8
- The protection within a form is done inside the templates/makeuser.html file on line 21 and templates/index.html file on line 136
- To make the entire application secure the same csrf_token would need to be in each form used on the application
- By opening the csrf_attack.html with the csrf protection commented away you can simulate a csrf attack and make a new user without token
- This user will be created and can be logged in to, but after enabeling csrf protection the same attack will end in: "Bad Request, The CSRF token is missing." and no user will be created




Flaw 2:

SQL injection

- Vulnerable code is at routes.py lines 70-79 and the fixed version 81-98
- The SQL is run straight without filtering the input, meaning that if username and password both have input ' OR '1'='1' --, this makes the sql SELECT user_id, password FROM users WHERE username=' OR '1'='1' -- AND password=' OR '1'='1' -- which is always true because of the '1'='1', loggin user in onto the user with user_id = 1: In this case it is automatically made user Hecules. 
- The fix for this is not directly inputing the input into the sql, and checking the password outside of the sql to be sure no injection is possibel




Flaw 3

Broken Access Control

- Changing other users data that should not be possible
- Broken code in the routes.py /changeinfo
- The fix is to not use the username = username that mistakenly runs the code for all users instead of the just the intended


Flaw 4

Sensitive Data Exposure

- Data like passwords being stored as plain text instead of hashed
- In routes.py /makeuser hash
- Fix is simply to hash the passwords before saving them in the database


Flaw 5

Security Misconfiguration

- Running the application in debug mode means users can see detailed error messages that can be used to exploit the application
- In production the application should always be run with debug=False
