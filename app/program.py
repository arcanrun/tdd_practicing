from app.reporter import Reporter
from app.report_sender import ReportSender
from app.reportBuilder import ReportBuilder





if __name__ == '__main__':
    sender = ReportSender()
    builder = ReportBuilder([1])

    reporter = Reporter(builder, sender)
    print(reporter.sendReports())