import reflex as rx
from app.states.auth_state import AuthState


def reset_field(
    label: str, type_: str, id_: str, placeholder: str, icon_name: str
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label,
            html_for=id_,
            class_name="block text-sm font-semibold text-gray-700 mb-1",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon(icon_name, class_name="h-5 w-5 text-gray-400"),
                class_name="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none",
            ),
            rx.el.input(
                id=id_,
                name=id_,
                type=type_,
                required=True,
                placeholder=placeholder,
                class_name="block w-full pl-10 pr-3 py-2.5 border border-gray-300 rounded-lg focus:ring-teal-500 focus:border-teal-500 sm:text-sm transition duration-150 ease-in-out",
            ),
            class_name="relative rounded-md shadow-sm",
        ),
        class_name="mb-5",
    )


def brand_panel() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            class_name="absolute top-0 left-0 w-full h-full overflow-hidden opacity-10 pointer-events-none",
            style={
                "background_image": "radial-gradient(circle at 20% 150%, #ffffff 0, transparent 50%), radial-gradient(circle at 80% -50%, #ffffff 0, transparent 50%)"
            },
        ),
        rx.el.div(
            rx.image(
                src="/medical_professional_technology.png",
                class_name="h-24 w-24 mb-8 bg-white p-2 rounded-2xl shadow-lg",
            ),
            rx.el.h1(
                "MediLink",
                class_name="text-4xl font-bold text-white mb-2 tracking-tight",
            ),
            rx.el.p(
                "Connected Healthcare Documentation",
                class_name="text-teal-100 text-lg font-medium mb-8",
            ),
            rx.el.div(
                rx.el.p(
                    "Securely recover your account access. We'll help you get back to documenting patient care in no time.",
                    class_name="text-center text-white/80 leading-relaxed max-w-md",
                ),
                class_name="backdrop-blur-sm bg-white/10 p-6 rounded-xl border border-white/10 shadow-xl",
            ),
            class_name="relative z-10 flex flex-col items-center justify-center text-center h-full max-w-2xl mx-auto",
        ),
        class_name="hidden lg:flex w-1/2 bg-gradient-to-br from-teal-600 to-blue-800 relative overflow-hidden items-center justify-center",
    )


def email_step() -> rx.Component:
    return rx.el.form(
        rx.el.p(
            "Enter your email address to find your account.",
            class_name="text-gray-500 mb-8 text-center lg:text-left",
        ),
        reset_field("Email Address", "email", "email", "name@hospital.com", "mail"),
        rx.cond(
            AuthState.reset_error != "",
            rx.el.div(
                rx.icon(
                    "circle-alert", class_name="h-5 w-5 text-red-500 mr-2 shrink-0"
                ),
                rx.el.span(
                    AuthState.reset_error, class_name="text-sm text-red-700 font-medium"
                ),
                class_name="mb-6 flex items-center bg-red-50 border border-red-100 p-4 rounded-lg animate-fade-in",
            ),
        ),
        rx.el.div(
            rx.el.button(
                "Find Account",
                type="submit",
                class_name="w-full flex justify-center py-3 px-4 border border-transparent rounded-lg shadow-sm text-sm font-semibold text-white bg-teal-600 hover:bg-teal-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-teal-500 transition-all duration-200",
            ),
            class_name="pt-2",
        ),
        on_submit=AuthState.check_email_exists,
        class_name="space-y-2 animate-fade-in",
        key="email_step_form",
    )


def reset_step() -> rx.Component:
    return rx.el.form(
        rx.el.div(
            rx.el.p("Resetting password for:", class_name="text-gray-500 text-sm"),
            rx.el.p(AuthState.reset_email, class_name="font-medium text-gray-900 mb-6"),
        ),
        reset_field(
            "New Password", "password", "password", "Enter new password", "lock"
        ),
        reset_field(
            "Confirm Password",
            "password",
            "confirm_password",
            "Confirm new password",
            "lock",
        ),
        rx.cond(
            AuthState.reset_error != "",
            rx.el.div(
                rx.icon(
                    "circle-alert", class_name="h-5 w-5 text-red-500 mr-2 shrink-0"
                ),
                rx.el.span(
                    AuthState.reset_error, class_name="text-sm text-red-700 font-medium"
                ),
                class_name="mb-6 flex items-center bg-red-50 border border-red-100 p-4 rounded-lg animate-fade-in",
            ),
        ),
        rx.el.div(
            rx.el.button(
                "Set New Password",
                type="submit",
                class_name="w-full flex justify-center py-3 px-4 border border-transparent rounded-lg shadow-sm text-sm font-semibold text-white bg-teal-600 hover:bg-teal-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-teal-500 transition-all duration-200",
            ),
            class_name="pt-2",
        ),
        on_submit=AuthState.reset_password,
        class_name="space-y-2 animate-fade-in",
        key="reset_step_form",
    )


def forgot_password_form_container() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.image(
                        src="/medical_professional_technology.png",
                        class_name="h-12 w-12 mx-auto mb-4",
                    ),
                    class_name="lg:hidden text-center",
                ),
                rx.el.h2(
                    "Account Recovery",
                    class_name="text-2xl font-bold text-gray-900 mb-2 text-center lg:text-left",
                ),
                rx.cond(AuthState.show_reset_form, reset_step(), email_step()),
                rx.el.div(
                    rx.el.a(
                        rx.icon("arrow-left", class_name="h-4 w-4 mr-2"),
                        "Back to Login",
                        href="/login",
                        on_click=AuthState.clear_reset_state,
                        class_name="inline-flex items-center text-sm font-medium text-teal-600 hover:text-teal-500",
                    ),
                    class_name="flex justify-center lg:justify-start mt-6 pt-6 border-t border-gray-100",
                ),
                class_name="w-full max-w-md px-8 py-10 bg-white shadow-2xl rounded-2xl border border-gray-100",
            )
        ),
        class_name="w-full lg:w-1/2 flex flex-col justify-center items-center p-4 sm:p-8 bg-gray-50 min-h-screen",
    )


def forgot_password_page() -> rx.Component:
    return rx.el.div(
        brand_panel(),
        forgot_password_form_container(),
        class_name="flex min-h-screen font-['Inter'] bg-gray-50",
    )