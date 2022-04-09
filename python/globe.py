import numpy as np
from scipy.stats import binom
import seaborn as sns
import matplotlib.pyplot as plt


def globe():
    grid = np.arange(0, 1, 0.001)
    prior = np.ones(1000)

    p_data = binom.pmf(k=6, n=9, p=grid)
    posterior = p_data * prior
    posterior_normalised = posterior / sum(posterior)
    plt.plot(posterior_normalised)
    plt.show()


if __name__ == '__main__':
    globe()
