import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom, beta


def globe():
    grid = np.arange(0, 1, 0.001)

    uniform_prior = np.ones(1000)
    plot_posterior(grid, uniform_prior)

    beta_prior = beta.ppf(grid, 3, 2)
    plot_posterior(grid, beta_prior)

    plt.show()


def plot_posterior(grid, prior):
    p_data = binom.pmf(k=6, n=9, p=grid)

    posterior = p_data * prior
    posterior_normalised = posterior / sum(posterior)
    plt.plot(posterior_normalised)


if __name__ == '__main__':
    globe()
