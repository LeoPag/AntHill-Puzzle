import random
import numpy as np
from scipy.stats import norm

class Simulation(object):

    def __init__(self):
        return

    def get_next_state(self,state):

        dir = random.randint(0,3)

        #Start
        if state == 0:
            next_state = 1

        #Edge
        elif state == 1:
            if dir == 0:
                next_state = 0

            elif (dir == 1) or (dir == 2):
                next_state = 2

            elif (dir == 3):
                next_state = 3

        #Corner
        elif state == 2:

            if (dir == 0) or (dir == 1):
                next_state = 1

            elif (dir == 2) or (dir == 3):
                next_state = 3

        return next_state

    def run_simulation(self):

        count = 0
        current_state = 0

        while current_state != 3:

            current_state = self.get_next_state(current_state)
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


sim = Simulation()

"""
Define here the statistical parameters
"""
CONFIDENCE = 0.95
SAMPLES = 10000

sim.get_confidence_interval(CONFIDENCE, SAMPLES)
