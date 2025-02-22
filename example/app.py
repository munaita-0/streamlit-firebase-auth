import streamlit as st
from streamlit_firebase_auth import FirebaseAuth

if "auth" not in st.session_state or not st.session_state.auth:
    st.session_state.auth = FirebaseAuth(
        {
            # "apiKey": "YOUR_API_KEY",
            # "authDomain": "YOUR_AUTH_DOMAIN",
            # "projectId": "YOUR_PROJECT_ID",
            # "storageBucket": "YOUR_STORAGE_BUCKET",
            # "messagingSenderId": "YOUR_MESSAGING_SENDER_ID",
            # "appId": "YOUR_APP_ID",
        })
if "login" not in st.session_state or not st.session_state.login:
    st.session_state.login_user = st.session_state.auth.check_session()
    st.session_state.login = st.session_state.login_user is not None

pages = [
    st.Page("page1.py"),
    st.Page("page2.py"),
    st.Page("page3.py"),
    st.Page("signup.py"),
]

with st.sidebar:
    result = st.session_state.auth.logout_form()
    if result:
        st.session_state.login = result["success"]
        if result["success"]:
            st.session_state.login = False
            st.success("successfully logged out")
        else:
            st.error("failed to log out")

pg = st.navigation(pages)
pg.run()