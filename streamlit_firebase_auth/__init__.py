import os
import streamlit.components.v1 as components
import warnings
from typing import Any
import firebase_admin
from firebase_admin import auth
from firebase_admin.exceptions import FirebaseError


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
        self._component_func = _get_component_func(False)
        self.firebase_config = firebase_config
        self.lang = lang

    # Displays the login form
    # After executing the login, {"success": True, "user": UserInfo } or {"success": False, "message": "xxx"} will be returned
    def login_form(self) -> dict[str, str]:
        return_val = self._component_func(name="LoginForm", firebase_config=self.firebase_config, lang=self.lang, height=500, default=None)
        return return_val

    # Displays the logout form
    # After executing the logout, {"success": True} or {"success": False, "message": "xxx"} will be returned
    def logout_form(self) -> dict[str, str]:
        return_val = self._component_func(name="LogoutForm", firebase_config=self.firebase_config, lang=self.lang, default=None)
        return return_val
    
    # Displays the password reset button
    # After sending email, {"success": True} or {"success": False, "message": "xxx"} will be returned
    def send_password_reset_email(self, email: str) -> dict[str, str]:
        return_val = self._component_func(name="SendPasswordResetEmail", firebase_config=self.firebase_config, lang=self.lang, email=email, default=None)
        return return_val

    # Checks the session
    # If the session is valid, a dict with user information is returned
    # If the session is invalid, None is returned
    def check_session(self) -> dict[str, Any]:
        return_val = self._component_func(name="CheckSession", firebase_config=self.firebase_config, lang=self.lang, default=None)
        return return_val

    # signup user with firebase-admin
    # After executing the signup, {"success": True } or {"success": False, "message": "xxx"} will be returned
    # Required to run it with an IAM that has firebase-admin permissions assigned.
    # https://firebase.google.com/docs/admin/setup?hl=ja
    # https://firebase.google.com/docs/auth/admin/manage-users?hl=ja#create_a_user
    def signup(self, email: str, password: str) -> None:
        TRANSLATIONS = {
            "en": {
                "failed_init": "Failed to initialize firbase-admin",
                "email_exists": "The user with the same email address already exists.",
                "invalid_password": "The password does not meet the requirements.",
                "failed_create_user": "Failed to create user"
            },
            "jp": {
                "failed_init": "firbase-adminの初期化に失敗しました",
                "email_exists": "既に同じメールアドレスのユーザーが存在します。",
                "invalid_password": "パスワードの要件を満たしていません。",
                "failed_create_user": "ユーザー作成に失敗しました"
            }
        }
        try:
            firebase_admin.get_app()
        except ValueError:
            try:
                firebase_admin.initialize_app()
            except FirebaseError as e:
                return {"success": False, "message": TRANSLATIONS[self.lang]["failed_init"] + f": {str(e)}"}

        try:
            auth.create_user(email=email, password=password)
            return {"success": True}
        except auth.EmailAlreadyExistsError:
            return {"success": False, "message": TRANSLATIONS[self.lang]["email_exists"] + f": {str(e)}"}
        except Exception as e:
            if "password" in str(e).lower():
                return {"success": False, "message": TRANSLATIONS[self.lang]["invalid_password"] + f": {str(e)}"}
            return {"success": False, "message": TRANSLATIONS[self.lang]["failed_create_user"] + f": {str(e)}"}

