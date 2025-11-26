import reflex as rx
from app.states.auth_state import AuthState


def navbar() -> rx.Component:
    return rx.el.nav(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.image(
                        src="/medical_professional_technology.png", class_name="h-8 w-8"
                    ),
                    rx.el.span(
                        "MediLink", class_name="ml-2 text-xl font-bold text-teal-700"
                    ),
                    href="/",
                    class_name="flex items-center",
                ),
                rx.el.div(
                    rx.el.a(
                        "Dashboard",
                        href="/",
                        class_name="px-3 py-2 rounded-md text-sm font-medium text-gray-600 hover:text-teal-600 hover:bg-teal-50 transition-colors",
                    ),
                    rx.el.a(
                        "Profile",
                        href="/profile",
                        class_name="px-3 py-2 rounded-md text-sm font-medium text-gray-600 hover:text-teal-600 hover:bg-teal-50 transition-colors",
                    ),
                    rx.el.button(
                        rx.icon("log-out", class_name="h-4 w-4 mr-2"),
                        "Logout",
                        on_click=AuthState.logout,
                        class_name="ml-4 flex items-center px-4 py-2 border border-teal-200 rounded-md shadow-sm text-sm font-medium text-teal-700 bg-white hover:bg-teal-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-teal-500 transition-colors",
                    ),
                    class_name="flex items-center space-x-4",
                ),
                class_name="flex justify-between h-16",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
        ),
        class_name="bg-white border-b border-gray-200 shadow-sm sticky top-0 z-50",
    )


def page_wrapper(content: rx.Component) -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(content, class_name="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8"),
        class_name="min-h-screen bg-gray-50 font-['Inter']",
    )