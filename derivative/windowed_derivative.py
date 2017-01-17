import numpy as np
import pylab as pl
from statsmodels.nonparametric.smoothers_lowess import lowess


def smooth_data(data):
    return lowess(data, np.linspace(0, len(data)-1, len(data)), is_sorted=True, frac=0.025, it=0)[:, 1]


def locate_zero_crossings(data):
    return np.where(np.diff(np.signbit(data)))[0]


def derivative(data, window_size_even=8):
    window_size = window_size_even
    data_derivative = np.zeros_like(data)

    for i in range(len(data)):
        end_i0 = i+window_size/2
        end_i1 = i+window_size
        if (end_i1 + 1) < (len(data)-1):
            sample0 = np.average(data[i:end_i0])
            sample1 = np.average(data[i+window_size/2:end_i1])
        else:
            sample0 = 0
            sample1 = 0
        data_derivative[i] = (sample1 - sample0)/window_size

    return data_derivative
