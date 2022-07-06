#SAKSHAM PATEL
#ROLL NO-32
#PROGRAM ON BINOMIAL PROBABILITY DISTRIBUTION
import matplotlib.pyplot as plt
import numpy as np

#fixing the seed for reproducibility
#of the result
np.random.seed(10)

size = 10000
#drawing 10000 sample from
#binomial distribution
sample = np.random.binomial(20, 0.5, size)
bin = np.arange(0,20,1)

plt.hist(sample, bins=bin, edgecolor='blue')
plt.title("Binomial Distribution")
plt.show()