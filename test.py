import pandas as pd
import numpy as np
from BinomialModel.main import Binomial, probability
import matplotlib.pyplot as plt

file = pd.read_csv('QueryResult.csv')
df = pd.DataFrame(file)
ages = np.array(df['idade'])
print(ages)
prob_age_35 = probability(35, ages)
prob_age_65 = probability(65, ages)
print(prob_age_35 * 100)
binomial = Binomial(365, 3, prob_age_35)
print(
    f'In the year 2020, the probability of a 35-year-old person purchasing the medicine AZITHROMYCIN DI-HYDRATE three times in a year in Brasília-DF'
    f'was equal to  '
    f'{binomial.BinomialProbability():.2f}%')
print(prob_age_65 * 100)
binomial = Binomial(365, 3, prob_age_65)
print(
    f'In the year 2020, the probability of a 65-year-old person purchasing the medicine AZITHROMYCIN DI-HYDRATE three times in a year in Brasília-DF'
    f'was equal to  '
    f'{binomial.BinomialProbability():.2f}%')

# Binomial distribution
r = list(range(1, 365 + 1))
distribution_a = []
for k in r:
    binomial = Binomial(365, k, prob_age_35)
    distribution_a.append(binomial.BinomialProbability())
print(f'Distribution of 35-years-old person : \n{distribution_a}')
plt.bar(r, distribution_a)
distribution_b = []
for k in r:
    binomial = Binomial(365, k, prob_age_65)
    distribution_b.append(binomial.BinomialProbability())
print(f'Distribution of 65-years-old person : \n{distribution_b}')
fig, ax = plt.subplots()
plt.bar(r, distribution_a)
plt.bar(r, distribution_b)
ax.legend(['35-years old', '65-years old'])
plt.xlabel('n = Number experiments (days)')
plt.ylabel('probability (%)')
plt.savefig('distribution.png')
plt.show()
