import numpy as np

def logistic_growth(t, N0, r, K):
    return K / (1 + ((K - N0) / N0) * np.exp(-r * t))