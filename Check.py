class Check(object):
    def __init__ (self):
        self.array = []
        self.estadoInicial = []
    def fitness(self , array , estadoInicial):
        self.array = array
        self.estadoInicial = estadoInicial
        collisions = 0
        for i in range(1,9):
            if i not in self.array:
                print ("ERROR")
                return 0

        for i in range(0, 8):
            col = 0
            for j in range(0, 8):
                if i != j:
                    if abs(self.estadoInicial[i] - self.estadoInicial[j]) == abs(self.array[j] - self.array[i]):
                        col = 1
            if col == 1:
                collisions += 1
        return 8 - collisions
