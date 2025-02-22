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

    # signup user with firebase-admin
    # After executing the signup, {"success": True } or {"success": False, "message": "xxx"} will be returned
    # Required to run it with an IAM that has firebase-admin permissions assigned.
    # https://firebase.google.com/docs/admin/setup?hl=ja
    # https://firebase.google.com/docs/auth/admin/manage-users?hl=ja#create_a_user
    def signup(self, email: str, password: str) -> None:
        try:
            firebase_admin.get_app()
        except ValueError:
            try:
                firebase_admin.initialize_app()
            except FirebaseError as e:
                return {"success": False, "message": "firbase-adminの初期化に失敗しました"}

        try:
            auth.create_user(email=email, password=password)
            return {"success": True}
        except auth.EmailAlreadyExistsError:
            return {"success": False, "message": "既に同じメールアドレスのユーザーが存在します。"}
        except auth.InvalidPasswordError:
            return {"success": False, "message": "パスワードの要件を満たしていません。"}
        except FirebaseError as e:
            return {"success": False, "message": "ユーザー作成に失敗しました"}

