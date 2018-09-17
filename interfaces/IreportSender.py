import abc


class IreportSender(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def send(self):
        pass
