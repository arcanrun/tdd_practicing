from interfaces.IreportBuilder import IreportBuilder
from app.special_report import SpecialReport


class ReportBuilder(IreportBuilder):
    def __init__(self, data=None):
        self.data = data
    def buildReport(self):
        return 'Atanttion!The new report: {}'.format(self.data)

    def buildSpecialReport(self, data=None):
        return SpecialReport(data)