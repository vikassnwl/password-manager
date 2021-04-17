import csv


def read(fname):
    output = []
    with open(fname) as f:
        reader = csv.reader(f)
        for row in reader:
            output.append(row)
        return output
