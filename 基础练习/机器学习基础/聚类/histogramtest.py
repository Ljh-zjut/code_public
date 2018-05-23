import numpy as np
import pylab as pl
# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
mu, sigma = 2, 0.5
v = np.random.normal(mu,sigma,10000)
# Plot a normalized histogram with 50 bins
pl.hist(v, bins=50, density=1)       # matplotlib version (plot)
pl.show()
(n, bins) = np.histogram(v, bins=50, density=True)  # NumPy version (no plot)
pl.plot(.5*(bins[1:]+bins[:-1]), n)
pl.show()