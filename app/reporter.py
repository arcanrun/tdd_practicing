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
        return len(self.builder.buildReport())