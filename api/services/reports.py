from api.repositories.reports import ReportsRepository


class UserService:

    def __init__(self, report_repository: ReportsRepository):
        self.report_repository = report_repository

    def get_report_reports(self, report_id: str, new: bool) -> list:
        return self.report_repository.get_report_reports()
