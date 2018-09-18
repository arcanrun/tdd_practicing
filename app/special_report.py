class SpecialReport:
    def __init__(self, data=None):
        self.data = data

    def __str__(self):
        return 'SPECIAL REPORT: ' + str(self.data)

    def __repr__(self):
        return 'SPECIAL REPORT!'