import reflex as rx
from app.states.report_state import ReportState
from app.components.navbar import page_wrapper


def step_indicator() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                rx.el.span("Step ", class_name="font-medium"),
                rx.text(ReportState.current_step),
                rx.el.span(" of 6", class_name="text-gray-500"),
                class_name="text-sm text-gray-900",
            ),
            rx.el.div(
                rx.el.div(
                    class_name="h-full bg-teal-600 rounded-full transition-all duration-300 ease-in-out",
                    style={
                        "width": rx.cond(
                            ReportState.current_step == 1,
                            "16%",
                            rx.cond(
                                ReportState.current_step == 2,
                                "33%",
                                rx.cond(
                                    ReportState.current_step == 3,
                                    "50%",
                                    rx.cond(
                                        ReportState.current_step == 4,
                                        "66%",
                                        rx.cond(
                                            ReportState.current_step == 5, "83%", "100%"
                                        ),
                                    ),
                                ),
                            ),
                        )
                    },
                ),
                class_name="mt-2 h-2 w-full bg-gray-200 rounded-full overflow-hidden",
            ),
            class_name="w-full mb-8",
        )
    )


def accident_info_step() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Accident Information", class_name="text-xl font-bold text-gray-900 mb-4"
        ),
        rx.el.div(
            rx.el.label(
                "Location", class_name="block text-sm font-medium text-gray-700"
            ),
            rx.el.input(
                on_change=ReportState.set_location,
                placeholder="Enter accident location",
                class_name="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-teal-500 focus:border-teal-500 sm:text-sm",
                default_value=ReportState.location,
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            rx.el.label(
                "Accident Type", class_name="block text-sm font-medium text-gray-700"
            ),
            rx.el.select(
                rx.el.option("Road Accident", value="Road"),
                rx.el.option("Fall", value="Fall"),
                rx.el.option("Fire", value="Fire"),
                rx.el.option("Other", value="Other"),
                value=ReportState.accident_type,
                on_change=ReportState.set_accident_type,
                class_name="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-teal-500 focus:border-teal-500 sm:text-sm rounded-md",
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.label(
                    "Date", class_name="block text-sm font-medium text-gray-700"
                ),
                rx.el.input(
                    type="date",
                    on_change=ReportState.set_accident_date,
                    class_name="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-teal-500 focus:border-teal-500 sm:text-sm",
                    default_value=ReportState.accident_date,
                ),
                class_name="flex-1",
            ),
            rx.el.div(
                rx.el.label(
                    "Time", class_name="block text-sm font-medium text-gray-700"
                ),
                rx.el.input(
                    type="time",
                    on_change=ReportState.set_accident_time,
                    class_name="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-teal-500 focus:border-teal-500 sm:text-sm",
                    default_value=ReportState.accident_time,
                ),
                class_name="flex-1",
            ),
            class_name="flex gap-4 mb-4",
        ),
        rx.el.div(
            rx.el.label(
                "Number of Patients",
                class_name="block text-sm font-medium text-gray-700",
            ),
            rx.el.input(
                type="number",
                min="1",
                on_change=ReportState.set_patient_count,
                class_name="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-teal-500 focus:border-teal-500 sm:text-sm",
                default_value=ReportState.patient_count,
            ),
            class_name="mb-4",
        ),
    )


