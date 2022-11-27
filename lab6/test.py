import numpy as np
"""
doska = []
n = range(1,9)
a = ["a","b","c","d","e","f","f","h"]
for i in a:
    for j in n:
        doska.append(i + str(j))

doska = np.array(doska)
doska = doska.reshape((8,8))
print(doska)"""

l = list('abcdefjh')
board = np.chararray((8, 8), itemsize=2, unicode=True)
for i in range(len(l)):
    for j in range(len(l)):
        board[j][i] = f'{l[i]}{j+1}'
        
print(board)

