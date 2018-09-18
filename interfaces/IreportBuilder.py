import abc
from app.special_report import SpecialReport

class IreportBuilder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def buildReport(self, data):
        pass

    @abc.abstractmethod
    def buildSpecialReport(self, data)->SpecialReport():
        pass

