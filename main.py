"""- Hay que guardar la mejor solucion
- Cada individuo tiene memoria de donde obtuvo la mejor solucion.
Parametros: posicion, calidad, best_position, best_quality"""

class Individual:
    def __init__(self):
        self.position = []      # Values
        self.quality = None
        self.bposition = []
        self.bquality = None

    def __str__(self):
        return f"Individual:\nPosition={self.position}\nQuality={self.quality}\nBest Po.={self.bposition}\nBest Quality={self.bquality})"

gbest = []
gquality = None


















