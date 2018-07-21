#Number of queens
print ("Enter the number of queens")
N = int(input())


#chessboard
#NxN matrix with all elements 0
board = [['.']*N for _ in range(N)]

def is_attack(i, j):
    #checking if there is a queen in row or column
    for k in range(0,N):
        #row and column
        if board[i][k]=='Q' or board[k][j]=='Q':
            return True
    #checking diagonals
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]=='Q':
                    return True
    return False

def N_queen(n):
    #if n is 0, solution found
    print (n)
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            '''checking if we can place a queen here or not
            queen will not be placed if the place is being attacked
            or already occupied'''
            if (not(is_attack(i,j))) and (board[i][j]!='Q'):
                board[i][j] = 'Q'
                #recursion
                #wether we can put the next queen with this arrangment or not
                if N_queen(n-1)==True:
                    return True
                board[i][j] = '.'        
    return False


if not(N_queen(N)):
    print('no solution found')
for i in board:
    print (' '.join(i))
