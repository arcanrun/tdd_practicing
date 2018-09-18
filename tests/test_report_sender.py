import unittest
from app.report_sender import ReportSender

class ReportSenderTest(unittest.TestCase):

    def setUp(self):
        self.sender = ReportSender()

    def test_sending_reprot(self):

        data = '[DATA]'

        self.sender.send(data)

        self.assertEqual(self.sender.send(data), 'Sending...{}'.format(data))