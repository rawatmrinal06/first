game = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

gameA=[]
gameB = []
for j in range(0,3):
    gameA.append([0,0,0])
    gameB.append([0,0,0])

def trans(go):
    return [[x[i] for x in go] for i in range(len(go[0]))]

def getMatrixOfAandB():
    for i in range(0,len(game)):
        for j in range(0,len(game)):
           if game[i][j] == 1:
                gameA[i][j] = game[i][j]
           elif game[i][j] == 2:
               gameB[i][j] = game[i][j]

getMatrixOfAandB()
winner = False

def gameWinner(g,total,winner):
    isWinner = False
    for i in g:
        tot = 0
        for j in i:
            tot += j
        if tot == total:
            isWinner = True
            print winner+" is winner"
            return isWinner
    print g
    g = trans(g)
    print g
    for i in g:
        tot = 0
        for j in i:
            tot += j
        if tot == total:
            isWinner = True
            print winner+" is winner"
            return isWinner

    tot = 0
    for i in range(0, len(g)):
        tot += g[i][i]
        if tot == total:
            isWinner = True
            print winner+" is winner"
            return isWinner
    return isWinner

winner = gameWinner(gameA,3,"A")
if not winner:
    winner = gameWinner(gameB,6,"B")
if not winner:
    print "Match Draw"