import reflex as rx
from app.states.report_state import ReportState
from app.components.navbar import page_wrapper


def detail_item(label: str, value: str | bool | int) -> rx.Component:
    return rx.el.div(
        rx.el.dt(label, class_name="text-sm font-medium text-gray-500"),
        rx.el.dd(
            rx.cond(
                value == True, "Yes", rx.cond(value == False, "No", value.to_string())
            ),
            class_name="mt-1 text-sm text-gray-900",
        ),
        class_name="sm:col-span-1",
    )


def section_header(title: str) -> rx.Component:
    return rx.el.h3(
        title,
        class_name="text-lg leading-6 font-medium text-gray-900 border-b border-gray-200 pb-2 mb-4 mt-6",
    )


def report_detail_content() -> rx.Component:
    r = ReportState.current_report_detail
    injuries = r["injuries"].to(dict)
    assessment = r["assessment"].to(dict)
    treatment = r["treatment"].to(dict)
    photos = r["photos"].to(list)
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Accident Report #" + r["id"].to_string(),
                    class_name="text-2xl font-bold text-gray-900",
                ),
                rx.el.p(
                    "Created on " + r["created_at"].to_string(),
                    class_name="text-sm text-gray-500",
                ),
                class_name="flex-1",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon("arrow-left", class_name="h-4 w-4 mr-2"),
                    "Back",
                    on_click=rx.redirect("/"),
                    class_name="mr-3 inline-flex items-center px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50",
                ),
                rx.el.button(
                    rx.icon("pencil", class_name="h-4 w-4 mr-2"),
                    "Edit",
                    on_click=lambda: ReportState.load_report_for_edit(r["id"]),
                    class_name="mr-3 inline-flex items-center px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50",
                ),
                rx.el.button(
                    rx.icon("trash-2", class_name="h-4 w-4 mr-2"),
                    "Delete",
                    on_click=lambda: ReportState.open_delete_dialog(r["id"]),
                    class_name="inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-red-600 hover:bg-red-700",
                ),
                class_name="flex items-center mt-4 md:mt-0",
            ),
            class_name="md:flex md:items-center md:justify-between mb-8",
        ),
        rx.el.div(
            section_header("Accident Information"),
            rx.el.dl(
                detail_item("Date", r["accident_date"]),
                detail_item("Time", r["accident_time"]),
                detail_item("Location", r["location"]),
                detail_item("Type", r["accident_type"]),
                detail_item("Patient Count", r["patient_count"]),
                class_name="grid grid-cols-1 gap-x-4 gap-y-6 sm:grid-cols-2",
            ),
            section_header("Patient Information"),
            rx.cond(
                r["is_patient_speaking"],
                rx.el.dl(
                    detail_item("Name", r["patient_name"]),
                    detail_item("Age", r["patient_age"]),
                    detail_item("Gender", r["patient_gender"]),
                    detail_item("Contact", r["patient_contact"]),
                    detail_item("Allergies", r["patient_allergies"]),
                    detail_item("History", r["patient_history"]),
                    class_name="grid grid-cols-1 gap-x-4 gap-y-6 sm:grid-cols-2",
                ),
                rx.el.dl(
                    detail_item("Estimated Age", r["est_patient_age"]),
                    detail_item("Estimated Gender", r["est_patient_gender"]),
                    detail_item("Consciousness", r["consciousness_level"]),
                    class_name="grid grid-cols-1 gap-x-4 gap-y-6 sm:grid-cols-2",
                ),
            ),
            section_header("Injuries Identified"),
            rx.el.div(
                rx.cond(
                    injuries["head"],
                    rx.el.span(
                        "Head",
                        class_name="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-red-100 text-red-800 mr-2 mb-2",
                    ),
                ),
                rx.cond(
                    injuries["chest"],
                    rx.el.span(
                        "Chest",
                        class_name="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-red-100 text-red-800 mr-2 mb-2",
                    ),
                ),
                rx.cond(
                    injuries["abdomen"],
                    rx.el.span(
                        "Abdomen",
                        class_name="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-red-100 text-red-800 mr-2 mb-2",
                    ),
                ),
                rx.cond(
                    injuries["legs"],
                    rx.el.span(
                        "Legs",
                        class_name="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-red-100 text-red-800 mr-2 mb-2",
                    ),
                ),
                rx.cond(
                    injuries["arms"],
                    rx.el.span(
                        "Arms",
                        class_name="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-red-100 text-red-800 mr-2 mb-2",
                    ),
                ),
                rx.cond(
                    injuries["spine"],
                    rx.el.span(
                        "Spine",
                        class_name="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-red-100 text-red-800 mr-2 mb-2",
                    ),
                ),
                rx.cond(
                    injuries["burns"],
                    rx.el.span(
                        "Burns",
                        class_name="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-red-100 text-red-800 mr-2 mb-2",
                    ),
                ),
                class_name="flex flex-wrap",
            ),
            section_header("Condition Assessment"),
            rx.el.dl(
                detail_item("Breathing", assessment["breathing"]),
                detail_item("Pain Level", assessment["pain"]),
                detail_item("Bleeding", assessment["bleeding"]),
                rx.cond(
                    assessment["bleeding"],
                    detail_item("Bleeding Description", assessment["bleeding_desc"]),
                ),
                detail_item("Chief Complaint", assessment["complaint"]),
                class_name="grid grid-cols-1 gap-x-4 gap-y-6 sm:grid-cols-2",
            ),
            section_header("Treatment Administered"),
            rx.el.div(
                rx.cond(
                    treatment["oxygen"],
                    rx.el.span(
                        "Oxygen",
                        class_name="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-green-100 text-green-800 mr-2 mb-2",
                    ),
                ),
                rx.cond(
                    treatment["bandage"],
                    rx.el.span(
                        "Bandage",
                        class_name="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-green-100 text-green-800 mr-2 mb-2",
                    ),
                ),
                rx.cond(
                    treatment["iv"],
                    rx.el.span(
                        "IV Fluids",
                        class_name="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-green-100 text-green-800 mr-2 mb-2",
                    ),
                ),
                rx.cond(
                    treatment["cpr"],
                    rx.el.span(
                        "CPR",
                        class_name="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-green-100 text-green-800 mr-2 mb-2",
                    ),
                ),
                rx.cond(
                    treatment["neck_collar"],
                    rx.el.span(
                        "Neck Collar",
                        class_name="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-green-100 text-green-800 mr-2 mb-2",
                    ),
                ),
                rx.cond(
                    treatment["splint"],
                    rx.el.span(
                        "Splint",
                        class_name="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-green-100 text-green-800 mr-2 mb-2",
                    ),
                ),
                class_name="flex flex-wrap mb-4",
            ),
            rx.cond(
                treatment["other"],
                rx.el.p(
                    rx.el.span("Other: ", class_name="font-medium text-gray-900"),
                    treatment["other"],
                    class_name="text-sm text-gray-600",
                ),
            ),
            rx.cond(
                photos.length() > 0,
                rx.fragment(
                    section_header("Scene Photos"),
                    rx.el.div(
                        rx.foreach(
                            photos,
                            lambda p: rx.image(
                                src=rx.get_upload_url(p),
                                class_name="h-48 w-full object-cover rounded-lg border border-gray-200 shadow-sm",
                            ),
                        ),
                        class_name="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4",
                    ),
                ),
            ),
            class_name="bg-white shadow overflow-hidden sm:rounded-lg p-6",
        ),
        class_name="max-w-4xl mx-auto",
    )


def report_detail_page() -> rx.Component:
    return page_wrapper(
        rx.cond(
            ReportState.current_report_detail,
            report_detail_content(),
            rx.el.div("Report not found", class_name="p-8 text-center text-gray-500"),
        )
    )