import streamlit as st

def page4():
    st.markdown("already logged in")

def signup_form():
    with st.form("signup_form"):
        email = st.text_input("email")
        password = st.text_input("password", type="password")
        if st.form_submit_button("signup"):
            result = st.session_state.auth.signup(email, password)
            if result["success"]:
                st.toast("signup success")
                st.switch_page("page1.py")
            else:
                st.error(f"signup failed: {result["message"]}")
            

if __name__ == "__page__":
    if st.session_state.login:
        page4()
    else:
        signup_form()
