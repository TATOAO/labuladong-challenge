from itertools import product, combinations

def get_choose_m_from_n(n, m):
    iterator = (range(d,i+d) for d,i in enumerate(range(n, m-1, -1)))
    return iterator

for i in combinations(range(5), 3):
    print(i)


# iterators = product(*get_choose_m_from_n(5, 3))
# for i in iterators:
#     print(i)
