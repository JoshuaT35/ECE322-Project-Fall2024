from allpairspy import AllPairs

parameters = [
    [0, 1, -10**6, 10**6],  # x values
    [0, 1, -10**6, 10**6]   # y values
]

for pair in AllPairs(parameters):
    print(pair)
