
    # Модули бывают самописные и с различных библиотек python

    # файлы hello и start для этого урока с функцией import

# def some():
#     print('Hello world')
# some()

# def some():
#     print('Hello')

# import math
# print(math.pi)

# import random
# r = random.randrange(0, 10)
# print(r)        # random integer 0-10

import random
r = random.randrange(0, 1000000)
user = 'User'
print(user + str(r))

from doc import math
print(math.pi)