def speaking_patient_form() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.label(
                "Patient Name", class_name="block text-sm font-medium text-gray-700"
            ),
            rx.el.input(
                on_change=ReportState.set_patient_name,
                class_name="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-teal-500 focus:border-teal-500 sm:text-sm",
                default_value=ReportState.patient_name,
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.label(
                    "Age", class_name="block text-sm font-medium text-gray-700"
                ),
                rx.el.input(
                    type="number",
                    on_change=ReportState.set_patient_age,
                    class_name="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-teal-500 focus:border-teal-500 sm:text-sm",
                    default_value=ReportState.patient_age,
                ),
                class_name="flex-1",
            ),
            rx.el.div(
                rx.el.label(
                    "Gender", class_name="block text-sm font-medium text-gray-700"
                ),
                rx.el.select(
                    rx.el.option("Male", value="Male"),
                    rx.el.option("Female", value="Female"),
                    rx.el.option("Other", value="Other"),
                    value=ReportState.patient_gender,
                    on_change=ReportState.set_patient_gender,
                    class_name="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-teal-500 focus:border-teal-500 sm:text-sm rounded-md",
                ),
                class_name="flex-1",
            ),
            class_name="flex gap-4 mb-4",
        ),
        rx.el.div(
            rx.el.label(
                "Contact Number (Optional)",
                class_name="block text-sm font-medium text-gray-700",
            ),
            rx.el.input(
                on_change=ReportState.set_patient_contact,
                class_name="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-teal-500 focus:border-teal-500 sm:text-sm",
                default_value=ReportState.patient_contact,
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            rx.el.label(
                "Allergies", class_name="block text-sm font-medium text-gray-700"
            ),
            rx.el.textarea(
                on_change=ReportState.set_patient_allergies,
                rows=2,
                class_name="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-teal-500 focus:border-teal-500 sm:text-sm",
                default_value=ReportState.patient_allergies,
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            rx.el.label(
                "Past Illnesses", class_name="block text-sm font-medium text-gray-700"
            ),
            rx.el.textarea(
                on_change=ReportState.set_patient_history,
                rows=2,
                class_name="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-teal-500 focus:border-teal-500 sm:text-sm",
                default_value=ReportState.patient_history,
            ),
            class_name="mb-4",
        ),
        class_name="animate-fade-in",
    )


def non_speaking_patient_form() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.label(
                    "Estimated Age",
                    class_name="block text-sm font-medium text-gray-700",
                ),
                rx.el.input(
                    type="text",
                    placeholder="e.g. 30s",
                    on_change=ReportState.set_est_patient_age,
                    class_name="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-teal-500 focus:border-teal-500 sm:text-sm",
                    default_value=ReportState.est_patient_age,
                ),
                class_name="flex-1",
            ),
            rx.el.div(
                rx.el.label(
                    "Gender Estimate",
                    class_name="block text-sm font-medium text-gray-700",
                ),
                rx.el.select(
                    rx.el.option("Male", value="Male"),
                    rx.el.option("Female", value="Female"),
                    rx.el.option("Unknown", value="Unknown"),
                    value=ReportState.est_patient_gender,
                    on_change=ReportState.set_est_patient_gender,
                    class_name="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-teal-500 focus:border-teal-500 sm:text-sm rounded-md",
                ),
                class_name="flex-1",
            ),
            class_name="flex gap-4 mb-4",
        ),
        rx.el.div(
            rx.el.label(
                "Consciousness Level",
                class_name="block text-sm font-medium text-gray-700",
            ),
            rx.el.select(
                rx.el.option("Alert", value="Alert"),
                rx.el.option("Drowsy", value="Drowsy"),
                rx.el.option("Unconscious", value="Unconscious"),
                value=ReportState.consciousness_level,
                on_change=ReportState.set_consciousness_level,
                class_name="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-teal-500 focus:border-teal-500 sm:text-sm rounded-md",
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            rx.el.label(
                "Major Injuries",
                class_name="block text-sm font-medium text-gray-700 mb-2",
            ),
            rx.el.div(
                rx.el.label(
                    rx.el.input(
                        type="checkbox",
                        checked=ReportState.injury_head,
                        on_change=ReportState.set_injury_head,
                        class_name="h-4 w-4 text-teal-600 focus:ring-teal-500 border-gray-300 rounded mr-2",
                    ),
                    "Head",
                    class_name="flex items-center text-sm text-gray-700",
                ),
                rx.el.label(
                    rx.el.input(
                        type="checkbox",
                        checked=ReportState.injury_chest,
                        on_change=ReportState.set_injury_chest,
                        class_name="h-4 w-4 text-teal-600 focus:ring-teal-500 border-gray-300 rounded mr-2",
                    ),
                    "Chest",
                    class_name="flex items-center text-sm text-gray-700",
                ),
                rx.el.label(
                    rx.el.input(
                        type="checkbox",
                        checked=ReportState.injury_abdomen,
                        on_change=ReportState.set_injury_abdomen,
                        class_name="h-4 w-4 text-teal-600 focus:ring-teal-500 border-gray-300 rounded mr-2",
                    ),
                    "Abdomen",
                    class_name="flex items-center text-sm text-gray-700",
                ),
                rx.el.label(
                    rx.el.input(
                        type="checkbox",
                        checked=ReportState.injury_legs,
                        on_change=ReportState.set_injury_legs,
                        class_name="h-4 w-4 text-teal-600 focus:ring-teal-500 border-gray-300 rounded mr-2",
                    ),
                    "Legs",
                    class_name="flex items-center text-sm text-gray-700",
                ),
                rx.el.label(
                    rx.el.input(
                        type="checkbox",
                        checked=ReportState.injury_arms,
                        on_change=ReportState.set_injury_arms,
                        class_name="h-4 w-4 text-teal-600 focus:ring-teal-500 border-gray-300 rounded mr-2",
                    ),
                    "Arms",
                    class_name="flex items-center text-sm text-gray-700",
                ),
                rx.el.label(
                    rx.el.input(
                        type="checkbox",
                        checked=ReportState.injury_spine,
                        on_change=ReportState.set_injury_spine,
                        class_name="h-4 w-4 text-teal-600 focus:ring-teal-500 border-gray-300 rounded mr-2",
                    ),
                    "Spine",
                    class_name="flex items-center text-sm text-gray-700",
                ),
                rx.el.label(
                    rx.el.input(
                        type="checkbox",
                        checked=ReportState.injury_burns,
                        on_change=ReportState.set_injury_burns,
                        class_name="h-4 w-4 text-teal-600 focus:ring-teal-500 border-gray-300 rounded mr-2",
                    ),
                    "Burns",
                    class_name="flex items-center text-sm text-gray-700",
                ),
                class_name="grid grid-cols-2 gap-2",
            ),
        ),
        class_name="animate-fade-in",
    )


