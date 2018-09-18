from interfaces.IreportBuilder import IreportBuilder
from app.special_report import SpecialReport


class ReportBuilder(IreportBuilder):
    def buildReport(self, data):
        return 'Atanttion!The new report: {}'.format(data)

    def buildSpecialReport(self, data):
        return SpecialReport()