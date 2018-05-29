# Lesson 13, Quizzes 17-34

import numpy as np

# NumPy arrays are great for doing math operations over every element
data = np.array([33219,36254,38801,46335,46840,47596,55130,56863,78070,88830])

mean = np.mean(data) # calculate the mean
print('The mean is {:g}'.format(mean), '\n')

devs = data - mean # deviations from the mean
print(devs, '\n')

avg_dev = np.sum(devs)/len(data) # calculate the average deviation

# the number we get is practically zero
print('The average deviation equals {:.15f}'.format(avg_dev), '\n')

abs_devs = np.absolute(devs) # convert to absolute values
print(abs_devs, '\n')

avg_absdev = np.sum(abs_devs)/len(data)
print('The average absolute deviation equals {:.2f}'.format(avg_absdev), '\n')

sq_devs = devs**2 # calculate squared deviations
print(sq_devs, '\n')

variance = np.sum(sq_devs)/len(data)
print('The average squared deviation (variance) equals {:.2f}'.format(variance), '\n')

print('The standard deviation equals {:.2f}'.format(np.sqrt(variance)), '\n')



# What if we write a function?

def calculate_std(array):
    """This function takes in data in the form of a NumPy array and returns
    its standard deviation
    """
    mean = np.mean(array)
    devs = array - mean
    sq_devs = devs**2
    variance = np.sum(sq_devs)/len(array)
    std = np.sqrt(variance)
    return std

# the dataset from Quiz: SD Social Networkers
sna_data = np.array([38946,43420,49191,50430,50557,52580,53595,54135,60181,62076])

result = calculate_std(sna_data)
print('The standard deviation equals {:.2f}'.format(result), '\n')

# How did we do?
# We can check if our calculations are correct by using NumPy's built-in function that computes std -

print('The standard deviation equals {:.2f}'.format(np.std(sna_data)), '\n')


# Quiz: Spreadsheet SD

from numpy import genfromtxt

salaries = genfromtxt('SNA_salaries.csv', delimiter = ',')
print(salaries, '\n')

salaries = salaries[~np.isnan(salaries)] # remove NaNs
print(salaries, '\n')

SNA_std = calculate_std(salaries)
print('The standard deviation equals {:.2f}'.format(SNA_std), '\n')



# Bessel's Correction

sample = np.array([18,21,15,18,17,21,22,23,20])

# calculate standard deviation for the sample data; modify the calculate_std() function
# if you want to get an estimate for the population standard deviation
