import streamlit as st

def page3():
    result = st.session_state.auth.send_password_reset_email(st.session_state.login_user["email"])
    if result:
        if result["success"]:
            st.success("success")
        else:
            st.error(f"failed to send password reset email: {result["message"]}")

if __name__ == "__page__":
    if st.session_state.login:
        page3()
    else:
        result = st.session_state.auth.login_form()
        if result and not result["success"]:
            st.error(f"login failed: {result["message"]}")
