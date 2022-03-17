transitions = ['H', 'N', 'N', 'S', 'S', 'H', 'H', 'H', 'S', 'S', 'N', 'S', 'H', 'N', 'H', 'S', 'H', 'H', 'S', 'S', 'H', 'N', 'H', 'N', 'S', 'S', 'N', 'N', 'N', 'H', 'S', 'H', 'S', 'N', 'H', 'N', 'S', 'S', 'N', 'N', 'S', 'S', 'N', 'S', 'N', 'H', 'N', 'H', 'N', 'H', 'S', 'N', 'H', 'N', 'H', 'S', 'H', 'H', 'N', 'N', 'N', 'S', 'H', 'H', 'H', 'N', 'N', 'H', 'H', 'N', 'H', 'N', 'N', 'S', 'S', 'S', 'N', 'N', 'N', 'N', 'H', 'N', 'N', 'H', 'H', 'S', 'H', 'S', 'S', 'H', 'N', 'S', 'N', 'S', 'S', 'S', 'S', 'H', 'H', 'N', 'S', 'S', 'H', 'S', 'H', 'H', 'S', 'H', 'N', 'S', 'S', 'S', 'H', 'H', 'N', 'S', 'N', 'N', 'S', 'H', 'H', 'S', 'H', 'H', 'N', 'H', 'H', 'H', 'H', 'N', 'S', 'S', 'N', 'N', 'N', 'S', 'N', 'H', 'N', 'S', 'S', 'H', 'S', 'H', 'N', 'H', 'H', 'N', 'S', 'H', 'N', 'S', 'S', 'S', 'S', 'H', 'N', 'H', 'H', 'S', 'N', 'S', 'S', 'S', 'S', 'N', 'H', 'H', 'S', 'S', 'S', 'H', 'N', 'N', 'N', 'N', 'N', 'S', 'H', 'S', 'N', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'N', 'S', 'N', 'N', 'H', 'N', 'N', 'H', 'H', 'H', 'H', 'H', 'H', 'N', 'H', 'N', 'H', 'H', 'S', 'N', 'N', 'N', 'N', 'H', 'N', 'H', 'H', 'N', 'S', 'S', 'N', 'H', 'H', 'S', 'S', 'S', 'N', 'N', 'H', 'N', 'N', 'H', 'H', 'N', 'S', 'S', 'N', 'H', 'H', 'S', 'S', 'S', 'N', 'N', 'S', 'S', 'H', 'N', 'H', 'H', 'H', 'H', 'H', 'N', 'N', 'N', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'H', 'S', 'S', 'N', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'N', 'N', 'H', 'H', 'H', 'S', 'H', 'N', 'N', 'H', 'S', 'H', 'H', 'N', 'N', 'N', 'N', 'H', 'H', 'N', 'N', 'N', 'H', 'H', 'N', 'N', 'N', 'H', 'N', 'H', 'N', 'S', 'N', 'N', 'N', 'H', 'H', 'H', 'H', 'N', 'H', 'H', 'N', 'H', 'H', 'H', 'H', 'N', 'N', 'S', 'H', 'N', 'H', 'N', 'H', 'N', 'N', 'N', 'H', 'H', 'H', 'H', 'S', 'H', 'H', 'H', 'N', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'N', 'N', 'S', 'H', 'H', 'H', 'H', 'H', 'H', 'N', 'H']

#make a new list that is compatible with rank and order functions

abctransitions = []

#Make list replacing H, N, and S letters with A, B, and C so we can use the rank() function later on.

for state in transitions:
    if state == "H":
        abctransitions.append("A")
    if state == "N":
        abctransitions.append("B")
    if state == "S":
        abctransitions.append("C")
    continue


def rank(c):
    return ord(c) - ord('A')

T = [rank(c) for c in abctransitions]

#create matrix of zeros

M = [[0]*3 for _ in range(3)]

for (i,j) in zip(T,T[1:]):
    M[i][j] += 1

#now convert to probabilities:
for row in M:
    n = sum(row)
    if n > 0:
        row[:] = [f/sum(row) for f in row]

#print M:

for row in M:
    print(row)
