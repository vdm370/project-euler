import math

number = 600851475143
i = 2
lst = 0
sqrt = int(math.sqrt(number))
for i in range(2, sqrt + 1):
	while number % i == 0:
		lst = i
		number = number // i
if number > 1:
	lst = number
print(lst)
