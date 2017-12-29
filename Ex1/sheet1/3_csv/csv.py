import sys
from itertools import groupby

csv = sys.argv[1]
column = int(sys.argv[2])


def computeMeanCSV():
    data = []
    try:
        with open(csv) as f:
            csv_file = iter(f)
            next(f)
            for line in csv_file:
                data.append(line.split(",")[column])
        if(is_number(data[0])):
            mean(data)
        else:
            mode(data)
    except IndexError:
        print("Index is out of range")


def is_number(s):
    """checks is the string is a number
    (from https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float-in-python)"""
    try:
        float(s)
        return True
    except ValueError:
        return False


def mean(data):
    """computes the mean for numeric values"""
    floats = [float(s) for s in data]
    mean = sum(floats) / len(data)
    print("Mean of column %d: %f" % (column, mean))


def mode(data):
    """computes the mode for non-numeric values."""
    amounts = {k: len(list(v)) for k, v in groupby(sorted(data))}
    mode = max(amounts, key=amounts.get)
    print("Mode of column %d: %s (%d times in the data)" % (column, mode, amounts[mode]))


computeMeanCSV()