def patient_status_step() -> rx.Component:
    return rx.el.div(
        rx.el.h2("Patient Status", class_name="text-xl font-bold text-gray-900 mb-4"),
        rx.el.div(
            rx.el.span(
                "Is the patient able to speak?",
                class_name="text-sm font-medium text-gray-700 mr-3",
            ),
            rx.el.label(
                rx.el.input(
                    type="checkbox",
                    checked=ReportState.is_patient_speaking,
                    on_change=ReportState.toggle_speaking_status,
                    class_name="sr-only peer",
                ),
                rx.el.div(
                    class_name="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-teal-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-teal-600"
                ),
                class_name="relative inline-flex items-center cursor-pointer",
            ),
            class_name="flex items-center mb-6 p-4 bg-gray-50 rounded-lg",
        ),
        rx.cond(
            ReportState.is_patient_speaking,
            speaking_patient_form(),
            non_speaking_patient_form(),
        ),
    )


def condition_assessment_step() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Condition Assessment", class_name="text-xl font-bold text-gray-900 mb-4"
        ),
        rx.el.div(
            rx.el.label(
                "Consciousness Level",
                class_name="block text-sm font-medium text-gray-700",
            ),
            rx.el.select(
                rx.el.option("Alert", value="Alert"),
                rx.el.option("Drowsy", value="Drowsy"),
                rx.el.option("Confused", value="Confused"),
                rx.el.option("Unresponsive", value="Unresponsive"),
                value=ReportState.consciousness_level,
                on_change=ReportState.set_consciousness_level,
                class_name="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-teal-500 focus:border-teal-500 sm:text-sm rounded-md",
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            rx.el.label(
                "Breathing Status", class_name="block text-sm font-medium text-gray-700"
            ),
            rx.el.select(
                rx.el.option("Normal", value="Normal"),
                rx.el.option("Difficulty", value="Difficulty"),
                rx.el.option("Not Breathing", value="Not Breathing"),
                value=ReportState.breathing_status,
                on_change=ReportState.set_breathing_status,
                class_name="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-teal-500 focus:border-teal-500 sm:text-sm rounded-md",
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "Visible Bleeding?",
                    class_name="text-sm font-medium text-gray-700 mr-3",
                ),
                rx.el.label(
                    rx.el.input(
                        type="checkbox",
                        checked=ReportState.bleeding_status,
                        on_change=ReportState.toggle_bleeding_status,
                        class_name="sr-only peer",
                    ),
                    rx.el.div(
                        class_name="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-teal-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-teal-600"
                    ),
                    class_name="relative inline-flex items-center cursor-pointer",
                ),
                class_name="flex items-center mb-2",
            ),
            rx.cond(
                ReportState.bleeding_status,
                rx.el.textarea(
                    placeholder="Describe bleeding location and severity...",
                    on_change=ReportState.set_bleeding_description,
                    class_name="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-teal-500 focus:border-teal-500 sm:text-sm",
                    rows=2,
                    default_value=ReportState.bleeding_description,
                ),
            ),
            class_name="mb-4 p-4 bg-gray-50 rounded-lg",
        ),
        rx.el.div(
            rx.el.label(
                "Pain Level (1-10): " + ReportState.pain_level.to_string(),
                class_name="block text-sm font-medium text-gray-700 mb-2",
            ),
            rx.el.input(
                type="range",
                min="0",
                max="10",
                default_value=ReportState.pain_level,
                key="pain_level_slider",
                on_change=ReportState.set_pain_level.throttle(100),
                class_name="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-teal-600",
            ),
            rx.el.div(
                rx.el.span("No Pain", class_name="text-xs text-gray-500"),
                rx.el.span("Severe Pain", class_name="text-xs text-gray-500"),
                class_name="flex justify-between mt-1",
            ),
            class_name="mb-6",
        ),
        rx.el.div(
            rx.el.label(
                "Chief Complaint", class_name="block text-sm font-medium text-gray-700"
            ),
            rx.el.textarea(
                placeholder="Patient's main complaint...",
                on_change=ReportState.set_chief_complaint,
                class_name="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-teal-500 focus:border-teal-500 sm:text-sm",
                rows=3,
                default_value=ReportState.chief_complaint,
            ),
            class_name="mb-4",
        ),
    )


