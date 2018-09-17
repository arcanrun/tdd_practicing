import unittest
from unittest.mock import patch
from app.reporter import Reporter
from app.special_report import SpecialReport


class ReporterTest(unittest.TestCase):

    @patch('interfaces.IreportSender.IreportSender')
    @patch('interfaces.IreportBuilder.IreportBuilder')
    def setUp(self, BuilderMock, SenderMock):
        self.builder = BuilderMock()
        self.sender = SenderMock()
        self.reporter = Reporter(self.builder, self.sender)

    def test_return_numbers_of_sent_reports(self):
        # arrange
        self.builder.buildReport.return_value = (['first'], ['second'])
        # act
        reportCount = self.reporter.sendReports()
        # assert
        self.assertEqual(2, reportCount)

    def test_sender(self):
        # arrange
        self.builder.buildReport.return_value = (['1'], ['2'], ['3'])
        # act
        self.reporter.sendReports()
        # assert
        self.assertEqual(len(self.sender.send.call_args_list), 3)

    def test_special_report_to_administrator_if_no_reports_created(self):
        # arrange
        self.builder.buildReport.return_value = ()
        self.builder.buildSpecialReport.return_value = SpecialReport()
        # act
        self.reporter.sendReports()
        # assert
        self.assertEqual(self.sender.send.mock_calls[0][1][0].__class__.__name__, 'SpecialReport')