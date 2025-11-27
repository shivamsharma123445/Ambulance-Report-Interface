import reflex as rx
from typing import Optional
from pydantic import BaseModel


class UserProfile(BaseModel):
    name: str = ""
    phone: str = ""
    ambulance_id: str = ""
    vehicle_number: str = ""
    email: str = ""
    is_setup_complete: bool = False


class AuthState(rx.State):
    users: dict[str, UserProfile] = {
        "admin@ambulance.com": UserProfile(
            name="John Doe",
            phone="555-0123",
            ambulance_id="AMB-001",
            vehicle_number="KV-9988",
            email="admin@ambulance.com",
            is_setup_complete=True,
        )
    }
    users_passwords: dict[str, str] = {"admin@ambulance.com": "admin123"}
    current_user: Optional[UserProfile] = None
    is_authenticated: bool = False
    login_error: str = ""
    is_editing_profile: bool = False
    reset_email: str = ""
    reset_error: str = ""
    reset_success: str = ""
    show_reset_form: bool = False

    @rx.event
    def login(self, form_data: dict):
        email = form_data.get("email", "").strip()
        password = form_data.get("password", "").strip()
        if not email or not password:
            self.login_error = "Please enter both email and password."
            return
        if email in self.users:
            stored_password = self.users_passwords.get(email)
            if stored_password and stored_password != password:
                self.login_error = "Invalid password."
                return
            self.current_user = self.users[email]
            if not stored_password:
                self.users_passwords[email] = password
        else:
            new_user = UserProfile(email=email)
            self.users[email] = new_user
            self.users_passwords[email] = password
            self.current_user = new_user
        self.is_authenticated = True
        self.login_error = ""
        if not self.current_user.is_setup_complete:
            self.is_editing_profile = True
            return rx.redirect("/profile")
        else:
            return rx.redirect("/")

    @rx.event
    def check_email_exists(self, form_data: dict):
        email = form_data.get("email", "").strip()
        if not email:
            self.reset_error = "Please enter your email address."
            return
        if email in self.users:
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
        self.users_passwords[self.reset_email] = password
        self.reset_success = "Password reset successfully."
        self.reset_error = ""
        self.show_reset_form = False
        self.reset_email = ""
        yield rx.toast.success("Password reset successfully. Please login.")
        yield rx.redirect("/login")

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
        if not self.current_user:
            return
        self.current_user.name = form_data.get("name", "")
        self.current_user.phone = form_data.get("phone", "")
        self.current_user.ambulance_id = form_data.get("ambulance_id", "")
        self.current_user.vehicle_number = form_data.get("vehicle_number", "")
        self.current_user.is_setup_complete = True
        self.users[self.current_user.email] = self.current_user
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