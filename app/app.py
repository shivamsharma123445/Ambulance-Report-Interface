import reflex as rx
from app.states.auth_state import AuthState
from app.states.report_state import ReportState
from app.pages.login import login_page
from app.pages.profile import profile_page
from app.pages.create_report import create_report_page
from app.pages.report_detail import report_detail_page
from app.components.navbar import page_wrapper
from app.components.dashboard import dashboard_content


def index() -> rx.Component:
    return page_wrapper(dashboard_content())


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
    stylesheets=[
        "https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css"
    ],
)
app.add_page(login_page, route="/login", on_load=AuthState.redirect_if_authenticated)
app.add_page(profile_page, route="/profile", on_load=AuthState.require_auth)
app.add_page(create_report_page, route="/create-report", on_load=AuthState.require_auth)
app.add_page(report_detail_page, route="/report/[id]", on_load=AuthState.require_auth)
app.add_page(index, route="/", on_load=AuthState.require_auth)