first_hundred = [i for i in range(1, 101)]
print(sum(first_hundred) ** 2 - sum([x * x for x in first_hundred]))
