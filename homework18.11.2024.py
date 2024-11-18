first: int = int(input('ведите целое число: '))
second: int = int(input('ведите целое число: '))
third: int = int(input('ведите целое число: '))
free: int = 3
two: int = 2
zero: int = 0
equal_all = (first == second) and (second == third)
equal_two = (first == second) or (first == third) or (second == third)
if equal_all:
    print(free)
elif equal_two:
    print(two)
else:
    print(zero)