import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        z = z - np.max(z) 
        sum_expo = np.exp(z)
        result = sum_expo / sum_expo.sum()
        return np.round(result, 4)
