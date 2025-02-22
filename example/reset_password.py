import streamlit as st

def page3():
    print(st.session_state.login_user)
    st.session_state.auth.send_password_reset_email(st.session_state.login_user["email"])

if __name__ == "__page__":
    if st.session_state.login:
        page3()
    else:
        result = st.session_state.auth.login_form()
        if result:
            st.session_state.login = result["success"]
            st.session_state.login = result["user"]
            if result["success"]:
                st.switch_page("page1.py")
            else:
                st.error("login failed")