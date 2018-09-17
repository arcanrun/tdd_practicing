import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from app.reporter import Reporter


class ReporterTest(unittest.TestCase):

    def setUp(self):
        pass

    @patch('interfaces.IreportSender.IreportSender')
    @patch('interfaces.IreportBuilder.IreportBuilder')
    def test_return_numbers_of_sent_reports(self, BuilderMock, SenderMock):
        builder = BuilderMock()
        sender = SenderMock()


        builder.buildReport.return_value = (['first'],['second'])
        sender.send.return_value = 'TEST'

        reporter = Reporter(builder, sender)

        reportCount = reporter.sendReports()

        self.assertEqual(2, reportCount)

