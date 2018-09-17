from interfaces.IreportSender import IreportSender
from interfaces.IreportBuilder import IreportBuilder

class Reporter:
    """
    Reporter controls

    And returns sent reports

    """
    def __init__(self, builder: IreportBuilder, sender: IreportSender):
        self.builder = builder
        self.sender = sender

    def sendReports(self):

        reports = self.builder.buildReport()
        if len(reports) == 0:
            self.sender.send(self.builder.buildSpecialReport())
        for report in reports:
            self.sender.send(report)
        return len(reports)