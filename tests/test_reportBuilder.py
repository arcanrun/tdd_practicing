import unittest
from interfaces.IreportBuilder import IreportBuilder
from app.special_report import SpecialReport
from app.reportBuilder import ReportBuilder


class ReportBuilderTest(unittest.TestCase):
    def setUp(self):
        self.reportBuilder = ReportBuilder()

    def test_if_method_return_correct_report(self):

        data = '#123123!'

        self.reportBuilder.buildReport(data)

        self.assertEqual(self.reportBuilder.buildReport(data), 'Atanttion!The new report: {}'.format(data))

    def test_if_method_return_correct_special_report(self):

        data = '0000'

        self.reportBuilder.buildSpecialReport(data)

        self.assertEqual(self.reportBuilder.buildSpecialReport(data), SpecialReport())