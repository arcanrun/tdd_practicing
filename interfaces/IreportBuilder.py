import abc
from app.special_report import SpecialReport

class IreportBuilder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def buildReport(self):
        pass

    @abc.abstractmethod
    def buildSpecialReport(self, data=None)->SpecialReport():
        pass

