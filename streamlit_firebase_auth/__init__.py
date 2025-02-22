import os
import streamlit.components.v1 as components
import warnings
from typing import Any
import time

def _get_component_func(release=True):
    if not release:
        warnings.warn("WARNING: firebase_auth is in development mode.")
        return components.declare_component(
            "firebase_auth",
            url="http://localhost:3001",
        )
    else:
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        build_dir = os.path.join(parent_dir, "frontend", "build")
        return components.declare_component("firebase_auth", path=build_dir)

class FirebaseAuth:

    def __init__(self, firebase_config = dict[str, str], lang: str = "en"):
        print("aaaaaaaaaaaaaa")
        self._component_func = _get_component_func(False)
        self.firebase_config = firebase_config
        self.lang = lang

    # Displays the login form
    # After executing the login, {"success": True} or {"success": False, "message": "xxx"} will be returned
    def login_form(self) -> dict[str, str]:
        return_val = self._component_func(name="LoginForm", firebase_config=self.firebase_config, lang=self.lang, height=500, default=None)
        return return_val

    # Displays the logout form
    # After executing the logout, {"success": True} or {"success": False, "message": "xxx"} will be returned
    def logout_form(self) -> dict[str, str]:
        return_val = self._component_func(name="LogoutForm", firebase_config=self.firebase_config, lang=self.lang, default=None)
        return return_val

    # Checks the session
    # If the session is valid, a dict with user information is returned
    # If the session is invalid, None is returned
    def check_session(self) -> dict[str, Any]:
        return_val = self._component_func(name="CheckSession", firebase_config=self.firebase_config, lang=self.lang, default=None)
        return return_val

    # signup user
    # After executing the signup, {"success": True, "user": UserInfo } or {"success": False, "message": "xxx"} will be returned
    # https://firebase.google.com/docs/admin/setup?hl=ja
    def signup(self, email: str, password: str) -> dict[str, Any]:
        return_val = self._component_func(name="Signup", email=email, password=password, firebase_config=self.firebase_config, lang=self.lang, default=None)
        return_val = self._component_func(name="Signup", email=email, password=password, firebase_config=self.firebase_config, lang=self.lang, default=None)
        for i in range(10):
            print(f"===={i}====")
            print(return_val)
            if return_val is not None:
                break
            time.sleep(0.3)
            
        print("######")
        print(return_val)
        print("#####")
        return return_val