import random
import numpy as np
from shapely import Point, Polygon
from shapely.affinity import scale
from scipy.stats import norm
import matplotlib.pyplot as plt


"""
This class defines the ellipse which form the boundary"
"""
class Shape_Ellipse():

    def __init__(self, center, semi_major, semi_minor):

        self.center = Point(center[0], center[1])
        self.ellipse = scale(self.center.buffer(1), xfact=semi_major, yfact=semi_minor)

    """
    A line’s endpoints are part of its boundary and are therefore not contained.
    """
    def does_contain(self,point):

        return self.ellipse.contains(Point(point[0],point[1]))


    def plot(self):

        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.add_patch(plt.Polygon(list(self.ellipse.exterior.coords), alpha=0.5))
        ax.autoscale_view()
        plt.show()


"""
This class allows to run simulations for the problem
"""
class Simulation_Ellipse():

    def __init__(self, center, semi_major, semi_minor):

        self.position = [0,0]
        self.ellipse = Shape_Ellipse(center, semi_major, semi_minor)

    """
    Randomly update ant position
    """
    def get_next_position(self):

        dir = random.randint(0,3)

        curr_x = self.position[0]
        curr_y = self.position[1]

        if dir == 0:
            self.position = [curr_x + 10, curr_y]

        elif dir == 1:
            self.position = [curr_x - 10, curr_y]

        elif dir == 2:
            self.position = [curr_x, curr_y + 10]

        elif dir == 3:
            self.position = [curr_x, curr_y - 10]


    """
    Run a single simulation for a single ant and returns the number of steps taken.
    """
    def run_simulation(self):

        count = 0
        self.position = [0,0]

        while self.ellipse.does_contain(self.position):

            count += 1
            self.get_next_position()

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

    def plot(self):

        self.ellipse.plot()


"""
Define here the parameters of the Ellipse
"""
CENTER = [2.5,2.5]
semi_major = 30
semi_minor = 40
sim = Simulation_Ellipse(CENTER,semi_major,semi_minor)


"""
Define here the statistical parameters
"""
CONFIDENCE = 0.95
SAMPLES = 10000

sim.get_confidence_interval(CONFIDENCE, SAMPLES)
