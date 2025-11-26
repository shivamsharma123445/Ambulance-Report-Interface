import reflex as rx
from app.states.auth_state import AuthState
from app.states.report_state import ReportState


def delete_confirmation_dialog() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title("Delete Report"),
            rx.dialog.description(
                "Are you sure you want to delete this report? This action cannot be undone.",
                size="2",
                margin_bottom="4",
            ),
            rx.el.div(
                rx.dialog.close(
                    rx.el.button(
                        "Cancel",
                        class_name="bg-white border border-gray-300 text-gray-700 font-medium py-2 px-4 rounded-md hover:bg-gray-50 transition duration-200",
                    )
                ),
                rx.el.button(
                    "Delete",
                    on_click=ReportState.confirm_delete,
                    class_name="bg-red-600 text-white font-medium py-2 px-4 rounded-md hover:bg-red-700 transition duration-200",
                ),
                class_name="flex justify-end gap-3 mt-4",
            ),
            max_width="450px",
        ),
        open=ReportState.show_delete_dialog,
        on_open_change=ReportState.set_show_delete_dialog,
    )


def stat_card(title: str, value: str, icon_name: str, color_class: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p(title, class_name="text-sm font-medium text-gray-500 truncate"),
                rx.el.p(value, class_name="mt-1 text-3xl font-semibold text-gray-900"),
            ),
            rx.el.div(
                rx.icon(icon_name, class_name=f"h-8 w-8 {color_class}"),
                class_name=f"p-3 rounded-full bg-opacity-10 {color_class.replace('text-', 'bg-')}",
            ),
            class_name="flex items-center justify-between",
        ),
        class_name="bg-white overflow-hidden shadow rounded-lg p-5 border border-gray-100",
    )


def filter_bar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(
                    "search",
                    class_name="h-5 w-5 text-gray-400 absolute left-3 top-1/2 transform -translate-y-1/2",
                ),
                rx.el.input(
                    placeholder="Search patient or location...",
                    on_change=ReportState.set_search_query,
                    class_name="pl-10 block w-full rounded-md border-gray-300 shadow-sm focus:ring-teal-500 focus:border-teal-500 sm:text-sm py-2 border",
                    default_value=ReportState.search_query,
                ),
                class_name="relative flex-grow min-w-[200px]",
            ),
            rx.el.select(
                rx.el.option("All Types", value="All"),
                rx.el.option("Road Accident", value="Road"),
                rx.el.option("Fall", value="Fall"),
                rx.el.option("Fire", value="Fire"),
                rx.el.option("Other", value="Other"),
                value=ReportState.filter_accident_type,
                on_change=ReportState.set_filter_accident_type,
                class_name="block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-teal-500 focus:border-teal-500 sm:text-sm rounded-md border",
            ),
            rx.el.input(
                type="date",
                on_change=ReportState.set_filter_date_from,
                class_name="block w-full rounded-md border-gray-300 shadow-sm focus:ring-teal-500 focus:border-teal-500 sm:text-sm py-2 border px-3",
                placeholder="From Date",
                default_value=ReportState.filter_date_from,
            ),
            rx.el.input(
                type="date",
                on_change=ReportState.set_filter_date_to,
                class_name="block w-full rounded-md border-gray-300 shadow-sm focus:ring-teal-500 focus:border-teal-500 sm:text-sm py-2 border px-3",
                placeholder="To Date",
                default_value=ReportState.filter_date_to,
            ),
            rx.el.button(
                "Clear",
                on_click=ReportState.clear_filters,
                class_name="inline-flex items-center px-3 py-2 border border-gray-300 shadow-sm text-sm leading-4 font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-teal-500",
            ),
            class_name="grid grid-cols-1 md:grid-cols-5 gap-4 w-full",
        ),
        class_name="bg-white p-4 rounded-lg shadow-sm border border-gray-200 mb-6",
    )


