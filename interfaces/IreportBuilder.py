import abc


class IreportBuilder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def buildReport(self):
        pass