def treatment_checkbox(
    label: str, checked: bool, on_change: rx.event.EventType
) -> rx.Component:
    return rx.el.label(
        rx.el.input(
            type="checkbox",
            checked=checked,
            on_change=on_change,
            class_name="h-5 w-5 text-teal-600 focus:ring-teal-500 border-gray-300 rounded mr-3",
        ),
        rx.el.span(label, class_name="text-gray-700 font-medium"),
        class_name="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors cursor-pointer",
    )


def treatment_given_step() -> rx.Component:
    return rx.el.div(
        rx.el.h2("Treatment Given", class_name="text-xl font-bold text-gray-900 mb-4"),
        rx.el.div(
            treatment_checkbox(
                "Oxygen", ReportState.treatment_oxygen, ReportState.set_treatment_oxygen
            ),
            treatment_checkbox(
                "Bandage",
                ReportState.treatment_bandage,
                ReportState.set_treatment_bandage,
            ),
            treatment_checkbox(
                "IV Fluids", ReportState.treatment_iv, ReportState.set_treatment_iv
            ),
            treatment_checkbox(
                "CPR", ReportState.treatment_cpr, ReportState.set_treatment_cpr
            ),
            treatment_checkbox(
                "Neck Collar",
                ReportState.treatment_neck_collar,
                ReportState.set_treatment_neck_collar,
            ),
            treatment_checkbox(
                "Splint", ReportState.treatment_splint, ReportState.set_treatment_splint
            ),
            class_name="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-6",
        ),
        rx.el.div(
            rx.el.label(
                "Other Treatments", class_name="block text-sm font-medium text-gray-700"
            ),
            rx.el.textarea(
                placeholder="List any other treatments administered...",
                on_change=ReportState.set_treatment_other,
                class_name="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-teal-500 focus:border-teal-500 sm:text-sm",
                rows=3,
                default_value=ReportState.treatment_other,
            ),
            class_name="mb-4",
        ),
    )


def photo_preview(filename: str) -> rx.Component:
    return rx.el.div(
        rx.image(
            src=rx.get_upload_url(filename),
            class_name="h-24 w-24 object-cover rounded-lg border border-gray-200",
        ),
        rx.el.button(
            rx.icon("trash-2", class_name="h-4 w-4"),
            on_click=lambda: ReportState.remove_photo(filename),
            class_name="absolute -top-2 -right-2 p-1 bg-white rounded-full shadow-sm border border-gray-200 text-red-600 hover:bg-red-50",
        ),
        class_name="relative inline-block",
    )


