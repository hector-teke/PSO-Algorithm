

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
gquality = None


















