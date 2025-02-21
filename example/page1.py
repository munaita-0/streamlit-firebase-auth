import streamlit as st

def page1():
    st.markdown("page1")

if __name__ == "__page__":
    if st.session_state.login:
        page1()
    else:
        result = st.session_state.auth.login_form()
        if result:
            st.session_state.login = result["success"]
            if result["success"]:
                st.switch_page("page1.py")
            else:
                st.error("login failed")
