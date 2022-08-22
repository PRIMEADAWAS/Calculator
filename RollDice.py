import random
import numpy as np
sum = 0
for round in range(20000):
    number = [1, 2, 3, 4, 5, 6]
    attempt = 1
    while attempt:
        rollDice = random.randint(0, 6)
        # print(rollDice)
        number[rollDice-1] = 0
        if(number == [0, 0, 0, 0, 0, 0]):
            # print('all zero', i, round)
            sum += attempt
            number = [1, 2, 3, 4, 5, 6]
            break
        attempt += 1
print('Average : ', (sum/(round+1)))
