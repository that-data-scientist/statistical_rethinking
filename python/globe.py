import matplotlib.pyplot as plt
import numpy as np
import numpy.random
from scipy.stats import binom, beta


def globe():
    grid = np.arange(0, 1, 0.001)

    uniform_prior = np.ones(1000)
    posterior_uniform_prior = plot_posterior(grid, uniform_prior)

    beta_prior = beta.ppf(grid, 3, 2)
    posterior_beta_prior = plot_posterior(grid, beta_prior)
    plt.show()

    samples = numpy.random.choice(grid, p=posterior_beta_prior, size=1000)
    posterior_predictive = binom.rvs(n=9, p=samples, size=1000)
    plt.hist(posterior_predictive)
    plt.show()


def plot_posterior(grid, prior):
    p_data = binom.pmf(k=6, n=9, p=grid)

    posterior = p_data * prior
    posterior_normalised = posterior / sum(posterior)
    plt.plot(posterior_normalised)

    return posterior_normalised


if __name__ == '__main__':
    globe()
