from interfaces.IreportSender import IreportSender


class ReportSender(IreportSender):
    def send(self, data):
        print('Sending...{}'.format(data))
        return 'Sending...{}'.format(data)