import random
import matplotlib.pylab as plb


dist = []
num_samples = 1000000

for i in range(num_samples):
    # first parameter mean, second std dev
    dist.append(random.gauss(0, 100))

weights = [1/num_samples]*len(dist)
v =  plb.hist(dist, bins=100, weights=weights)

plb.xlabel('x')
plb.ylabel('Relative Frequency')

print(f'fraction within approx 200 of mean = {sum(v[0][30:70])}')

plb.show()