import reflex as rx
from app.states.auth_state import AuthState


def login_field(
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
                    "Advanced digital solutions for emergency response documentation. Streamlining patient care data with precision and security.",
                    class_name="text-center text-white/80 leading-relaxed max-w-md",
                ),
                class_name="backdrop-blur-sm bg-white/10 p-6 rounded-xl border border-white/10 shadow-xl",
            ),
            class_name="relative z-10 flex flex-col items-center justify-center text-center h-full max-w-2xl mx-auto",
        ),
        class_name="hidden lg:flex w-1/2 bg-gradient-to-br from-teal-600 to-blue-800 relative overflow-hidden items-center justify-center",
    )


def login_form_container() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.image(
                    src="/medical_professional_technology.png",
                    class_name="h-12 w-12 mx-auto mb-4",
                ),
                class_name="lg:hidden text-center",
            ),
            rx.el.h2(
                "Welcome Back",
                class_name="text-2xl font-bold text-gray-900 mb-2 text-center lg:text-left",
            ),
            rx.el.p(
                "Please sign in to access the MediLink dashboard.",
                class_name="text-gray-500 mb-8 text-center lg:text-left",
            ),
            rx.el.form(
                login_field(
                    "Email Address", "email", "email", "name@hospital.com", "mail"
                ),
                login_field(
                    "Password", "password", "password", "Enter your password", "lock"
                ),
                rx.cond(
                    AuthState.login_error,
                    rx.el.div(
                        rx.icon(
                            "circle-alert",
                            class_name="h-5 w-5 text-red-500 mr-2 shrink-0",
                        ),
                        rx.el.span(
                            AuthState.login_error,
                            class_name="text-sm text-red-700 font-medium",
                        ),
                        class_name="mb-6 flex items-center bg-red-50 border border-red-100 p-4 rounded-lg animate-fade-in",
                    ),
                ),
                rx.el.div(
                    rx.el.button(
                        "Sign In",
                        type="submit",
                        class_name="w-full flex justify-center py-3 px-4 border border-transparent rounded-lg shadow-sm text-sm font-semibold text-white bg-teal-600 hover:bg-teal-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-teal-500 transition-all duration-200 transform hover:-translate-y-0.5",
                    ),
                    class_name="pt-2",
                ),
                rx.el.div(
                    rx.el.a(
                        "Forgot your password?",
                        href="#",
                        class_name="text-sm font-medium text-teal-600 hover:text-teal-500",
                    ),
                    class_name="flex justify-end mt-4",
                ),
                on_submit=AuthState.login,
                class_name="space-y-2",
            ),
            class_name="w-full max-w-md px-8 py-10 bg-white shadow-2xl rounded-2xl border border-gray-100",
        ),
        class_name="w-full lg:w-1/2 flex flex-col justify-center items-center p-4 sm:p-8 bg-gray-50 min-h-screen",
    )


def login_page() -> rx.Component:
    return rx.el.div(
        brand_panel(),
        login_form_container(),
        class_name="flex min-h-screen font-['Inter'] bg-gray-50",
    )