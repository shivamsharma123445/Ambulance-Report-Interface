import reflex as rx
from typing import Optional
import datetime
import logging


class ReportState(rx.State):
    current_step: int = 1
    total_steps: int = 6
    location: str = ""
    accident_type: str = "Road"
    accident_date: str = datetime.date.today().isoformat()
    accident_time: str = datetime.datetime.now().strftime("%H:%M")
    patient_count: int = 1
    is_patient_speaking: bool = True
    patient_name: str = ""
    patient_age: str = ""
    patient_gender: str = "Male"
    patient_contact: str = ""
    patient_allergies: str = ""
    patient_history: str = ""
    est_patient_age: str = ""
    est_patient_gender: str = "Male"
    consciousness_level: str = "Alert"
    injury_head: bool = False
    injury_chest: bool = False
    injury_abdomen: bool = False
    injury_legs: bool = False
    injury_arms: bool = False
    injury_spine: bool = False
    injury_burns: bool = False
    reports: list[dict] = []
    breathing_status: str = "Normal"
    bleeding_status: bool = False
    bleeding_description: str = ""
    pain_level: int = 0
    chief_complaint: str = ""
    treatment_oxygen: bool = False
    treatment_bandage: bool = False
    treatment_iv: bool = False
    treatment_cpr: bool = False
    treatment_neck_collar: bool = False
    treatment_splint: bool = False
    treatment_other: str = ""
    uploaded_photos: list[str] = []
    is_uploading: bool = False
    search_query: str = ""
    filter_accident_type: str = "All"
    filter_date_from: str = ""
    filter_date_to: str = ""
    report_id_being_edited: Optional[str] = None
    show_delete_dialog: bool = False
    report_id_to_delete: str = ""

    @rx.var
    def total_reports(self) -> int:
        return len(self.reports)

    @rx.var
    def recent_reports_count(self) -> int:
        today = datetime.date.today()
        week_ago = today - datetime.timedelta(days=7)
        count = 0
        for r in self.reports:
            try:
                r_date = datetime.datetime.strptime(
                    r["accident_date"], "%Y-%m-%d"
                ).date()
                if week_ago <= r_date <= today:
                    count += 1
            except ValueError as e:
                logging.exception(f"Error parsing date: {e}")
        return count

    @rx.var
    def road_accident_count(self) -> int:
        return len([r for r in self.reports if r["accident_type"] == "Road"])

    @rx.var
    def filtered_reports(self) -> list[dict]:
        filtered = self.reports
        if self.search_query:
            query = self.search_query.lower()
            filtered = [
                r
                for r in filtered
                if query in r.get("location", "").lower()
                or query in r.get("patient_name", "").lower()
                or query in r.get("patient_contact", "").lower()
            ]
        if self.filter_accident_type != "All":
            filtered = [
                r for r in filtered if r["accident_type"] == self.filter_accident_type
            ]
        if self.filter_date_from:
            filtered = [
                r for r in filtered if r["accident_date"] >= self.filter_date_from
            ]
        if self.filter_date_to:
            filtered = [
                r for r in filtered if r["accident_date"] <= self.filter_date_to
            ]
        return filtered

    @rx.var
    def current_report_detail(self) -> dict:
        report_id = self.router.page.params.get("id")
        if not report_id:
            return {}
        for r in self.reports:
            if r["id"] == report_id:
                return r
        return {}

    @rx.event
    def set_search_query(self, value: str):
        self.search_query = value

    @rx.event
    def set_filter_accident_type(self, value: str):
        self.filter_accident_type = value

    @rx.event
    def set_filter_date_from(self, value: str):
        self.filter_date_from = value

    @rx.event
    def set_filter_date_to(self, value: str):
        self.filter_date_to = value

    @rx.event
    def clear_filters(self):
        self.search_query = ""
        self.filter_accident_type = "All"
        self.filter_date_from = ""
        self.filter_date_to = ""

    @rx.event
    def set_breathing_status(self, value: str):
        self.breathing_status = value

    @rx.event
    def toggle_bleeding_status(self, value: bool):
        self.bleeding_status = value

    @rx.event
    def set_bleeding_description(self, value: str):
        self.bleeding_description = value

    @rx.event
    def set_pain_level(self, value: int):
        self.pain_level = int(value)

    @rx.event
    def set_chief_complaint(self, value: str):
        self.chief_complaint = value

    @rx.event
    def set_treatment_oxygen(self, value: bool):
        self.treatment_oxygen = value

    @rx.event
    def set_treatment_bandage(self, value: bool):
        self.treatment_bandage = value

    @rx.event
    def set_treatment_iv(self, value: bool):
        self.treatment_iv = value

    @rx.event
    def set_treatment_cpr(self, value: bool):
        self.treatment_cpr = value

    @rx.event
    def set_treatment_neck_collar(self, value: bool):
        self.treatment_neck_collar = value

    @rx.event
    def set_treatment_splint(self, value: bool):
        self.treatment_splint = value

    @rx.event
    def set_treatment_other(self, value: str):
        self.treatment_other = value

    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle photo uploads."""
        for file in files:
            upload_data = await file.read()
            upload_dir = rx.get_upload_dir()
            upload_dir.mkdir(parents=True, exist_ok=True)
            import uuid

            file_ext = file.name.split(".")[-1] if "." in file.name else "jpg"
            unique_name = f"{uuid.uuid4()}.{file_ext}"
            file_path = upload_dir / unique_name
            with file_path.open("wb") as f:
                f.write(upload_data)
            self.uploaded_photos.append(unique_name)

    @rx.event
    def remove_photo(self, filename: str):
        """Remove a photo from the list."""
        self.uploaded_photos.remove(filename)

    @rx.event
    def save_report(self):
        """Save the completed report."""
        is_edit = self.report_id_being_edited is not None
        if is_edit:
            report_id = self.report_id_being_edited
            created_at = datetime.datetime.now().isoformat()
            for r in self.reports:
                if r["id"] == report_id:
                    created_at = r.get("created_at", created_at)
                    break
        else:
            report_id = str(len(self.reports) + 1)
            created_at = datetime.datetime.now().isoformat()
        report_data = {
            "id": report_id,
            "created_at": created_at,
            "location": self.location,
            "accident_type": self.accident_type,
            "accident_date": self.accident_date,
            "accident_time": self.accident_time,
            "patient_count": self.patient_count,
            "is_patient_speaking": self.is_patient_speaking,
            "patient_name": self.patient_name,
            "patient_age": self.patient_age,
            "patient_gender": self.patient_gender,
            "patient_contact": self.patient_contact,
            "patient_allergies": self.patient_allergies,
            "patient_history": self.patient_history,
            "est_patient_age": self.est_patient_age,
            "est_patient_gender": self.est_patient_gender,
            "consciousness_level": self.consciousness_level,
            "injuries": {
                "head": self.injury_head,
                "chest": self.injury_chest,
                "abdomen": self.injury_abdomen,
                "legs": self.injury_legs,
                "arms": self.injury_arms,
                "spine": self.injury_spine,
                "burns": self.injury_burns,
            },
            "assessment": {
                "breathing": self.breathing_status,
                "bleeding": self.bleeding_status,
                "bleeding_desc": self.bleeding_description,
                "pain": self.pain_level,
                "complaint": self.chief_complaint,
            },
            "treatment": {
                "oxygen": self.treatment_oxygen,
                "bandage": self.treatment_bandage,
                "iv": self.treatment_iv,
                "cpr": self.treatment_cpr,
                "neck_collar": self.treatment_neck_collar,
                "splint": self.treatment_splint,
                "other": self.treatment_other,
            },
            "photos": self.uploaded_photos,
        }
        if is_edit:
            for i, r in enumerate(self.reports):
                if r["id"] == report_id:
                    self.reports[i] = report_data
                    break
            msg = "Report updated successfully!"
        else:
            self.reports.append(report_data)
            msg = "Report saved successfully!"
        self.reset_form()
        self.current_step = 1
        return (rx.toast.success(msg), rx.redirect("/"))

    @rx.event
    def load_report_for_edit(self, report_id: str):
        """Load a report into the form for editing."""
        target_report = None
        for r in self.reports:
            if r["id"] == report_id:
                target_report = r
                break
        if not target_report:
            return rx.toast.error("Report not found")
        self.report_id_being_edited = report_id
        self.location = target_report.get("location", "")
        self.accident_type = target_report.get("accident_type", "Road")
        self.accident_date = target_report.get("accident_date", "")
        self.accident_time = target_report.get("accident_time", "")
        self.patient_count = target_report.get("patient_count", 1)
        self.is_patient_speaking = target_report.get("is_patient_speaking", True)
        self.patient_name = target_report.get("patient_name", "")
        self.patient_age = target_report.get("patient_age", "")
        self.patient_gender = target_report.get("patient_gender", "Male")
        self.patient_contact = target_report.get("patient_contact", "")
        self.patient_allergies = target_report.get("patient_allergies", "")
        self.patient_history = target_report.get("patient_history", "")
        self.est_patient_age = target_report.get("est_patient_age", "")
        self.est_patient_gender = target_report.get("est_patient_gender", "Male")
        self.consciousness_level = target_report.get("consciousness_level", "Alert")
        injuries = target_report.get("injuries", {})
        self.injury_head = injuries.get("head", False)
        self.injury_chest = injuries.get("chest", False)
        self.injury_abdomen = injuries.get("abdomen", False)
        self.injury_legs = injuries.get("legs", False)
        self.injury_arms = injuries.get("arms", False)
        self.injury_spine = injuries.get("spine", False)
        self.injury_burns = injuries.get("burns", False)
        assessment = target_report.get("assessment", {})
        self.breathing_status = assessment.get("breathing", "Normal")
        self.bleeding_status = assessment.get("bleeding", False)
        self.bleeding_description = assessment.get("bleeding_desc", "")
        self.pain_level = assessment.get("pain", 0)
        self.chief_complaint = assessment.get("complaint", "")
        treatment = target_report.get("treatment", {})
        self.treatment_oxygen = treatment.get("oxygen", False)
        self.treatment_bandage = treatment.get("bandage", False)
        self.treatment_iv = treatment.get("iv", False)
        self.treatment_cpr = treatment.get("cpr", False)
        self.treatment_neck_collar = treatment.get("neck_collar", False)
        self.treatment_splint = treatment.get("splint", False)
        self.treatment_other = treatment.get("other", "")
        self.uploaded_photos = target_report.get("photos", [])
        self.current_step = 1
        return rx.redirect("/create-report")

    @rx.event
    def open_delete_dialog(self, report_id: str):
        self.report_id_to_delete = report_id
        self.show_delete_dialog = True

    @rx.event
    def set_show_delete_dialog(self, value: bool):
        self.show_delete_dialog = value
        if not value:
            self.report_id_to_delete = ""

    @rx.event
    def confirm_delete(self):
        if self.report_id_to_delete:
            self.reports = [
                r for r in self.reports if r["id"] != self.report_id_to_delete
            ]
            rx.toast.success("Report deleted successfully")
        self.show_delete_dialog = False
        self.report_id_to_delete = ""

    @rx.event
    def start_new_report(self):
        self.reset_form()
        self.current_step = 1
        return rx.redirect("/create-report")

    @rx.event
    def set_accident_type(self, value: str):
        self.accident_type = value

    @rx.event
    def set_patient_gender(self, value: str):
        self.patient_gender = value

    @rx.event
    def set_est_patient_gender(self, value: str):
        self.est_patient_gender = value

    @rx.event
    def set_consciousness_level(self, value: str):
        self.consciousness_level = value

    @rx.event
    def toggle_speaking_status(self, value: bool):
        self.is_patient_speaking = value

    @rx.event
    def next_step(self):
        if self.current_step < self.total_steps:
            self.current_step += 1

    @rx.event
    def prev_step(self):
        if self.current_step > 1:
            self.current_step -= 1

    @rx.event
    def cancel_report(self):
        self.current_step = 1
        self.reset_form()
        return rx.redirect("/")

    @rx.event
    def reset_form(self):
        self.report_id_being_edited = None
        self.location = ""
        self.accident_type = "Road"
        self.patient_count = 1
        self.is_patient_speaking = True
        self.patient_name = ""
        self.patient_age = ""
        self.patient_gender = "Male"
        self.patient_contact = ""
        self.patient_allergies = ""
        self.patient_history = ""
        self.est_patient_age = ""
        self.est_patient_gender = "Male"
        self.consciousness_level = "Alert"
        self.injury_head = False
        self.injury_chest = False
        self.injury_abdomen = False
        self.injury_legs = False
        self.injury_arms = False
        self.injury_spine = False
        self.injury_burns = False
        self.breathing_status = "Normal"
        self.bleeding_status = False
        self.bleeding_description = ""
        self.pain_level = 0
        self.chief_complaint = ""
        self.treatment_oxygen = False
        self.treatment_bandage = False
        self.treatment_iv = False
        self.treatment_cpr = False
        self.treatment_neck_collar = False
        self.treatment_splint = False
        self.treatment_other = ""
        self.uploaded_photos = []