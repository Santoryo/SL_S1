import pickle
import time
import sys

start = time.time()


def load_data(file):
    """Handles the file and closes it"""
    try:
        datafile = open(file, 'rb')
        data = pickle.load(datafile)
        datafile.close
        return data
    except IOError as ioe:
        print(f"The file couldn't be located: {ioe}")
        sys.exit()


def max_subarray(numbers):
    """Find the largest sum in contiguous subarray."""
    highest_sum = 0
    sum = 0
    for num in numbers:
        sum = max(num, sum + num)
        highest_sum = max(highest_sum, sum)
    return highest_sum


def args():
    """Handles the arguments, so the program
    can be run with CLI only"""
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return "substr_1e5.pkl"


file = args()
data = load_data(file)
max_sum = max_subarray(data)
t = time.time()-start
print(len(data), t, max_sum)
