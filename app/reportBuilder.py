from interfaces.IreportBuilder import IreportBuilder
from app.special_report import SpecialReport


class ReportBuilder(IreportBuilder):
    def __init__(self, data=[]):
        self.data = data
    def buildReport(self):
        return self.data

    def buildSpecialReport(self, data=None):
        return SpecialReport(data)