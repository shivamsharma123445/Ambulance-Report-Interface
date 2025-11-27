import reflex as rx
from typing import Optional
from pydantic import BaseModel
from sqlmodel import select
from app.models import User
import logging


class UserProfile(BaseModel):
    id: int = 0
    name: str = ""
    phone: str = ""
    ambulance_id: str = ""
    vehicle_number: str = ""
    email: str = ""
    is_setup_complete: bool = False


class AuthState(rx.State):
    current_user: Optional[UserProfile] = None
    is_authenticated: bool = False
    login_error: str = ""
    is_editing_profile: bool = False
    reset_email: str = ""
    reset_error: str = ""
    reset_success: str = ""
    show_reset_form: bool = False

    def _get_user_by_email(self, email: str) -> Optional[User]:
        with rx.session() as session:
            return session.exec(select(User).where(User.email == email)).first()

    @rx.event
    def login(self, form_data: dict):
        email = form_data.get("email", "").strip()
        password = form_data.get("password", "").strip()
        if not email or not password:
            self.login_error = "Please enter both email and password."
            return
        with rx.session() as session:
            user = session.exec(select(User).where(User.email == email)).first()
            if not user and email == "admin@ambulance.com" and (password == "admin123"):
                user = User(
                    email=email,
                    password=password,
                    name="John Doe",
                    phone="555-0123",
                    ambulance_id="AMB-001",
                    vehicle_number="KV-9988",
                    is_setup_complete=True,
                )
                session.add(user)
                session.commit()
                session.refresh(user)
            if user:
                if user.password == password:
                    self.current_user = UserProfile(
                        id=user.id,
                        name=user.name,
                        phone=user.phone,
                        ambulance_id=user.ambulance_id,
                        vehicle_number=user.vehicle_number,
                        email=user.email,
                        is_setup_complete=user.is_setup_complete,
                    )
                    self.is_authenticated = True
                    self.login_error = ""
                    if not self.current_user.is_setup_complete:
                        self.is_editing_profile = True
                        return rx.redirect("/profile")
                    else:
                        return rx.redirect("/")
                else:
                    self.login_error = "Invalid password."
            else:
                self.login_error = "User not found."

    @rx.event
    def register(self, form_data: dict):
        email = form_data.get("email", "").strip()
        password = form_data.get("password", "").strip()
        if not email or not password:
            return rx.toast.error("Please provide email and password")
        with rx.session() as session:
            existing_user = session.exec(
                select(User).where(User.email == email)
            ).first()
            if existing_user:
                return rx.toast.error("User already exists")
            new_user = User(email=email, password=password)
            session.add(new_user)
            session.commit()
            return rx.toast.success("Registration successful. Please login.")

    @rx.event
    def check_email_exists(self, form_data: dict):
        email = form_data.get("email", "").strip()
        if not email:
            self.reset_error = "Please enter your email address."
            return
        user = self._get_user_by_email(email)
        if user:
            self.reset_email = email
            self.reset_error = ""
            self.show_reset_form = True
        else:
            self.reset_error = "Email address not found."

    @rx.event
    def reset_password(self, form_data: dict):
        password = form_data.get("password", "").strip()
        confirm_password = form_data.get("confirm_password", "").strip()
        if not password or not confirm_password:
            self.reset_error = "Please fill in all fields."
            return
        if password != confirm_password:
            self.reset_error = "Passwords do not match."
            return
        with rx.session() as session:
            user = session.exec(
                select(User).where(User.email == self.reset_email)
            ).first()
            if user:
                user.password = password
                session.add(user)
                session.commit()
                self.reset_success = "Password reset successfully."
                self.reset_error = ""
                self.show_reset_form = False
                self.reset_email = ""
                yield rx.toast.success("Password reset successfully. Please login.")
                yield rx.redirect("/login")
            else:
                self.reset_error = "Error resetting password."

    @rx.event
    def clear_reset_state(self):
        self.reset_email = ""
        self.reset_error = ""
        self.reset_success = ""
        self.show_reset_form = False

    @rx.event
    def logout(self):
        self.current_user = None
        self.is_authenticated = False
        return rx.redirect("/login")

    @rx.event
    def toggle_edit_profile(self):
        self.is_editing_profile = not self.is_editing_profile

    @rx.event
    def save_profile(self, form_data: dict):
        if not self.current_user or not self.current_user.id:
            return
        with rx.session() as session:
            user = session.exec(
                select(User).where(User.id == self.current_user.id)
            ).first()
            if user:
                user.name = form_data.get("name", "")
                user.phone = form_data.get("phone", "")
                user.ambulance_id = form_data.get("ambulance_id", "")
                user.vehicle_number = form_data.get("vehicle_number", "")
                user.is_setup_complete = True
                session.add(user)
                session.commit()
                session.refresh(user)
                self.current_user.name = user.name
                self.current_user.phone = user.phone
                self.current_user.ambulance_id = user.ambulance_id
                self.current_user.vehicle_number = user.vehicle_number
                self.current_user.is_setup_complete = user.is_setup_complete
                self.is_editing_profile = False
                return rx.toast.success("Profile saved successfully.")

    @rx.event
    def require_auth(self):
        """Run on page load for protected routes."""
        if not self.is_authenticated:
            return rx.redirect("/login")

    @rx.event
    def redirect_if_authenticated(self):
        """Run on page load for login page."""
        if self.is_authenticated:
            return rx.redirect("/")