def media_upload_step() -> rx.Component:
    return rx.el.div(
        rx.el.h2("Scene Photos", class_name="text-xl font-bold text-gray-900 mb-4"),
        rx.el.div(
            rx.upload.root(
                rx.el.div(
                    rx.icon("camera", class_name="h-10 w-10 text-gray-400 mb-2"),
                    rx.el.p(
                        "Tap to take photo or select from gallery",
                        class_name="text-sm text-gray-600 text-center",
                    ),
                    rx.el.p(
                        "Supports JPG, PNG", class_name="text-xs text-gray-400 mt-1"
                    ),
                    class_name="flex flex-col items-center justify-center p-6 border-2 border-dashed border-gray-300 rounded-lg bg-gray-50 hover:bg-gray-100 transition-colors cursor-pointer",
                ),
                id="report_photos",
                accept={"image/png": [".png"], "image/jpeg": [".jpg", ".jpeg"]},
                multiple=True,
                max_files=5,
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            rx.foreach(
                rx.selected_files("report_photos"),
                lambda file: rx.el.div(
                    rx.icon("paperclip", class_name="h-3 w-3 mr-2"),
                    rx.text(file, class_name="text-xs truncate"),
                    class_name="flex items-center text-gray-500 bg-gray-100 px-2 py-1 rounded mb-1",
                ),
            ),
            class_name="mb-4",
        ),
        rx.el.button(
            "Upload Selected Photos",
            on_click=ReportState.handle_upload(
                rx.upload_files(upload_id="report_photos")
            ),
            class_name="w-full mb-6 px-4 py-2 bg-white border border-gray-300 text-gray-700 text-sm font-medium rounded-md hover:bg-gray-50",
        ),
        rx.el.div(
            rx.el.h3(
                "Uploaded Photos", class_name="text-sm font-medium text-gray-900 mb-3"
            ),
            rx.cond(
                ReportState.uploaded_photos.length() > 0,
                rx.el.div(
                    rx.foreach(ReportState.uploaded_photos, photo_preview),
                    class_name="flex flex-wrap gap-4",
                ),
                rx.el.p(
                    "No photos uploaded yet.", class_name="text-sm text-gray-500 italic"
                ),
            ),
        ),
    )


def review_section(title: str, content: list[rx.Component]) -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            title,
            class_name="text-sm font-bold text-gray-900 uppercase tracking-wider mb-3 border-b pb-1",
        ),
        rx.el.div(
            *content, class_name="grid grid-cols-1 sm:grid-cols-2 gap-y-2 text-sm mb-6"
        ),
    )


def review_item(label: str, value: str) -> rx.Component:
    return rx.el.div(
        rx.el.span(label + ": ", class_name="font-medium text-gray-600"),
        rx.el.span(value, class_name="text-gray-900"),
    )


