import random
import numpy as np
from scipy.stats import norm

class Simulation():

    def __init__(self,p):

        self.p = p


    """
    Run a single simulation for a single ant and returns the number of steps taken.
    """
    def run_simulation(self):

        curr_dist = 1
        count = 0

        while curr_dist != 0:

            dir = np.random.choice([-1,1], p = [self.p, 1-self.p])
            curr_dist += dir
            count += 1

        return count


    """
    Compute a confidence interval for the mean of the population
    """
    def get_confidence_interval(self, confidence, n):

        "Store observations"
        observations = []
        for i in range(n):
            observations.append(self.run_simulation())

        """
        Compute sample mean and sample_variance
        """
        sample_mean = sum(observations) / n

        sample_variance = 0
        for i in range(n):
            sample_variance += (observations[i] - sample_mean) ** 2
        sample_variance = sample_variance / (n - 1)

        z_alpha_halved = norm.ppf((1-confidence) / 2 + confidence, loc=0, scale=1)

        print("The ", confidence*100, "% confidence interval for the mean of the population is: [",
                sample_mean - z_alpha_halved * (np.sqrt(sample_variance) /  np.sqrt(n)) ,
                sample_mean + z_alpha_halved * (np.sqrt(sample_variance) /  np.sqrt(n)),
                "]")



"""
Define here the probability p of moving towards the food
"""
p = 2/3
sim = Simulation(p)


"""
Define here the statistical parameters
"""
CONFIDENCE = 0.95
SAMPLES = 10000

sim.get_confidence_interval(CONFIDENCE, SAMPLES)
