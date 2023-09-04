import os
import numpy as np

def test():
    int_rand = np.random.randint(3, size = 10)
    return int_rand


dict_test = {
    '1' : test(),
    '2' : test(),
}

list_test = [
    test(),
    test(),
]

for test_ in dict_test:
    
    test__ = dict_test[test_]
    print(test_)
    print(test__)


for test_ in list_test:
    
    print(test_)