import csv


def write(fname, mode, content):
    with open(fname, mode) as f:
        writer = csv.writer(f)
        writer.writerows(content)
