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

# comprehension #4
# results of multiplication all numbers in range 0 - 10
print({x*y for x in range(1,11) for y in range(1,11)})
print(len({x*y for x in range(1,11) for y in range(1,11)}))

# comprehension #5
# results of multiplication all different numbers in range 0 - 10
print({x*y for x in range(1,11) for y in range(1,11) if x != y})
print(len({x*y for x in range(1,11) for y in range(1,11) if x != y}))

# comprehension #6
# dict – key: value
print({x: x*x for x in range(-5, 6)})
print(len({x: x*x for x in range(-5, 6)}))
