# just test of GIT, nothing else

# comprehension #1
# generator of pairs: index and integer from specified range
print({key: value for key, value in enumerate(range(100, 0, -2))})

# comprehension #2
# number of unique numbers as result of multiplication up to 100
print(len({x*y for x in range(1, 11) for y in range(1, 11)}))

# comprehension #3
# sequant power for number 2
print([2**i for i in range(65)])
