from interfaces.IreportSender import IreportSender


class ReportSender(IreportSender):
    def send(self, data):
        return 'Sending...{}'.format(data)