import random

class Individual:
    def __init__(self):
        self.position = []      # Values
        self.quality = None
        self.bposition = []
        self.bquality = None
        self.velocity = 0

    def __str__(self):
        return f"Individual:\nPosition={self.position}\nQuality={self.quality} \tVelocity:{self.velocity}\nBest Po.={self.bposition}\nBest Quality={self.bquality})"

gbest = []
gquality = 0


def create_first(bound=5.12, p_size=20, dimension=10, function=sum):  # Returns the first population of solutions
    population = []

    for i in range(p_size):     #Number of individuals
        ind = Individual()
        for j in range(dimension):  #Dimension of an individual
            ind.position.append(round(random.uniform(- bound, bound), 4))   #Random position
            ind.bposition = ind.position.copy()
            ind.quality = function(ind.position)
            ind.bquality = ind.quality

        population.append(ind)

    update_global(population, function)

    return population


def update_global(population, function):

    global gquality
    global gbest

    for i in population:
        if i.bquality > gquality:
            gquality = i.bquality
            gbest = i.bposition









if __name__ == '__main__':

    population = create_first(p_size=2)

    for i in population:
        print(i)







