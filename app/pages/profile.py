import reflex as rx
from app.states.auth_state import AuthState, UserProfile
from app.components.navbar import page_wrapper


def profile_field(label: str, value: str, icon_name: str) -> rx.Component:
    return rx.el.div(
        rx.el.dt(
            rx.icon(icon_name, class_name="h-5 w-5 text-gray-400 mr-2"),
            label,
            class_name="flex items-center text-sm font-medium text-gray-500",
        ),
        rx.el.dd(
            value, class_name="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2 ml-7"
        ),
        class_name="py-4 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4",
    )


def form_field(
    label: str, name: str, default_value: str, type_: str = "text"
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label, html_for=name, class_name="block text-sm font-medium text-gray-700"
        ),
        rx.el.div(
            rx.el.input(
                type=type_,
                name=name,
                id=name,
                default_value=default_value,
                class_name="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-teal-500 focus:border-teal-500 sm:text-sm",
            ),
            class_name="mt-1",
        ),
        class_name="col-span-6 sm:col-span-4",
    )


def view_profile(user: UserProfile) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                "Driver Information",
                class_name="text-lg leading-6 font-medium text-gray-900",
            ),
            rx.el.p(
                "Personal details and ambulance assignment.",
                class_name="mt-1 max-w-2xl text-sm text-gray-500",
            ),
            rx.el.button(
                rx.icon("pencil", class_name="h-4 w-4 mr-2"),
                "Edit Profile",
                on_click=AuthState.toggle_edit_profile,
                class_name="mt-4 inline-flex items-center px-4 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-teal-500",
            ),
            class_name="px-4 py-5 sm:px-6 mb-4",
        ),
        rx.el.div(
            rx.el.dl(
                profile_field("Full Name", user.name, "user"),
                profile_field("Email Address", user.email, "mail"),
                profile_field("Phone Number", user.phone, "phone"),
                profile_field("Ambulance ID", user.ambulance_id, "ambulance"),
                profile_field("Vehicle Number", user.vehicle_number, "truck"),
            ),
            class_name="border-t border-gray-200 px-4 py-5 sm:p-0",
        ),
        class_name="bg-white shadow overflow-hidden sm:rounded-lg",
    )


def edit_profile(user: UserProfile) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                "Edit Profile", class_name="text-lg leading-6 font-medium text-gray-900"
            ),
            rx.el.p(
                "Update your information below.",
                class_name="mt-1 text-sm text-gray-500",
            ),
            class_name="px-4 py-5 sm:px-6",
        ),
        rx.el.div(
            rx.el.form(
                rx.el.div(
                    rx.el.div(
                        form_field("Full Name", "name", user.name),
                        form_field("Phone Number", "phone", user.phone, "tel"),
                        form_field("Ambulance ID", "ambulance_id", user.ambulance_id),
                        form_field(
                            "Vehicle Number", "vehicle_number", user.vehicle_number
                        ),
                        class_name="grid grid-cols-6 gap-6",
                    ),
                    class_name="px-4 py-5 bg-white sm:p-6",
                ),
                rx.el.div(
                    rx.el.button(
                        "Cancel",
                        type="button",
                        on_click=AuthState.toggle_edit_profile,
                        class_name="bg-white py-2 px-4 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-teal-500 mr-3",
                    ),
                    rx.el.button(
                        "Save Changes",
                        type="submit",
                        class_name="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-teal-600 hover:bg-teal-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-teal-500",
                    ),
                    class_name="px-4 py-3 bg-gray-50 text-right sm:px-6 flex justify-end",
                ),
                on_submit=AuthState.save_profile,
            ),
            class_name="border-t border-gray-200",
        ),
        class_name="bg-white shadow sm:rounded-lg",
    )


def profile_content() -> rx.Component:
    return rx.cond(
        AuthState.is_editing_profile,
        edit_profile(AuthState.current_user),
        view_profile(AuthState.current_user),
    )


def profile_page() -> rx.Component:
    return page_wrapper(profile_content())