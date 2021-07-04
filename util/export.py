from collections import OrderedDict
import csv

# Usage:
# with OutputCSV('data.csv', ['crn', 'restriction']) as out:
#   out.write_header()
#   out.insert(crn=13240, restriction="wheeeee")

class OutputCSV():
    def __init__(self, filename, fields):
        # fields is a list of fields
        self.file = None
        self.filename = filename
        self.fmt = OrderedDict.fromkeys(fields)
        self.writer = None

    def __enter__(self):
        self.file = open(self.filename, 'w')
        self.writer = csv.writer(self.file)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.file.close()
        self.writer = None

    def write_header(self):
        self.insert(**{ header: header for header in self.fmt})

    def insert(self, **kwargs):
        if self.fmt.keys() != kwargs.keys():
            raise TypeError("Bad entries!")
        self.fmt.update(kwargs.items())
        self.writer.writerow(self.fmt.values())
