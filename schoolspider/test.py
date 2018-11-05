import random

import time

random.seed(time.time())
for i in range(100):
    print(random.randrange(100000, 1000000))