def review_summary_step() -> rx.Component:
    return rx.el.div(
        rx.el.h2("Review Report", class_name="text-xl font-bold text-gray-900 mb-6"),
        review_section(
            "Accident Info",
            [
                review_item("Date", ReportState.accident_date),
                review_item("Time", ReportState.accident_time),
                review_item("Location", ReportState.location),
                review_item("Type", ReportState.accident_type),
            ],
        ),
        review_section(
            "Patient Info",
            [
                rx.cond(
                    ReportState.is_patient_speaking,
                    rx.fragment(
                        review_item("Name", ReportState.patient_name),
                        review_item("Age", ReportState.patient_age),
                        review_item("Gender", ReportState.patient_gender),
                        review_item("Allergies", ReportState.patient_allergies),
                    ),
                    rx.fragment(
                        review_item("Est. Age", ReportState.est_patient_age),
                        review_item("Est. Gender", ReportState.est_patient_gender),
                        review_item("Status", "Unconscious/Non-Speaking"),
                    ),
                )
            ],
        ),
        review_section(
            "Condition",
            [
                review_item("Consciousness", ReportState.consciousness_level),
                review_item("Breathing", ReportState.breathing_status),
                review_item("Pain Level", ReportState.pain_level.to_string()),
                review_item(
                    "Bleeding", rx.cond(ReportState.bleeding_status, "Yes", "No")
                ),
                rx.cond(
                    ReportState.bleeding_status,
                    review_item("Bleeding Desc", ReportState.bleeding_description),
                    rx.fragment(),
                ),
            ],
        ),
        rx.el.div(
            rx.el.h3(
                "Treatments Administered",
                class_name="text-sm font-bold text-gray-900 uppercase tracking-wider mb-3 border-b pb-1",
            ),
            rx.el.div(
                rx.cond(
                    ReportState.treatment_oxygen,
                    rx.el.span(
                        "Oxygen",
                        class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800 mr-2",
                    ),
                ),
                rx.cond(
                    ReportState.treatment_bandage,
                    rx.el.span(
                        "Bandage",
                        class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800 mr-2",
                    ),
                ),
                rx.cond(
                    ReportState.treatment_iv,
                    rx.el.span(
                        "IV Fluids",
                        class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800 mr-2",
                    ),
                ),
                rx.cond(
                    ReportState.treatment_cpr,
                    rx.el.span(
                        "CPR",
                        class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800 mr-2",
                    ),
                ),
                rx.cond(
                    ReportState.treatment_neck_collar,
                    rx.el.span(
                        "Neck Collar",
                        class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800 mr-2",
                    ),
                ),
                rx.cond(
                    ReportState.treatment_splint,
                    rx.el.span(
                        "Splint",
                        class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800 mr-2",
                    ),
                ),
                class_name="flex flex-wrap mb-6",
            ),
        ),
        rx.cond(
            ReportState.uploaded_photos.length() > 0,
            rx.el.div(
                rx.el.h3(
                    "Photos",
                    class_name="text-sm font-bold text-gray-900 uppercase tracking-wider mb-3 border-b pb-1",
                ),
                rx.el.div(
                    rx.foreach(
                        ReportState.uploaded_photos,
                        lambda filename: rx.image(
                            src=rx.get_upload_url(filename),
                            class_name="h-20 w-20 object-cover rounded-md border border-gray-200",
                        ),
                    ),
                    class_name="flex gap-3 flex-wrap",
                ),
            ),
        ),
    )


def navigation_buttons() -> rx.Component:
    return rx.el.div(
        rx.el.button(
            "Cancel",
            on_click=ReportState.cancel_report,
            class_name="px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50",
        ),
        rx.el.div(
            rx.cond(
                ReportState.current_step > 1,
                rx.el.button(
                    "Previous",
                    on_click=ReportState.prev_step,
                    class_name="ml-3 px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50",
                ),
            ),
            rx.cond(
                ReportState.current_step < ReportState.total_steps,
                rx.el.button(
                    "Next Step",
                    on_click=ReportState.next_step,
                    class_name="ml-3 px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-teal-600 hover:bg-teal-700",
                ),
                rx.el.button(
                    rx.cond(
                        ReportState.report_id_being_edited,
                        "Update Report",
                        "Save Report",
                    ),
                    on_click=ReportState.save_report,
                    class_name="ml-3 px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-600 hover:bg-green-700",
                ),
            ),
            class_name="flex",
        ),
        class_name="flex justify-between mt-8 pt-4 border-t border-gray-200",
    )


def create_report_content() -> rx.Component:
    return rx.el.div(
        rx.cond(
            ReportState.report_id_being_edited,
            rx.el.div(
                rx.el.span(
                    "Editing Report #" + ReportState.report_id_being_edited,
                    class_name="font-bold text-teal-600 mr-2",
                ),
                class_name="mb-4 p-3 bg-teal-50 border border-teal-100 rounded-md text-sm",
            ),
        ),
        step_indicator(),
        rx.el.div(
            rx.cond(ReportState.current_step == 1, accident_info_step()),
            rx.cond(ReportState.current_step == 2, patient_status_step()),
            rx.cond(ReportState.current_step == 3, condition_assessment_step()),
            rx.cond(ReportState.current_step == 4, treatment_given_step()),
            rx.cond(ReportState.current_step == 5, media_upload_step()),
            rx.cond(ReportState.current_step == 6, review_summary_step()),
            class_name="bg-white p-6 rounded-lg shadow-sm border border-gray-200 min-h-[400px]",
        ),
        navigation_buttons(),
        class_name="max-w-3xl mx-auto",
    )


def create_report_page() -> rx.Component:
    return page_wrapper(create_report_content())