# streamlit-firebase-auth

**Overview**  
streamlit-firebase-auth is a lightweight Streamlit component library that simplifies integrating Firebase Authentication into your apps. It provides built-in widgets for login and logout functionalities as well as session management utilities, enabling you to quickly add secure, Firebase-powered user authentication to your Streamlit projects.

# Install

```
pip install streamlit-firebase-auth

```

# Quick Use

```python
from streamlit_firebase_auth import FirebaseAuth

auth = FirebaseAuth(
        {
            "apiKey": "YOUR_API_KEY",
            "authDomain": "YOUR_AUTH_DOMAIN",
            "projectId": "YOUR_PROJECT_ID",
            "storageBucket": "YOUR_STORAGE_BUCKET",
            "messagingSenderId": "YOUR_MESSAGING_SENDER_ID",
            "appId": "YOUR_APP_ID",
        })

login_user = auth.check_session()

if login_user:
    auth.logout_form()
else:
    suth.login_form()
```

# API Reference

## auth.login_form()
**Description:**  
Displays a login form to the user and returns the result of the login attempt.

**Return (dict):**  
- `success` (bool): True if login was successful; otherwise, False.  
- `message` (str, optional): An error message if the login failed.

## auth.logout_form()
**Description:**  
Displays a logout interface and performs logout operations (like clearing the session).

**Return (dict):**  
- `success` (bool): True if logout was successful; otherwise, False.  
- `message` (str, optional): An error message if the logout failed.

## auth.check_session()
**Description:**  
Checks the current session to determine if the user is authenticated.

**Return (dict):**  
A dictionary containing the user information provided by Firebase upon successful login.


# Detailed Usage

Please refer to the example for detailed usage.

Run :

```shell
streamlit run example/app.py
```

# Image

![Image](https://github.com/user-attachments/assets/b0c6e0ed-c9aa-4785-bd81-92a62040842f)
