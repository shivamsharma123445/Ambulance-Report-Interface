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
    current_user: Optional[UserProfile] = None
    is_authenticated: bool = False
    login_error: str = ""
    is_editing_profile: bool = False

    @rx.event
    def login(self, form_data: dict):
        email = form_data.get("email", "").strip()
        password = form_data.get("password", "").strip()
        if not email or not password:
            self.login_error = "Please enter both email and password."
            return
        if email in self.users:
            self.current_user = self.users[email]
        else:
            new_user = UserProfile(email=email)
            self.users[email] = new_user
            self.current_user = new_user
        self.is_authenticated = True
        self.login_error = ""
        if not self.current_user.is_setup_complete:
            self.is_editing_profile = True
            return rx.redirect("/profile")
        else:
            return rx.redirect("/")

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