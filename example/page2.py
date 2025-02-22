import streamlit as st

def page2():
    st.markdown("page2")

if __name__ == "__page__":
    if st.session_state.login:
        page2()
    else:
        result = st.session_state.auth.login_form()
        if result and not result["success"]:
            st.error(f"login failed: {result["message"]}")