def empty_dashboard() -> rx.Component:
    return rx.el.div(
        rx.el.p(
            f"Hello, {AuthState.current_user.name | 'User'}!",
            class_name="text-xl text-gray-700 mb-6",
        ),
        rx.el.div(
            stat_card(
                "Total Reports",
                ReportState.total_reports.to_string(),
                "clipboard-list",
                "text-teal-600",
            ),
            stat_card(
                "Last 7 Days",
                ReportState.recent_reports_count.to_string(),
                "calendar-days",
                "text-blue-600",
            ),
            stat_card(
                "Road Accidents",
                ReportState.road_accident_count.to_string(),
                "car",
                "text-teal-700",
            ),
            class_name="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8",
        ),
        filter_bar(),
        rx.el.div(
            rx.el.div(
                rx.el.button(
                    rx.icon("file-plus", class_name="h-8 w-8 text-teal-600 mb-3"),
                    rx.el.h3(
                        "Create New Report",
                        class_name="text-lg font-medium text-gray-900",
                    ),
                    rx.el.p(
                        "Start documenting a new accident response.",
                        class_name="mt-2 text-sm text-gray-500",
                    ),
                    class_name="block h-full",
                ),
                class_name="p-6 bg-white rounded-lg shadow-sm border border-gray-200 hover:border-teal-300 transition-colors cursor-pointer",
            ),
            rx.el.div(
                rx.icon("history", class_name="h-8 w-8 text-blue-600 mb-3"),
                rx.el.h3(
                    "View History", class_name="text-lg font-medium text-gray-900"
                ),
                rx.el.p(
                    "Access past accident reports and records.",
                    class_name="mt-2 text-sm text-gray-500",
                ),
                class_name="p-6 bg-white rounded-lg shadow-sm border border-gray-200 hover:border-blue-300 transition-colors cursor-pointer",
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
        ),
        class_name="bg-white p-8 rounded-xl shadow-sm border border-gray-100",
    )


def report_card(report: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    report["accident_type"],
                    class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-50 text-blue-700",
                ),
                rx.el.span(report["accident_date"], class_name="text-xs text-gray-500"),
                class_name="flex justify-between items-start mb-2",
            ),
            rx.el.h3(
                rx.cond(
                    report["patient_name"], report["patient_name"], "Unknown Patient"
                ),
                class_name="text-lg font-medium text-gray-900 truncate",
            ),
            rx.el.p(
                report["location"], class_name="text-sm text-gray-500 mb-4 truncate"
            ),
            rx.el.div(
                rx.el.a(
                    rx.el.button(
                        "View",
                        class_name="text-xs font-medium text-teal-600 hover:text-teal-500 bg-teal-50 px-2 py-1 rounded",
                    ),
                    href=f"/report/{report['id']}",
                ),
                rx.el.button(
                    "Edit",
                    on_click=lambda: ReportState.load_report_for_edit(report["id"]),
                    class_name="text-xs font-medium text-gray-600 hover:text-gray-500 bg-gray-100 px-2 py-1 rounded",
                ),
                rx.el.button(
                    "Delete",
                    on_click=lambda: ReportState.open_delete_dialog(report["id"]),
                    class_name="text-xs font-medium text-red-600 hover:text-red-500 bg-red-50 px-2 py-1 rounded",
                ),
                class_name="mt-auto pt-4 border-t border-gray-100 flex justify-end gap-2",
            ),
            class_name="flex flex-col h-full",
        ),
        class_name="bg-white p-5 rounded-lg shadow-sm border border-gray-200 hover:shadow-md transition-shadow",
    )


def dashboard_content() -> rx.Component:
    return rx.el.div(
        delete_confirmation_dialog(),
        rx.el.div(
            rx.el.h1("Dashboard", class_name="text-3xl font-bold text-gray-900"),
            rx.el.button(
                rx.icon("plus", class_name="h-4 w-4 mr-2"),
                "New Report",
                on_click=ReportState.start_new_report,
                class_name="inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-teal-600 hover:bg-teal-700",
            ),
            class_name="flex justify-between items-center mb-8",
        ),
        rx.cond(
            ReportState.reports.length() > 0,
            rx.el.div(
                stat_card(
                    "Total Reports",
                    ReportState.total_reports.to_string(),
                    "clipboard-list",
                    "text-teal-600",
                ),
                stat_card(
                    "Last 7 Days",
                    ReportState.recent_reports_count.to_string(),
                    "calendar-days",
                    "text-blue-600",
                ),
                stat_card(
                    "Road Accidents",
                    ReportState.road_accident_count.to_string(),
                    "car",
                    "text-teal-700",
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8",
            ),
        ),
        rx.cond(ReportState.reports.length() > 0, filter_bar()),
        rx.cond(
            ReportState.filtered_reports.length() > 0,
            rx.el.div(
                rx.foreach(ReportState.filtered_reports, report_card),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6",
            ),
            rx.cond(
                ReportState.reports.length() == 0,
                empty_dashboard(),
                rx.el.div(
                    rx.el.p(
                        "No reports match your filters.",
                        class_name="text-gray-500 text-center py-10",
                    ),
                    class_name="bg-white rounded-lg shadow-sm border border-gray-200 p-8",
                ),
            ),
        ),
        class_name="animate-fade-in",
    )