#''''
import random as rd
test_list = [rd.randint(10000, 100000) for x in range(30)] # random integer number generator
#test_list = [round((rd.uniform(1.0, 10.0)), 2) for x in range(10)] # random floating point number generator
test_list.sort()
print(test_list)
#'''
