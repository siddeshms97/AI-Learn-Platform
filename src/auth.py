import bcrypt
import streamlit as st
from src.db import add_user, get_user, update_user_login


def hash_password(password):
    """Hash password using bcrypt"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(password, password_hash):
    """Verify password against hash"""
    return bcrypt.checkpw(password.encode(), password_hash.encode())


def register_user(username, email, password, password_confirm):
    """Register a new user"""
    if not username or not email or not password:
        return False, "All fields are required"

    if password != password_confirm:
        return False, "Passwords do not match"

    if len(password) < 6:
        return False, "Password must be at least 6 characters"

    password_hash = hash_password(password)

    if add_user(username, email, password_hash):
        return True, "Registration successful! Please log in."
    else:
        return False, "Username or email already exists"


def login_user(username, password):
    """Login user"""
    user = get_user(username)

    if user is None:
        return False, "User not found"

    if verify_password(password, user["password_hash"]):
        update_user_login(user["id"])
        return True, user
    else:
        return False, "Invalid password"


def is_logged_in():
    """Check if user is logged in"""
    return "user" in st.session_state and st.session_state.user is not None


def logout_user():
    """Logout user"""
    if "user" in st.session_state:
        del st.session_state.user
