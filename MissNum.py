<<<<<<< HEAD
<<<<<<< HEAD
def miss_func_num(iter):
    return [x for x in range(lst[0], lst[-1]+1)
                               if x not in iter]

# Driver code
iter = [0, 1, 2, 4, 5, 6]
miss = miss_func_num(iter)
for i in miss:
    print(i)
#print(miss)
=======
iter = [0,1,2,4,5,6,8,9]
>>>>>>> ea535d5f2d362128422ecd2c4fdbf48f6b846149
def miss_num_func():
    return [x for x in range(iter[0], iter[-1]+1)
                                if x not in iter]

print(miss_num_funct(iter))
>>>>>>> 478a3b7c3cc5c5e82136935595c679a077b1f535
=======
=======
<<<<<<< HEAD
>>>>>>> 68d7dd20d5297c4671f175d03a0d6fb32ebfb2b1
"""
This file is part of the github course W2 task
"""
import numpy as np

iter = [0, 1, 2, 4, 5, 6, 8, 9]
def miss_num_func(iter):
    '''
    This function takes in a list called "iter" with items in serial order,
    and returns the missing item.
    1. Make another list called "compare" with the biggest item in iter list as the final item
    2. Compare "compare" with "iter", and returns the missing item
    '''
    n = iter[-1]
    compare = np.arange(0, n+1, 1).tolist()
    same_index = []
    for i in range(len(iter)):
        for j in range(len(compare)):
            if iter[i] == compare[j]:
                same_index.append(j)
    all_index = list(range(0, n+1))
    lis_dif = [i for i in all_index if i not in same_index]

    item = []
    for i in range(len(lis_dif)):
        item.append(compare[lis_dif[i]])

    return item

miss = miss_num_func(iter)

miss
<<<<<<< HEAD
>>>>>>> 754c5963d52b7f35ac340377aed974049123b36b
=======
=======
=======
>>>>>>> 50a546aa2d4be86bdbde870a452fff9b9c45c8bb
def miss_func_num(iter):
    return [x for x in range(lst[0], lst[-1]+1)
                               if x not in iter]

# Driver code
iter = [0, 1, 2, 4, 5, 6]
miss = miss_func_num(iter)
for i in miss:
    print(i)
#print(miss)
<<<<<<< HEAD
>>>>>>> 1a0e1ec27b773629fa1e3a38e16f7d321aebc87b
=======
=======
iter = [0,1,2,4,5,6,8,9]
>>>>>>> ea535d5f2d362128422ecd2c4fdbf48f6b846149
def miss_num_func():
    return [x for x in range(iter[0], iter[-1]+1)
                                if x not in iter]

print(miss_num_funct(iter))
>>>>>>> 478a3b7c3cc5c5e82136935595c679a077b1f535
>>>>>>> 50a546aa2d4be86bdbde870a452fff9b9c45c8bb
>>>>>>> 68d7dd20d5297c4671f175d03a0d6fb32ebfb2b1
