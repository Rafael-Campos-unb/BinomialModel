
def factorial(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x


def probability(a, N: list):
    n_a = []
    for i in N:
        if i == a:
            n_a.append(a)
    return len(n_a) / len(N)


# prob_dado = probability(3, [1, 2, 3, 4, 5, 6])
# print(prob_dado)

class Binomial:
    def __init__(self, n: int, k: int, p: float):
        self.n = n
        self.k = k
        self.p = p

    def combination(self):
        return factorial(self.n) / (factorial(self.k) * factorial(self.n - self.k))

    def BinomialProbability(self):
        return (self.combination() * pow(self.p, self.k) * pow(1 - self.p, self.n - self.k))*100


# binomial = Binomial(6, 2, 0.05)
# binomial_prob = binomial.BinomialProbability()
# print(binomial_prob)