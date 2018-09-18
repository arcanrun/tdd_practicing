import unittest
from interfaces.IreportBuilder import IreportBuilder
from app.special_report import SpecialReport
from app.reportBuilder import ReportBuilder


class ReportBuilderTest(unittest.TestCase):
    def setUp(self):
        self.data = '#123123!'
        self.reportBuilder = ReportBuilder(self.data)

    def test_if_method_return_correct_report(self):
        # arrange Third_step
         # this data from DB, for example, so it requires Mock - object

        # act Second_step
        self.reportBuilder.buildReport()

        # assert First_step
        self.assertEqual(self.reportBuilder.buildReport(), 'Atanttion!The new report: {}'.format(self.data))

    def test_if_method_return_correct_special_report(self):

        data = 'SomeSPECIALdata'

        self.reportBuilder.buildSpecialReport(data)

        self.assertIsInstance(self.reportBuilder.buildSpecialReport(data), SpecialReport)

    def test_if_scpecial_report_gets_no_data(self):

        self.reportBuilder.buildSpecialReport()

        self.assertEqual(self.reportBuilder.buildSpecialReport().data, None)