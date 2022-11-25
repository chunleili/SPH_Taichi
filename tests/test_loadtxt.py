import numpy as np
import sys

sys.path.append(".")

def test_loadtxt():
    data = np.loadtxt('./test_data_input_nsearch.csv',dtype=float)
    print(data)
    print(data.shape)
    print(data[1][1])
if __name__ == '__main__':
    test_loadtxt()