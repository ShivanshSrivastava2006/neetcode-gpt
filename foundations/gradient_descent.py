class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: float) -> float:
        x = init
        if(iterations == 0):
            return round(x, 5)
        for _ in range(iterations):
            diff = 2 * x
            
            next_x = x - learning_rate * diff
            
            if round(next_x, 5) == round(x, 5):
                break
                
            x = next_x
            
        return float(round(x, 5))
