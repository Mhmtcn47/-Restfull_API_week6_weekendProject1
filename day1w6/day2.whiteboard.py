def crashing_weights(weights):
    
        for row in range(len(weights)):
            for i in range(len(weights[row])):
                if row < len(weights)-1 and weights[row][i] > weights[row + 1][i]:
                        weights[row + 1][i] = weights[row + 1][i] ++ weights[row][i]
        return weights[row]