import math
import random
import numpy as np


class ObjFunction:

    def sphere(self, vector):

        sum = 0

        for e in vector:
            sum += pow(e, 2)

        return 1 / (1 + sum)    # Inverse. Cause we wanna found the minimum

    def schwefel(self, vector):

        v1 = 4189.829   # Already multiplied for d=10
        sum = 0

        for e in vector:
            sum += e * math.sin(pow(abs(e), 0.5))

        result = v1 - sum

        return 1 / (1 + result)   # Inverse. Cause we wanna found the minimum


    def rastrigin(self, vector):

        v1 = 100    # 10 * d
        sum = 0

        for e in vector:
            sum += pow(e, 2) - 10 * math.cos(2 * math.pi * e)

        result = v1 + sum

        return 1 / (1 + result)   # Inverse. Cause we wanna found the minimum

class Individual:
    def __init__(self, dimension=10):
        self.position = np.zeros(dimension)
        self.quality = None
        self.bposition = np.zeros(dimension)
        self.bquality = None
        self.velocity = np.zeros(dimension)     # Initialize the velocity vector to 0

    def __str__(self):
        return f"Individual:\nPosition={self.position}\nQuality={self.quality} \tVelocity:{self.velocity}\nBest Po.={self.bposition}\nBest Quality={self.bquality})"

gbest = np.zeros(0)
gquality = 0


def create_first(bound, p_size, dimension, function):  # Returns the first population of solutions
    population = []

    for i in range(p_size):     #Number of individuals
        ind = Individual(dimension)

        ind.position = np.random.uniform(-bound, bound, dimension)
        ind.bposition = ind.position.copy()
        ind.quality = function(ind.position)
        ind.bquality = ind.quality

        population.append(ind)

    update_global(population)

    return population


def update_global(population):
    global gquality
    global gbest

    for i in population:
        if i.bquality > gquality:
            gquality = i.bquality
            gbest = i.bposition.copy()


def weight(iter, itotal, wstart=0.9, wend=0.4):     #iter: current iteration   itotal: total number of iterations
    return wstart - (((wstart - wend) * iter) / itotal)


def new_position(ind, bound, function):       #Updates the position and quality of the individual
    ind.position += ind.velocity
    ind.position = np.round(np.clip(ind.position, -bound, bound), decimals=4)
    ind.quality = function(ind.position)

def update_velocity(ind, weight, bound, c1=1.49618, c2=1.49618):
    global gbest

    s1 = weight * ind.velocity
    s2 = c1 * np.random.rand() * (ind.bposition - ind.position)
    s3 = c2 * np.random.rand() * (gbest - ind.position)

    new_velocity = s1 + s2 + s3
    ind.velocity = np.clip(new_velocity, -0.2*bound, 0.2*bound)


def pso(bound=5.12, p_size=20, dimension=10, function=sum, iterations=1000):
    global gbest
    global gquality
    history = []

    population = create_first(bound, p_size, dimension, function)   #Create the initial population
    history.append(gquality)

    for i in range(iterations):

        for ind in population:          #For each individual
            #print("Current individual's position: ", ind.position, "Quality: ", ind.quality, "Vel: ", ind.velocity)
            w = weight(i, iterations)
            update_velocity(ind, w, bound)  #Update the velocity
            new_position(ind, bound, function)        #Update the position and quality

            if ind.quality > ind.bquality:  #Update the individual's best
                ind.bquality = ind.quality
                ind.bposition = ind.position.copy()

        update_global(population)       #Update global best and global quality
        history.append(gquality)
        #print(f"{i}\t BestQuality = {gquality}")

    #Return the best solution found
    return gbest, gquality, history





if __name__ == '__main__':

    f = ObjFunction()

    best, quality, history = pso(bound=5.12, p_size=20, function=f.sphere, iterations=1000)

    print("Best: ", best)
    print("Quality: ", quality)
    print(history)











