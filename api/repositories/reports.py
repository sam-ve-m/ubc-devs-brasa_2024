from api.repositories.abs.abs_mongo import AbstractRepository


class ReportsRepository(AbstractRepository):

    def get_user_reports(self, user_id: str, new: bool) -> list:
        mongo_filter = {"user_id": user_id}
        if new is not None:
            mongo_filter["new"] = new
        if reports := self.get_many_by_filter(mongo_filter):
            return reports
